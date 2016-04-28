.. _contributor-guide:


Ostro |trade| OS Contributor Guide
##################################

As an open-source project, we welcome and encourage the community to submit patches directly to the project. 
This document explains how to participate in project conversations, log bugs and enhancement requests, 
and submit patches to the project so your patch will be accepted quickly in the codebase. At a high-level, 
we use the GitHub Pull Request workflow and follow the `Open Embedded guidelines for commit messages`_, 
as explained in our `Code Review Process Guidelines`_ section below.

Participating in Ostro Project Conversations
============================================

As in many open source projects, we have online options for developers and community members to converse about the Ostro Project, including
an `Ostro-dev mailing list`_, `Ostro Project IRC channel`_ on freenode.net, `ostroproject GitHub repo`_, 
`bug and issue tracking`_, `Ostro OS Release Notes`_, and more.  
You can learn more about these resources and how to subscribe to and access them in :ref:`access-support`.

Communication on IRC is immediate, yet transient, making it good for meetings or a quick question. 
The mailing list is for announcements and questions for broad exposure and discussion. 
JIRA is our issue tracking system, for feature requests and bug reports.

.. _`Open Embedded guidelines for commit messages`: http://openembedded.org/wiki/Commit_Patch_Message_Guidelines
.. _`Yocto Project`: http://yoctoproject.org
.. _`Ostro OS Release Notes`: https://github.com/ostroproject/ostro-os/releases/
.. _`Ostro-dev mailing list`: mailto://ostro-dev@lists.ostroproject.org
.. _`ostroproject GitHub repo`: https://github.com/ostroproject/
.. _`Ostro Project JIRA`: https://ostroproject.org/jira
.. _`bug and issue tracking`: https://ostroproject.org/jira
.. _`Ostro Project IRC channel`: irc://#ostroproject@irc.freenode.net

Prerequisites
=============

As a contributor, you'll want to be familiar with the Ostro OS project and the `Yocto Project`_ configuration and build tools.
You should have set up your development environment (as introduced in our :ref:`quick_start`) 
and successfully built an Ostro OS image (as introduced in :ref:`Building Images`). 
As a Linux developer, you should also be familiar with common development tools such as Git and GitHub.

Logging Bugs and Enhancement Requests
=====================================

Before starting on a patch, first check in `Ostro Project JIRA`_ to see what’s been reported on the issue you’re addressing. 
Have a conversation on the mailing list to see what others think of your issue (and proposed solution). 
You may find others that have encountered the issue you're finding, or with similar ideas for changes or additions. 
If you don't, send a message to the mailing list to introduce and discuss your idea with the development community.

After logging into JIRA, click “Issues” to search for open items. To avoid duplication, it's always a good practice 
to search for existing or related issues before submitting your own. When you submit an issue (bug or feature request),
the triage team will review the submission, typically within a few business days, and update the “Priority” 
and “Target Version” and other program management fields. 


Code Review Process Guidelines
==============================

.. _`Linux Foundation Developer Certificate of Origin`: http://developercertificate.org

Here are guidelines for the review process that you and the maintainers will follow when you submit a patch for the Ostro OS:

#. Contributors follow the `Open Embedded guidelines for commit messages`_ and patches for recipes and other submissions.
   In your commit message, briefly describe what the patch does, the problem it is addressing, or why it was submitted. 
   Include additional detailed comments in the code itself, as appropriate.  
#. In the commit message, include the JIRA issue ID if available (using this notation::

    [Fixes|Related-to] OP-<number>

#. When making contributions to the Ostro project (or any open source project), it's important to confirm you have
   the rights to submit your contribution under the open source license being used by the project. The
   `Linux Foundation Developer Certificate of Origin`_ agreement explains this further.  You confirm is indicated by
   adding a "Signed-off-by" line in the commit message.

#. The general commit message format is::

     <component>: <summary>
     <description>
     [Fixes|Related-to] OP-<number>
     Signed-off-by: <name> <email>

   Variations of the tags are also acceptable, such as Fix/Fixes/Fixed.

#. For each pull request (PR), the submitter and maintainer verify the patch does not cause a Continuous Integration (CI) build to break.
   Every PR by an authorized user triggers a CI test build that shows whether this is true and the PR can be merged safely (after
   a full code review is complete).  If you're not one of the recognized contributors, your PR will get an automated comment from the 
   CI system saying "Can one of the admins verify this patch?". This means one of layer maintainers should review the code change 
   and add a comment to the PR "ok to test" or "retest this please" that informs the CI system it's OK to continue with an 
   automated CI test build.  These are messages directing the CI system and are not asking you, the contributor, to act.

#. Some PRs do not require a CI build to verify, in particular documentation-only changes. We can save CI machine cycles for such
   changes by including a special tag anywhere in the Pull Request description:::

     [skip ci]

   This advises the CI system to not do its normal CI test build for this Pull Request.  

