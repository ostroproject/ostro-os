#!/bin/sh
# Hook to add source component/revision info to commit message
# Parameter:
#   $1 patch-file
#   $2 revision
#   $3 reponame

patchfile=$1
rev=$2
reponame=$3

# If the existing prefix is unique enough (= already the repository name or
# one of the layers inside it), then keep it as-is without adding the
# component name. Otherwise add the component name as prefix in front of
# the existing subject line.
perl -e "while(<>) {
   if (s/^Subject: \[PATCH\] (?:($reponame|meta-\S+-fixes): )?/'Subject: [PATCH] ' . ((\$1 == '$reponame' || \$1 != '') && \$1 || '$reponame') . ': '/e) {
      print;
      last;
   } else {
      print;
   }
}
while(<>) {
   print;
}" <$patchfile >$patchfile.tmp
mv $patchfile.tmp $patchfile

if grep -q '^Signed-off-by:' $patchfile; then
    # Insert before Signed-off-by.
    sed -i -e "0,/^Signed-off-by:/s#\(^Signed-off-by:.*\)#\(From $reponame rev: $rev\)\n\n\1#" $patchfile
else
    # Insert before final --- separator, with extra blank lines removed.
    perl -e "\$_ = join('', <>); s/^(.*\S[ \t]*)(\n|\n\s*\n)---\n/\$1\n\nFrom $reponame rev: $rev\n---\n/s; print;" $patchfile >$patchfile.tmp
    mv $patchfile.tmp $patchfile
fi
