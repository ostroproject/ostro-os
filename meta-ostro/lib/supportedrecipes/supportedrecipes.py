# Python code implementing most of the logic behind
# supported-recipes.bbclass.

import bb
import csv
import exceptions
import os
import re
import urlparse

def load_supported_recipes(d):
    class SupportedRecipe:
        def __init__(self, pattern, filename, linenumber):
            self.filename = filename
            self.pattern = pattern
            self.linenumber = linenumber
            parts = pattern.split('@')
            if len(parts) != 2:
                raise exceptions.RuntimeError("%s.%d: entry must have format <recipe name regex>@<collection name regex>, splitting by @ found %d parts instead: %s" % (
                    filename,
                    linenumber,
                    len(parts),
                    pattern))
            def parse_regex(regex):
                try:
                    # must match entire string, hence the '$'
                    return (re.compile(regex + '$'), regex)
                except Exception as ex:
                    raise RuntimeError("%s.%d: parsing '%s' as regular expression failed: %s" % (
                        filename,
                        linenumber,
                        regex,
                        str(ex)))
            self.pn_re = parse_regex(parts[0])
            self.collection_re = parse_regex(parts[1])

        def supported(self, pn, collection):
            supported = bool((pn is None or self.pn_re[0].match(pn)) and
                (collection is None or self.collection_re[0].match(collection)))
            return supported

    class SupportedRecipes:
        def __init__(self):
            self.supported = []

        def append(self, recipe):
            self.supported.append(recipe)

        def current_recipe_supported(self, d):
            pn = d.getVar('PN', True)
            filename = d.getVar('FILE', True)
            collection = bb.utils.get_file_layer(filename, d)
            return self.recipe_supported(pn, collection)

        def recipe_supported(self, pn, collection):
            for supported_recipe in self.supported:
                if supported_recipe.supported(pn, collection):
                    return True
            return False

        def find_collections(self, pn):
            collections = set()
            for supported_recipe in self.supported:
                if supported_recipe.supported(pn, None):
                    collections.add(supported_recipe.collection_re[1])
            return collections

    files = []
    supported_files = d.getVar('SUPPORTED_RECIPES', True)
    if not supported_files:
        bb.fatal('SUPPORTED_RECIPES is not set')
    supported_recipes = SupportedRecipes()
    for filename in supported_files.split():
        try:
            with open(filename) as f:
                linenumber = 1
                for line in f.readlines():
                    if line.startswith('#'):
                        continue
                    # TODO (?): sanity check the content to catch obsolete entries or typos.
                    pn = line.strip()
                    if pn:
                        supported_recipes.append(SupportedRecipe(line.strip(), filename, linenumber))
                    linenumber += 1
            files.append(filename)
        except OSError, ex:
            bb.fatal('Could not read SUPPORTED_RECIPES = %s: %s' % (supported_files, str(ex)))

    return (supported_recipes, files)

# Collects information about one recipe during parsing for SUPPORTED_RECIPES_SOURCES.
# The dumped information cannot be removed because it might be needed in future
# bitbake invocations, so the default location is inside the tmp directory.
def dump_sources(d):
    pn = d.getVar('PN', True)
    filename = d.getVar('FILE', True)
    collection = bb.utils.get_file_layer(filename, d)
    pv = d.getVar('PV', True)
    summary = d.getVar('SUMMARY', True) or ''
    homepage = d.getVar('HOMEPAGE', True) or ''
    src = d.getVar('SRC_URI', True).split()
    sources = []
    for url in src:
        scheme, netloc, path, query, fragment = urlparse.urlsplit(url)
        if scheme != 'file':
            parts = path.split(';')
            if len(parts) > 1:
                path = parts[0]
                params = dict([x.split('=') if '=' in x else (x, '') for x in parts[1:]])
            else:
                params = {}
            name = params.get('name', None)
            sources.append((name, '%s://%s%s' % (scheme, netloc, path)))
    dumpfile = d.getVar('SUPPORTED_RECIPES_SOURCES_DIR', True) + '/' + pn + filename
    bb.utils.mkdirhier(os.path.dirname(dumpfile))
    with open(dumpfile, 'w') as f:
        writer = csv.writer(f)
        for idx, val in enumerate(sources):
            name, url = val
            if name and not len(sources) == 1:
                fullname = '%s/%s' % (pn, name)
            elif idx > 0:
                fullname = '%s/%d' % (pn, idx)
            else:
                fullname = pn
            writer.writerow((fullname, collection, pv, homepage, url, summary))