#. For each pull request, allow enough time for feedback and questions to be provided:
     * If the change is considered trivial or review expertise is available in the same time-zone, a same-day merge might be possible,
       but shouldn't be expected.
     * If the change is complex and requires thorough review, allow a minimum of two business days for comments, to accommodate people 
       working on different schedules and in various worldwide locations. You can get the attention of a specific person
       by using the `@<github username>` notation in your comment.

#. Negative feedback must be resolved before merging
#. The layer maintainer is responsible for merging the open PR after the pull request is properly reviewed:
     * Use common sense when merging. If you are unsure, please request more feedback from the submitter and other team members
     * Layer Maintainers should respond to a PR within two business days. 
     * If no discussion has occurred within this timeframe, maintainers are responsible for contacting the PR
       submitter and other developers to request feedback, or close the pull request.

Please feel free to make comments on this code review process to the `Ostro-dev mailing list`_ mailing list.

Bug and Feature Request Tracking Process
========================================

.. note::
   We anticipate the `Ostro Project JIRA`_ issue tracking system to be live early May...

The Ostro Project includes many upstream projects. Some projects are unchanged and reused directly in Ostro; 
some are patched with Ostro OS-specific code.  While this section addresses bug reporting and tracking, a similar
approach is used for feature requests since they're also entered and tracked in JIRA and could apply to an 
upstream component used by Ostro OS. (We'll collectively refer to bugs and features as issues.)

In general, all issues found in the Ostro OS image are tracked in the `Ostro Project JIRA`_, though some are not. For example, 
if an upstream test case fails both upstream and in Ostro OS but without obvious impact to devices running Ostro OS, 
we want to avoid duplicating such minor issues in the Ostro Project JIRA. The bug should be reported
to the upstream projects' issue tracking system.

When an bug is discovered:

#. Find the proper Ostro OS component for tracking the bug:
     * If the bug is caused by Ostro OS code, an Ostro Project feature or component owner should address it. (Ostro Project
       components and the responsible owner can be found on the "Components" page in `Ostro Project JIRA`_.)
     * If the bug is caused by upstream code, the feature owner and QA owner should report in the Ostro OS JIRA and 
       map it to an upstream project’s bug tracking system. 

   Similarly for feature requests, submit them to the appropriate component or upstream project's issue tracking system.

#. Once the bug is fixed upstream, the feature owner owns merging the upstream code back into Ostro OS. 
#. QA will verify the fix with the Ostro image and update the Ostro Project bug status properly, and track the issue until it's closed.

The upstream developer and QA owner take responsibility to drive a fix. Based on the bug's impact and available resources, 
the Ostro feature owner decides whether a hotfix is required in Ostro OS before the upstream project releases a fixed version. The
feature owner is also responsible for removing the hotfix when appropriate.

When submitting a new bug report (or feature request) to Ostro Project or an upstream project, verify 
that the issue has not been reported already to avoid duplication. 


Submitting Patches to the Ostro Project
=======================================

For general patches to upstream packages, we recommend you submit them directly to the
appropriate upstream project home. For patches specific to the Ostro OS, submit them as a 
git pull request (PR) so project maintainers can review and merge them. In this section we'll 
explain how to properly format and submit your patch.

In a collaborative open source environment, standards and methods for submitting changes 
help reduce chaos that can result from an active development community. One general practice 
is to make small, controlled changes. This practice simplifies review, makes merging and 
rebasing easier, and keeps the change history clear and clean.

The Ostro OS is based on Yocto Project layers that are put together using the combo-layer script.
The http://github.com/ostroproject/ostro-os repository is a combination of several components in a 
single repository and contains everything needed to build Ostro OS, including: bitbake, openembedded-core,
meta-intel, meta-ostro, meta-ioc, meta-swupd, and more.

.. _`meta-ostro README`: https://github.com/ostroproject/meta-ostro/blob/master/README.rst

See the `meta-ostro README`_ for a complete and up-to-date list on the GitHub repo.

The top-level directory comes from openembedded-core and meta-ostro, everything else is in its own
sub-directory. The ostro-os repository gets updated by importing commits from the individual 
component repositories. 

For more information about each of these components including the URL,
branch and current revision used, please refer to the ``conf/combo-layer.conf``
file in your cloned copy of the top-level ``ostro-os`` repository.

When you initially clone the repository, you clone the aggregation resulting from that script. 
While developing a fix, it can be very convenient to work in this aggregated repository, particularly
when patches are needed against different components. 

Patches may not be submitted against this aggregated repository; send those to the original layer and
don't mix changes against different components in one PR.

To begin then, you’ll need to identify which layer needs to be modified.

In this example, we assume you’re familiar with Git, GitHub, and the basic Linux development process. For convenience,
we'll use both the http://github.com/ostroproject web interface and Git command line tools.

Upstream project code is not stored in the Ostro Project's Git tree. Instead, 
there are Yocto Project recipes that reference upstream source and, as needed, hotfix patches for 
issues that have not been incorporated upstream. 

We’ll assume in the following steps that you’ll be modifying the ``meta-ostro`` layer.

If you haven't already done so, you'll need to create a (free) GitHub account on http://github.com and have
Git tools available on your development system.  (For Windows users you can use `Git Bash`_ or other Git command line tools.)

.. _`Git Bash`: https://git-for-windows.github.io/

Prepare your patch
------------------

.. _`Fork a Repo`: https://help.github.com/articles/fork-a-repo/
.. _`Yocto Project Managing Layers`: http://www.yoctoproject.org/docs/current/dev-manual/dev-manual.html#managing-layers

#. Create a Fork (using GitHub's web interface)
   In GitHub, create a fork of the repo containing the layer you need to modify. In this example we use ``meta-ostro``. 
   For more information, see GitHub's `Fork a Repo`_ help page.

   In your web browser, navigate to the repo: https://github.com/ostroproject/meta-ostro and click on the Fork button
   in the top right corner to fork your own copy of the ``ostroproject/meta-ostro`` repo to your account.

#. Create a repository on your local computer to your fork.  If you have ssh keys generated you can register your 
   public key on your GitHub account (SSH and GPG keys in your Personal Settings on Git Hub) to be authorized.  
   Otherwise, you can clone with "https" and specify your GitHub username and password:::
 
      $ git clone github.com:<your-username>/meta-ostro                # if you've registered your ssh key
      $ git clone https://github.com/<your-username>/meta-ostro.git    # if not use this (and your GitHub username/password)

      $ cd meta-ostro

      $ git remote add upstream github.com:ostroproject/meta-ostro            # if you've registered your ssh key
      $ git remote add upstream https://github.com/ostroproject/meta-ostro    # if you cloned with https

      $ git remote -v        # verify origin (your fork) and remote (Ostro OS master) are defined as expected

#. Create a new branch to work on your patch:::

      $ git fetch upstream
      $ git checkout -b my-patched-branch upstream/master

#. Make and test your changes
   After making your edits or adding files, this typically involves building a new image that contains your changes. 

   To replace the current layer with the one you are working on, modify your <builddir>/conf/bblayers.conf file as appropriate
   or use the Yocto Project tools ``bitbake-layers`` command instead of manually editing the ``bblayers.conf`` file (from
   within your local cloned copy of ``ostro-os``::

      $ bitbake-layers show-layers          # add-layer, remove-layer are other options...

   See the `Yocto Project Managing Layers`_ documentation for more usage details.

   When ready, run bitbake to start the build:::

      $ bitbake -k ostro-image-noswupd        # for example, other target images are available too

#. Commit your changes and rebase onto master
   After you’ve tested and verified your change does what was intended, you can commit your change locally. 
   Make sure that you follow the `Code Review Process Guidelines`_ described earlier in this document:::

      $ git commit -a -s                    # follow guidelines for the commit message
      $ git push origin my-patch-branch     # push your local branch up to your forked GitHub repo

   Depending on how long you have worked on your patch, it may be that the master branch has evolved since you branched 
   it off. If that is the case, you should rebase your working branch onto master before sending the Pull Request (PR):::


      $ git rebase upstream/master

#. Create a Pull Request (PR)
   Once your change is in your forked version (up on GitHub), use your web browser to submit your PR:

     * Navigate to your branch: https://github.com/<username>/meta-ostro/tree/my-patched-branch (the branch name you
       created earlier).
     * Click on "Compare & pull request" button From there you can see your changes and create a Pull Request (PR) to the 
       master branch for that component.


7. Respond to Pull Request (PR) Comments
   You may be asked to update or re-work your patch as part of the review process. 
   The easiest way to keep the discussion going in the same Pull Request is to force-push a revised commit to your 
   forked repository. GitHub will automatically update the Pull Request with the latest changes.  Using amended
   commits is preferred over a PR with multiple commits and helps make reviewing the cumulative changes much easier:::


      $ git commit --amend
      $ git push -f origin my-patched-branch      # force the push back to your forked copy on GitHub

   Be sure to add a comment to your amended commit message saying what was changed and that this update was forced-pushed, 
   otherwise reviewers will not get notification about the change.  
   Once the reviewers and maintainers accept your changes, they will be merged and incorporated in the Ostro OS 
   next time the maintainers run the combo-layer script. 

Once your changes have been merged, you can clean your local branches and go back to using the layer that is part of 
the Ostro project and revert the changes you (preferred) made in <builddir>/conf/bblayers.conf using the Yocto Project tools 
``bitbake-layers`` command (preferred) or manually editing the ``bblayers.conf`` file.
)

