.. _doc_guidelines:

Ostro |trade| Project Documentation Guidelines
##############################################

Ostro Project content is written using the `reStructuredText`_ markup language (.rst file extension)
with sphinx extensions, and processed using sphinx to create a formatted
standalone website.  Developers can view this content either in its raw form
as .rst markup files, or (with sphinx installed) they can run the makefile to generate
the HTML content and view it with a web browser directly
from their workstation's drive.
This same .rst content is also fed into the Ostro Project's public website documentation
area (with a different theme applied).

You can read details about `reStructuredText`_
and about `Sphinx extensions`_ from their respective websites.

.. _Sphinx extensions: http://www.sphinx-doc.org/en/stable/contents.html
.. _reStructuredText: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
.. _Sphinx Inline Markup:  http://sphinx-doc.org/markup/inline.html#inline-markup

Folder structure
================

top-level doc directory
    index.rst "main page"

howtos_
    Articles explaining how to do certain tasks covering
    development on (or for) Ostro OS as well as using and contributing to it.

architecture_
    Technical Architecture information about the Ostro OS and its components

quick_start_
    Getting Started Guide and associated subtopics for setting up Ostro OS development

sphinx_build
    Sphinx configuration and build files for the Ostro Project's website.  When processed, 
    HTML output is contained within this folder in the _build/html folder.


.. _howtos: howtos
.. _architecture: architecture
.. _quick_start: quick_start


Headings
========

For consistency, please use just an underline indicator for headings (not both over- and under lines).

* For the document title (h1) use "#" for the underline character
* for the first section heading level (h2) use "="
* for the second section heading level (h3) use "-"
* and for the third section heading level (h4) use "^"

Remember that the underline must be at least as long as the title it's under.


Markup samples
==============

Some common reST inline markup samples:

* one asterisk: ``*text*`` for emphasis (*italics*),
* two asterisks: ``**text**`` for strong emphasis (**boldface**), and
* backquotes: ````text```` for inline code samples.

List markup is natural: just place an asterisk at
the start of a paragraph and indent properly for continuation lines.  For numbered lists
start with a 1. or a. for example, and continue with autonumbered bu using a ``#`` sign::

   * This is a bulleted list.
   * It has two items, the second
     item uses two lines.

   1. This is a numbered list.
   2. It has two items too.

   a. This is a numbered list using alphabetic list headings
   #. It has three items (and uses autonumbering for the rest of the list)
   #. Here's the third item


If asterisks or backquotes appear in running text and could be confused with
inline markup delimiters, they must be escaped with a backslash ("\\")

Sphinx Inline Markup
====================

Sphinx supports a large number of inline markup elements used to tag text with special
meanings and output formatting. (You can refer to the `Sphinx Inline Markup`_
documentation for the full list).   Here are some of the more useful markup notations
for our use:

* Use the 'command' markup when the name of a specific command is
  used as part of a paragraph for emphasis. Use the ``.. code-block::``
  directive to supply full actionable commands as part as a series of
  steps.

   :command:`make`

   ``:command:`command```

* Use the 'file' markup to emphasize a filename or directory. Do not
  use the markup inside a code-block but use it inside all notices that
  contain files or directories.

   :file:`collaboration.rst` :file:`doc/collaboration/figures`

   ``:file:`filename.ext` :file:`path/or/directory```


Internal Cross-Reference Linking
================================

Normal ReST linking is only supported within the current file. With Sphinx however, we can create 
and link to references anywhere within the Ostro Project documentation.  The only requirement is that 
these reference labels must be unique.  Each file should have a reference label before its title so it may
be referenced from another file.  For example:


.. code-block:: rst

   .. _label_of_target:

   This Is a Heading
   -----------------

   This creates a link to the :ref:`label_of_target` using the text of the
   heading.

   This creates a link to the :ref:`target <label_of_target>` using the word
   'target' instead of the original heading.

The template renders as:

.. _label_of_target:

This Is a Heading
-----------------

This creates a link to the :ref:`label_of_target` using the text of the
heading.

This creates a link to the :ref:`target <label_of_target>` using the word
'target' instead of the original heading.

.. important::

   This type of internal cross reference works across multiple files, is
   independent of changes in the text of the headings and works on all
   Sphinx builders that support cross references.



Non-ASCII Characters
====================

For inserting non-ASCII characters such as a Trademark symbol, use the notation ``|trade|``.
These replacement names are defined in an include file used during the sphinx processing
of the reST files.  The names of these replacement characters are the same as used in HTML
entities used to insert characters in html, e.g., \&trade; and are defined in the
file ``substitutions.txt``
