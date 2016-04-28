.. _pull-request-guidelines:

Ostro |trade| OS Pull Request Guidelines
########################################

The :ref:`contributor-guide` explains how to submit changes as pull
requests (PRs) and how they will get merged.

This document complements those instructions with more hands-on
guidelines about what information will be needed during a review, what
kind of mistakes to watch out for during review, and how to deal with
PRs.

The goal is to make the review process more consistent and help less
experienced reviewers in catching potential mistakes that otherwise
might get overlooked. A submitter can use this to avoid these mistakes
before even submitting the pull request.

Workflow
========

PRs are typically checked in this order:

1. pull request message
2. commit messages
3. actual diff

Reviewers should be aware of that context before looking at the diff
and, when in doubt, also look at the entire file that gets modified
to ensure that the change is consistent with the rest.

If reviewers find issues with the PR, a review of all changes may be
abandoned early with a request to the submitter to fix those things
first before the review continues.

Pull Request Message
====================

The main pull request message summarizes the change. Relevant
information is how important the PR is, whether there are dependencies
on other PRs, and who should, might, or needs to review it.

Submitters should mention specific reviewers (if known) by using their
Github handle with the at symbol to alert them of the PR, as in
``@johndoe please review`` or ``@joandoe needs to review this``.

Commit Messages
===============

Your commit messages should follow the format explained in
:ref:`contributor-guide`, for the sake of consistency and
completeness.

The commit message will be used in different ways and with different
goals:

* Listing commits (for example, ``git log --oneline``, Jenkins PR overview pages, ``gitk``):
  the first line should be informative and ideally unique.
* Reviewing the change: what is the motivation for the change, why
  was it solved this way?
* Distro maintenance at a later point in time: is the change still relevant?
  What breaks if the change has to removed or modified? This might also
  get answered in the actual code, but sometimes there is additional information
  like verbatim copies of error messages that are too large for the code
  itself. Storing them in the commit message preserves that additional
  information (see next point).
* Searching for problems and how they were solved: ``git log --grep`` can be
  useful to find commits again.
* Commit author: when including something written by others (like patches
  or complete files), try to submit that in a separate commit with the
  original author set as author of the commit. This is important for tracking
  the origin of code in Ostro OS, which is assisted by automated tooling.
  When multiple people authored the change, use the upstream project's
  mailing list as author. Alternatively, using ``git am`` format for patches
  can also be used to document the author of a code patch (see next section).


Content of a Pull Request
=========================

When a change affects user-visible behavior, make sure that relevant
user documentation gets updated, ideally in the same commit (only
works when submitting to ``meta-ostro``, which is where the ``doc``
directory is maintained). If that is not possible or not desirable at
the time, include enough information in the change or commit message
for a technical writer to update the Ostro OS user documentation
later.

Avoid unnecessary changes, like arbitrarily reformatting unrelated code.

Avoid mixing unrelated changes in the same commit. Changes that are
not mentioned in the commit message are questionable because they may
have been included accidentally. Split large changes into smaller,
individual commits because they are easier to review. They also
support bisecting better when there are problems.

When adding patches inside a PR:

* It is really necessary? Can the problem be fixed upstream first? Are
  there other solutions that are easier to maintain?
* Document the patch status by adding a ``Upstream-Status`` line in
  the `patch header`_. "Pending" patches are discouraged because they
  contribute to the technical debt in Ostro OS.
* The author of the patch must be clear, either by using ``git am``
  format with an ``Author:`` line, adding such a line manually to
  the patch header, or by committing the entire file with the author
  of the commit set to the author of the patch.

.. _patch header: http://www.openembedded.org/wiki/Commit_Patch_Message_Guidelines#Patch_Header_Recommendations

Adding or removing layers needs to be done in two separate PRs:

* In the ``ostro-os`` repo, update ``combo-layer.conf`` and ``combo-layer-local-sample.conf``,
  then include the initial import of the new component in the PR.
* In the ``meta-ostro`` repo, update:

  * ``.gitignore`` - imported files must not be ignored
  * ``README.rst`` - the list of layers
  * ``meta-ostro/conf/bblayers.conf.sample`` - add the layer and increase
    ``LCONF_VERSION`` by one
  * ``meta-ostro/conf/layer.conf`` - increase ``LAYER_CONF_VERSION``
    by one. It must match ``LCONF_VERSION``.

The layer config file versioning ensures that developers who update to
a new revision of ``ostro-os`` where the new layer was added are told
to update their local ``bblayers.conf`` when invoking bitbake in older
build directories

Similarly, when making changes to ``local.conf.sample``,
increase both ``LOCALCONF_VERSION`` in ``meta-ostro/conf/layer.conf``
and ``CONF_VERSION`` in ``meta-ostro/conf/local.conf.sample``.

Dos and Don'ts
==============

* When providing feedback, be clear whether you consider highlighted
  issues as critical enough that they need to be fixed before merging.

* Try to write correct English. Use a spell checker when
  unsure. Pointing out language mistakes is acceptable during a review,
  but typically is considered a minor issue that the submitter may or
  may not want to fix. Review comments about spelling, grammar, and
  clarity in documentation should be addressed.

* A code review typically is done by just looking at a change. Review
  comments such as ``Looks good to me = LGTM``, ``+1`` or adding a
  positive reaction via the Github button typically just means that
  the reviewer has agreed to merge the pull request based on such a
  visual inspection.

* The submitter is expected to have tested the change, i.e. it is
  expected to work at a functional level. However, exhaustive testing
  often is not possible. So when there is additional need for testing,
  describe that.

* If a reviewer actually tries out a change, that should be mentioned
  in a review comment because it provides additional assurance that a
  pull request is really okay.

* :ref:`contributor-guide` explains when a PR is considered ready for
  merging (enough time to provide feedback, no objections, etc.).

* The Ostro project uses Github's non-fast-forward merges (aka the
  "merge" button in the Gitub web interface). The reason is that this
  style of merging records when commits were merged and by whom. The
  merge commit message can be used to add additional information about
  the merge (but in practice, that is not done often). Automatic testing
  happens only for the full set of commits that are getting merged, so
  when bisecting history, the merge commits are good candidates for
  testing because they are more likely to build correctly.
