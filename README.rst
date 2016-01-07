About this repository
=====================

This repository is a combination of several different components in a
single repository:

- bitbake
- openembedded-core
- meta-intel
- meta-ostro
- meta-oic
- meta-intel-iot-middleware
- meta-intel-iot-security
- meta-ostro-fixes
- meta-ostro-bsp
- meta-iot-web
- meta-yocto-bsp (from the meta-yocto git repository)
- meta-iotqa
- meta-user-management
- meta-sensor-framework
- meta-appfw
- meta-java

The top-level directory comes from openembedded-core, everything else
is in its own sub-directory. This repository gets updated by importing
commits from the component's repostories. It is convenient to make
changes in this repository and then publish the result, for example in
a sandbox or clone of the repository. However, to get changes merged,
please submit them against the upstream components.

Updating the repository
=======================

Everyone with a copy of the repository can use ``scripts/combo-layer`` to
import commits from the components. That works because the
``last_revision`` property which gets changed after each import gets
committed to the combined repostory.

First, copy ``conf/combo-layer-local-sample.conf`` into
conf/combo-layer-local.conf and set the paths for each component
repository to a suitable location.

Then run:

- ``scripts/combo-layer init`` (only once)
- ``scripts/combo-layer update <component>`` where <component> is either one of
   components above (for updating just that one) or empty (for updating all)
- optional: ``git commit --amend`` the last auto-generated commit

Branching
=========

Each branch in this repository tracks one branch in each component. To
create a new branch:

- checkout a new branch at a suitable base
- change the "branch" properties in ``conf/combo-layer.conf``
- change the branch part in the ``last_revision`` sections
- commit
- continue as before

This works best if the last imported revision from each component is
the branching point of that component. Ensure that by updating before
the components branch. If it is too late, either select commits
interactively (``combo-layer --interactive``) or import too many commits
and then drop unwanted ones via ``git rebase`` or ``git reset
--hard``. Remember to keep ``last_revision`` correct when doing that.
