#
# BitBake Graphical GTK User Interface
#
# Copyright (C) 2011        Intel Corporation
#
# Authored by Joshua Lock <josh@linux.intel.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import gtk
import gobject
import re

class BuildRep(gobject.GObject):

    def __init__(self, userpkgs, allpkgs, base_image=None):
        gobject.GObject.__init__(self)
        self.base_image = base_image
        self.allpkgs = allpkgs
        self.userpkgs = userpkgs

    def loadRecipe(self, pathname):
        contents = []
        packages = ""
        base_image = ""

        with open(pathname, 'r') as f:
            contents = f.readlines()

        pkg_pattern = "^\s*(IMAGE_INSTALL)\s*([+=.?]+)\s*(\".*?\")"
        img_pattern = "^\s*(require)\s+(\S+.bb)"

        for line in contents:
            matchpkg = re.search(pkg_pattern, line)
            matchimg = re.search(img_pattern, line)
            if matchpkg:
                packages = packages + matchpkg.group(3).strip('"')
            if matchimg:
                base_image = os.path.basename(matchimg.group(2)).split(".")[0]

        self.base_image = base_image
        self.userpkgs = packages

    def writeRecipe(self, writepath, model):
        template = """
# Recipe generated by the HOB

require %s

IMAGE_INSTALL += "%s"
"""

        empty_template = """
# Recipe generated by the HOB

inherit core-image

IMAGE_INSTALL = "%s"
"""
        if self.base_image and not self.base_image == "empty":
            meta_path = model.find_image_path(self.base_image)
            recipe = template % (meta_path, self.userpkgs)
        else:
            recipe = empty_template % self.allpkgs

        if os.path.exists(writepath):
            os.rename(writepath, "%s~" % writepath)

        with open(writepath, 'w') as r:
            r.write(recipe)

        return writepath

