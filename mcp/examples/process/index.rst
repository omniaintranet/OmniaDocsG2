Process
=======

A process in Omnia Management System is a documented way of working - how to onboard a new employee, how to handle a customer complaint - built up as a tree of process steps and kept in a process library. The connector can list the processes you are allowed to read, look at one of them, and show you its steps.

What you can ask for
********************

+ List the published processes you can read.
+ Include your own drafts and checked-out processes in the list.
+ Narrow the list to one process library, or to processes whose title contains a word.
+ Look at one process - its version, who published it and when, its review date and its properties.
+ Show the steps of a process, as a tree.

Listing processes
*****************

::

   List the processes I can read

::

   Which processes have "onboarding" in the title?

Each process in the list comes with its title in your language, whether it is published or a draft, the process library it belongs to, who published it and when, who last changed it and when, and its review date if it has one. The process's properties are included as well - including the ones Management System keeps itself, such as the edition, revision and process type.

By default only **published** processes are listed. To see your work in progress as well, say so:

::

   List the processes I can read, including my drafts

A process that has both a published version and a draft then appears once for each.

.. TODO screenshot: Claude listing the processes the user can read

Looking at one process
**********************

::

   Show me the Employee onboarding process

You get the same information as in the list, plus the process's current working status - for example whether it has been sent for review or for approval - and a summary of its top step with the number of steps directly under it.

When a process has both a published version and a draft, the **published version** is the one shown. To look at the draft, ask for it from a list that includes drafts.

.. TODO screenshot: Claude showing the details of one process

Showing the steps
*****************

::

   Show me the steps of the Employee onboarding process

The steps come back in the order they are authored, top step first, each with its title, its level in the tree and its position among the steps next to it. A step that is a **link to another process** is marked as such, together with the process it points to.

.. TODO screenshot: Claude showing the step tree of a process

Good to know
************

+ Processes need no particular scope, only the tenant. Everything is **trimmed to what you are allowed to read** in Management System - a process in a library you cannot read is simply not in the list, and asking for it directly tells you it is not visible to you.
+ The list is the complete view of the processes you can read. :doc:`Search <../search/index>` only reaches processes that are in the search index, so a process can be missing from search results and still be in this list.
+ **Read only.** The connector cannot create, edit, publish or archive processes.
+ The steps show the **structure** of the process only - titles and how they are arranged. The content inside each step is not included.
+ **No link to the process is given.** Omnia builds a process's address from the page that hosts the Process Library block, and that page is not recorded on the process. If you know the address of that page, the process is at that address followed by ``/@pm/`` and the id of the process's top step, then ``/g``.
+ The **review date** is the one Management System set when the process was published, based on the review reminder of its process type. It is empty when no review is scheduled.

Actions
*******

+ ``Process.List`` - the processes you can read, published only unless drafts are asked for.
+ ``Process.Get`` - one process, with its working status and a summary of its top step.
+ ``Process.GetSteps`` - the full step tree of one process.