def check_build(d, event):
    supported_recipes, files = load_supported_recipes(d)
    supported_recipes_check = d.getVar('SUPPORTED_RECIPES_CHECK', True)
    if not supported_recipes_check:
        return

    # Always add a trailing $ to ensure a full match.
    isnative_exception = re.compile('(' + '|'.join(d.getVar('SUPPORTED_RECIPES_NATIVE_RECIPES', True).split()) + ')$')
    isnative_baseclasses = d.getVar('SUPPORTED_RECIPES_NATIVE_BASECLASSES', True).split()
    valid = ('note', 'warn', 'error', 'fatal')
    if supported_recipes_check not in valid:
        bb.fatal('SUPPORTED_RECIPES_CHECK must be set to one of %s, currently is: %s' % ('/'.join(valid), supported_recipes_check))
    logger = bb.__dict__[supported_recipes_check]

    # See bitbake/lib/bb/cooker.py buildDependTree() for the content of the depgraph hash.
    # Basically it mirrors the information dumped by "bitbake -g".
    depgraph = event._depgraph
    # import pprint
    # bb.note('depgraph: %s' % pprint.pformat(depgraph))

    dirname = d.getVar('SUPPORTED_RECIPES_SOURCES_DIR', True)
    report_sources = d.getVar('SUPPORTED_RECIPES_SOURCES', True)

    unsupported = {}
    sources = []
    for pn, pndata in depgraph['pn'].iteritems():
        # We only care about recipes compiled for the target.
        # Most native ones can be detected reliably because they inherit native.bbclass,
        # but some special cases have to be hard-coded.
        # Image recipes also do not matter.
        def isnative():
            for inherited in pndata['inherits']:
                if os.path.basename(inherited) in isnative_baseclasses:
                    return True
            # Some build recipes do not inherit cross.bbclass and must be skipped explicitly.
            # The "real" recipes (in cases like glibc) still get checked. Other recipes are OE-core
            # internal helpers.
            if isnative_exception.match(pn):
                return True
        if not isnative():
            filename = pndata['filename']
            collection = bb.utils.get_file_layer(filename, d)
            supported = supported_recipes.recipe_supported(pn, collection)
            if not supported:
                unsupported[pn] = collection
            if report_sources:
                dumpfile = dirname + '/' + pn + filename
                with open(dumpfile) as f:
                    reader = csv.reader(f)
                    for row in reader:
                        row.insert(2, 'yes' if supported else 'no')
                        sources.append(row)

    if report_sources:
        with open(report_sources, 'w') as f:
            writer = csv.writer(f)
            writer.writerow('component,collection,supported,version,homepage,source,summary'.split(','))
            for row in sorted(sources):
                writer.writerow(row)
        bb.note('Created SUPPORTED_RECIPES_SOURCES = %s file.' % report_sources)

    if unsupported:
        # Walk the recipe dependency tree and add one line for each path that ends in
        # an unsupported recipe.
        lines = []
        max_lines = int(d.getVar('SUPPORTED_RECIPES_CHECK_DEPENDENCY_LINES', True))
        current_line = []

        # Pre-compute complete dependencies (DEPEND and RDEPEND) for each recipe
        # instead of doing it each time we reach a recipe. Also identifies those
        # recipes that nothing depends on. They are the start points for the build.
        roots = set(depgraph['pn'])
        deps = {}
        for task, taskdeps in depgraph['tdepends'].iteritems():
            pn = task.split('.')[0]
            pndeps = deps.setdefault(pn, set())
            for taskdep in taskdeps:
                pndep = taskdep.split('.')[0]
                if pndep != pn:
                    pndeps.add(pndep)
                    roots.discard(pndep)
        for pn in deps.keys():
            deps[pn] = sorted(deps[pn])

        # We can prune the search tree a lot by keeping track of those recipes which are already
        # known to not depend on an unsupported recipe.
        okay = set()

        class TruncatedError(Exception):
            pass

        def visit_recipe(pn):
            if pn in okay:
                return False
            if pn in current_line:
                # Recursive dependency, bail out. Can happen
                # because we flattened the task dependencies; those don't have
                # cycles.
                return False
            current_line.append(pn)
            printed = False
            for dep in deps.get(pn, []):
                if visit_recipe(dep):
                    printed = True
            if not printed and \
               pn in unsupported and \
               not len(current_line) == 1:
                # Current path is non-trivial, ends in an unsupported recipe and was not alread
                # included in a longer, printed path. Add a copy to the output.
                if len(lines) >= max_lines:
                    raise TruncatedError()
                lines.append(current_line[:])
                printed = True
            if not printed and not pn in unsupported:
                okay.add(pn)
            del current_line[-1]
            return printed

        truncated = False
        try:
            for pn in sorted(roots):
                visit_recipe(pn)
        except TruncatedError:
            truncated = True

        def collection_hint(pn):
            '''Determines whether the recipe would be supported in some other collection.'''
            collections = supported_recipes.find_collections(pn)
            return ' (would be supported in %s)' % ' '.join(collections) if collections else ''

        logger('The following unsupported recipes are required for the build:\n  ',
               # In contrast to re.escape(), we only escape + (as in gtk+3).
               # Escaping all non-alphanumerics makes many entries (like linux-yocto)
               # unnecessarily less readable (linux\-yocto).
               '\n  '.join(sorted(['%s@%s%s' % (pn.replace('+', r'\+'), collection.replace('+', r'\+'), collection_hint(pn)) for pn, collection in unsupported.iteritems()])),
               '''

Each unsupported recipe is identified by the recipe name and the collection
in which it occurs and has to be marked as supported (see below) using that
format. Typically each layer has exactly one collection.''',
'''

Here are the dependency chains (including DEPENDS and RDEPENDS)
which include one or more of the unsupported recipes. -> means "depends on"
and * marks unsupported recipes:
  ''' if lines else '',
               '\n  '.join([' -> '.join([('*' if pn in unsupported else '') + pn for pn in line]) for line in lines]),
               ('''
  ...
  Output truncated, to see more increase SUPPORTED_RECIPES_CHECK_DEPENDENCY_LINES
  (currently %d).''' % max_lines) if truncated else '',
               '''

To avoid this message, several options exist:
* Check the dependency chain(s) to see why a recipe gets pulled in and perhaps
  change recipe configurations or image content to avoid pulling in undesired
  components.
* If the recipe is supported in some other layer, disable the unsupported one
  with BBMASK.
* Add the unsupported recipes to one of the following files:
  %s
  Regular expressions are supported on both sides of the @ separator.
* Create a new file which lists the unsupported recipes and extend SUPPORTED_RECIPES:
    SUPPORTED_RECIPES_append = " <path>/recipes-supported-by-me.txt"
  See meta-ostro/conf/layer.conf and ostro.conf for an example how the path can be
  derived automatically. The expectation is that SUPPORTED_RECIPES gets set in
  distro configuration files, depending on the support provided by the distro
  creator.
* Disable the check with SUPPORTED_RECIPES_CHECK = "" in local.conf.
  'bitbake -g <build target>' produces .dot files showing these dependencies.
''' % '\n '.join(files)
   )