class TaskListModel(gtk.ListStore):
    """
    This class defines an gtk.ListStore subclass which will convert the output
    of the bb.event.TargetsTreeGenerated event into a gtk.ListStore whilst also
    providing convenience functions to access gtk.TreeModel subclasses which
    provide filtered views of the data.
    """
    (COL_NAME, COL_DESC, COL_LIC, COL_GROUP, COL_DEPS, COL_BINB, COL_TYPE, COL_INC, COL_IMG, COL_PATH, COL_PN) = range(11)

    __gsignals__ = {
        "tasklist-populated" : (gobject.SIGNAL_RUN_LAST,
                                gobject.TYPE_NONE,
                                ()),
        "contents-changed"   : (gobject.SIGNAL_RUN_LAST,
                                gobject.TYPE_NONE,
                                (gobject.TYPE_INT,)),
        "image-changed"      : (gobject.SIGNAL_RUN_LAST,
                                gobject.TYPE_NONE,
                                (gobject.TYPE_STRING,)),
        }

    """
    """
    def __init__(self):
        self.contents = None
        self.tasks = None
        self.packages = None
        self.images = None
        self.selected_image = None
        
        gtk.ListStore.__init__ (self,
                                gobject.TYPE_STRING,
                                gobject.TYPE_STRING,
                                gobject.TYPE_STRING,
                                gobject.TYPE_STRING,
                                gobject.TYPE_STRING,
                                gobject.TYPE_STRING,
                                gobject.TYPE_STRING,
                                gobject.TYPE_BOOLEAN,
                                gobject.TYPE_BOOLEAN,
                                gobject.TYPE_STRING,
                                gobject.TYPE_STRING)

    """
    Helper method to determine whether name is a target pn
    """
    def non_target_name(self, name):
        if ('-native' in name) or ('-cross' in name) or name.startswith('virtual/'):
            return True
        return False

    def contents_changed_cb(self, tree_model, path, it=None):
        pkg_cnt = self.contents.iter_n_children(None)
        self.emit("contents-changed", pkg_cnt)

    def contents_model_filter(self, model, it):
        if not model.get_value(it, self.COL_INC) or model.get_value(it, self.COL_TYPE) == 'image':
            return False
        name = model.get_value(it, self.COL_NAME)
        if self.non_target_name(name):
            return False
        else:
            return True

    """
    Create, if required, and return a filtered gtk.TreeModel
    containing only the items which are to be included in the
    image
    """
    def contents_model(self):
        if not self.contents:
            self.contents = self.filter_new()
            self.contents.set_visible_func(self.contents_model_filter)
            self.contents.connect("row-inserted", self.contents_changed_cb)
            self.contents.connect("row-deleted", self.contents_changed_cb)
        return self.contents
    
    """
    Helper function to determine whether an item is a task
    """
    def task_model_filter(self, model, it):
        if model.get_value(it, self.COL_TYPE) == 'task':
            return True
        else:
            return False

    """
    Create, if required, and return a filtered gtk.TreeModel
    containing only the items which are tasks
    """
    def tasks_model(self):
        if not self.tasks:
            self.tasks = self.filter_new()
            self.tasks.set_visible_func(self.task_model_filter)
        return self.tasks

    """
    Helper function to determine whether an item is an image
    """
    def image_model_filter(self, model, it):
        if model.get_value(it, self.COL_TYPE) == 'image':
            return True
        else:
            return False

    """
    Create, if required, and return a filtered gtk.TreeModel
    containing only the items which are images
    """
    def images_model(self):
        if not self.images:
            self.images = self.filter_new()
            self.images.set_visible_func(self.image_model_filter)
        return self.images

    """
    Helper function to determine whether an item is a package
    """
    def package_model_filter(self, model, it):
        if model.get_value(it, self.COL_TYPE) != 'package':
            return False
        else:
            name = model.get_value(it, self.COL_NAME)
            if self.non_target_name(name):
                return False
            return True

    """
    Create, if required, and return a filtered gtk.TreeModel
    containing only the items which are packages
    """
    def packages_model(self):
        if not self.packages:
            self.packages = self.filter_new()
            self.packages.set_visible_func(self.package_model_filter)
        return self.packages

    """
    The populate() function takes as input the data from a
    bb.event.TargetsTreeGenerated event and populates the TaskList.
    Once the population is done it emits gsignal tasklist-populated
    to notify any listeners that the model is ready
    """
    def populate(self, event_model):
        # First clear the model, in case repopulating
        self.clear()
        for item in event_model["pn"]:
            atype = 'package'
            name = item
            summary = event_model["pn"][item]["summary"]
            lic = event_model["pn"][item]["license"]
            group = event_model["pn"][item]["section"]
            filename = event_model["pn"][item]["filename"]
            if ('task-' in name):
                atype = 'task'
            elif ('-image-' in name):
                atype = 'image'

            # Create a combined list of build and runtime dependencies and
            # then remove any duplicate entries and any entries for -dev
            # packages
            depends = event_model["depends"].get(item, [])
            rdepends = event_model["rdepends-pn"].get(item, [])
            packages = {}
            for pkg in event_model["packages"]:
                if event_model["packages"][pkg]["pn"] == name:
                    deps = []
                    deps.extend(depends)
                    deps.extend(event_model["rdepends-pkg"].get(pkg, []))
                    deps.extend(rdepends)
                    deps = self.squish(deps)
                    # rdepends-pn includes pn-dev
                    if ("%s-dev" % item) in deps:
                        deps.remove("%s-dev" % item)
                    # rdepends-on includes pn
                    if pkg in deps:
                        deps.remove(pkg)
                    packages[pkg] = deps

            for p in packages:
                self.set(self.append(), self.COL_NAME, p, self.COL_DESC, summary,
                         self.COL_LIC, lic, self.COL_GROUP, group,
                         self.COL_DEPS, " ".join(packages[p]), self.COL_BINB, "",
                         self.COL_TYPE, atype, self.COL_INC, False,
                         self.COL_IMG, False, self.COL_PATH, filename,
                         self.COL_PN, item)

	self.emit("tasklist-populated")

    """
    Load a BuildRep into the model
    """
    def load_image_rep(self, rep):
        # Unset everything
        it = self.get_iter_first()
        while it:
            path = self.get_path(it)
            self[path][self.COL_INC] = False
            self[path][self.COL_IMG] = False
            it = self.iter_next(it)

        # Iterate the images and disable them all
        it = self.images.get_iter_first()
        while it:
            path = self.images.convert_path_to_child_path(self.images.get_path(it))
            name = self[path][self.COL_NAME]
            if name == rep.base_image:
                self.include_item(path, image_contents=True)
            else:
                self[path][self.COL_INC] = False
            it = self.images.iter_next(it)

        # Mark all of the additional packages for inclusion
        packages = rep.userpkgs.split(" ")
        it = self.get_iter_first()
        while it:
            path = self.get_path(it)
            name = self[path][self.COL_NAME]
            if name in packages:
                self.include_item(path, binb="User Selected")
                packages.remove(name)
            it = self.iter_next(it)

        self.emit("image-changed", rep.base_image)

    """
    squish lst so that it doesn't contain any duplicate entries
    """
    def squish(self, lst):
        seen = {}
        for l in lst:
            seen[l] = 1
        return seen.keys()

    """
    Mark the item at path as not included
    NOTE:
    path should be a gtk.TreeModelPath into self (not a filtered model)
    """
    def remove_item_path(self, path):
        self[path][self.COL_BINB] = ""
        self[path][self.COL_INC] = False

    """
    Recursively called to mark the item at opath and any package which
    depends on it for removal.
    NOTE: This method dumbly removes user selected packages and since we don't
    do significant reverse dependency tracking it's easier and simpler to save
    the items marked as user selected and re-add them once the removal sweep is
    complete.
    """
    def mark(self, opath):
        usersel = {}
        removed = []

        it = self.get_iter_first()
        # The name of the item we're removing, so that we can use it to find
        # other items which either depend on it, or were brought in by it
        marked_name = self[opath][self.COL_NAME]

        # Remove the passed item
        self.remove_item_path(opath)

        # Remove all dependent packages, update binb
        while it:
            path = self.get_path(it)
            it = self.iter_next(it)

            inc = self[path][self.COL_INC]
            deps = self[path][self.COL_DEPS]
            binb = self[path][self.COL_BINB].split(', ')
            itype = self[path][self.COL_TYPE]
            itname = self[path][self.COL_NAME]

            # We ignore anything that isn't a package
            if not itype == "package":
                continue

            # If the user added this item and it's not the item we're removing
            # we should keep it and its dependencies, the easiest way to do so
            # is to save its name and re-mark it for inclusion once dependency
            # processing is complete
            if "User Selected" in binb:
                usersel[itname] = self[path][self.COL_IMG]

            # If the iterated item is included and depends on the removed
            # item it should also be removed.
            # FIXME: need to ensure partial name matching doesn't happen
            if inc and marked_name in deps and itname not in removed:
                # found a dependency, remove it
                removed.append(itname)
                self.mark(path)

            # If the iterated item was brought in by the removed (passed) item
            # try and find an alternative dependee and update the binb column
            if inc and marked_name in binb:
                binb.remove(marked_name)
                self[path][self.COL_BINB] = ', '.join(binb).lstrip(', ')

        # Re-add any removed user selected items
        for u in usersel:
            npath = self.find_path_for_item(u)
            self.include_item(item_path=npath,
                              binb="User Selected",
                              image_contents=usersel[u])
    """
    Remove items from contents if the have an empty COL_BINB (brought in by)
    caused by all packages they are a dependency of being removed.
    If the item isn't a package we leave it included.
    """
    def sweep_up(self):
        it = self.contents.get_iter_first()
        while it:
            binb = self.contents.get_value(it, self.COL_BINB)
            itype = self.contents.get_value(it, self.COL_TYPE)
            remove = False

            if itype == 'package' and not binb:
                oit = self.contents.convert_iter_to_child_iter(it)
                opath = self.get_path(oit)
                self.mark(opath)
                remove = True

            # When we remove a package from the contents model we alter the
            # model, so continuing to iterate is bad. *Furthermore* it's
            # likely that the removal has affected an already iterated item
            # so we should start from the beginning anyway.
            # Only when we've managed to iterate the entire contents model
            # without removing any items do we allow the loop to exit.
            if remove:
                it = self.contents.get_iter_first()
            else:
                it = self.contents.iter_next(it)

    """
    Check the self.contents gtk.TreeModel for an item
    where COL_NAME matches item_name
    Returns True if a match is found, False otherwise
    """
    def contents_includes_name(self, item_name):
        it = self.contents.get_iter_first()
        while it:
            path = self.contents.get_path(it)
            if self.contents[path][self.COL_NAME] == item_name:
                return True
            it = self.contents.iter_next(it)
        return False

    """
    Add this item, and any of its dependencies, to the image contents
    """
    def include_item(self, item_path, binb="", image_contents=False):
        name = self[item_path][self.COL_NAME]
        deps = self[item_path][self.COL_DEPS]
        cur_inc = self[item_path][self.COL_INC]
        if not cur_inc:
            self[item_path][self.COL_INC] = True

        bin = self[item_path][self.COL_BINB].split(', ')
        if not binb in bin:
            bin.append(binb)
            self[item_path][self.COL_BINB] = ', '.join(bin).lstrip(', ')

        # We want to do some magic with things which are brought in by the
        # base image so tag them as so
        if image_contents:
            self[item_path][self.COL_IMG] = True
            if self[item_path][self.COL_TYPE] == 'image':
                self.selected_image = name

        if deps:
            # add all of the deps and set their binb to this item
            for dep in deps.split(" "):
                # If the contents model doesn't already contain dep, add it
                dep_included = self.contents_includes_name(dep)
                path = self.find_path_for_item(dep)
                if not path:
                    continue
                if dep_included:
                    bin = self[path][self.COL_BINB].split(', ')
                    bin.append(name)
                    self[path][self.COL_BINB] = ', '.join(bin).lstrip(', ')
                else:
                    self.include_item(path, binb=name, image_contents=image_contents)

    """
    Find the model path for the item_name
    Returns the path in the model or None
    """
    def find_path_for_item(self, item_name):
        # We don't include virtual/* or *-native items in the model so save a
        # heavy iteration loop by exiting early for these items
        if self.non_target_name(item_name):
            return None

        it = self.get_iter_first()
        path = None
        while it:
            path = self.get_path(it)
            if (self[path][self.COL_NAME] == item_name):
                return path
            else:
                it = self.iter_next(it)
        return None

    """
    Empty self.contents by setting the include of each entry to None
    """
    def reset(self):
        # Deselect images - slightly more complex logic so that we don't
        # have to iterate all of the contents of the main model, instead
        # just iterate the images model.
        if self.selected_image:
            iit = self.images.get_iter_first()
            while iit:
                pit = self.images.convert_iter_to_child_iter(iit)
                self.set(pit, self.COL_INC, False)
                iit = self.images.iter_next(iit)
            self.selected_image = None

        it = self.contents.get_iter_first()
        while it:
            oit = self.contents.convert_iter_to_child_iter(it)
            self.set(oit,
                     self.COL_INC, False,
                     self.COL_BINB, "",
                     self.COL_IMG, False)
            # As we've just removed the first item...
            it = self.contents.get_iter_first()

    """
    Returns two lists. One of user selected packages and the other containing
    all selected packages
    """
    def get_selected_packages(self):
        allpkgs = []
        userpkgs = []

        it = self.contents.get_iter_first()
        while it:
            sel = "User Selected" in self.contents.get_value(it, self.COL_BINB)
            name = self.contents.get_value(it, self.COL_NAME)
            allpkgs.append(name)
            if sel:
                userpkgs.append(name)
            it = self.contents.iter_next(it)
        return userpkgs, allpkgs

    """
    Return a squished (uniquified) list of the PN's of all selected items
    """
    def get_selected_pn(self):
        pns = []

        it = self.contents.get_iter_first()
        while it:
            if self.contents.get_value(it, self.COL_BINB):
                pns.append(self.contents.get_value(it, self.COL_PN))
            it = self.contents.iter_next(it)

        return self.squish(pns)

    def image_contents_removed(self):
        it = self.get_iter_first()
        while it:
            sel = self.get_value(it, self.COL_INC)
            img = self.get_value(it, self.COL_IMG)
            if img and not sel:
                return True
            it = self.iter_next(it)
        return False

    def get_build_rep(self):
        userpkgs, allpkgs = self.get_selected_packages()
        # If base image contents have been removed start from an empty rootfs
        if not self.selected_image or self.image_contents_removed():
            image = "empty"
        else:
            image = self.selected_image

        return BuildRep(" ".join(userpkgs), " ".join(allpkgs), image)

    def find_reverse_depends(self, pn):
        revdeps = []
        it = self.contents.get_iter_first()

        while it:
            name = self.contents.get_value(it, self.COL_NAME)
            itype = self.contents.get_value(it, self.COL_TYPE)
            deps = self.contents.get_value(it, self.COL_DEPS)

            it = self.contents.iter_next(it)

            if not itype == 'package':
                continue

            if pn in deps:
                revdeps.append(name)

        if pn in revdeps:
            revdeps.remove(pn)
        return revdeps

    def set_selected_image(self, img):
        self.selected_image = img
        path = self.find_path_for_item(img)
        self.include_item(item_path=path,
                          binb="User Selected",
                          image_contents=True)

        self.emit("image-changed", self.selected_image)

    def set_selected_packages(self, pkglist):
        selected = pkglist
        it = self.get_iter_first()

        while it:
            name = self.get_value(it, self.COL_NAME)
            if name in pkglist:
                pkglist.remove(name)
                path = self.get_path(it)
                self.include_item(item_path=path,
                                  binb="User Selected")
                if len(pkglist) == 0:
                    return
            it = self.iter_next(it)

    def find_image_path(self, image):
        it = self.images.get_iter_first()

        while it:
            image_name = self.images.get_value(it, self.COL_NAME)
            if image_name == image:
                path = self.images.get_value(it, self.COL_PATH)
                meta_pattern = "(\S*)/(meta*/)(\S*)"
                meta_match = re.search(meta_pattern, path)
                if meta_match:
                    _, lyr, bbrel = path.partition(meta_match.group(2))
                    if bbrel:
                        path = bbrel
                return path
            it = self.images.iter_next(it)
