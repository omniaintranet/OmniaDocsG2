Review and approval
===================

A controlled document can go through two kinds of workflow before and during publishing. A **review** asks one or more colleagues to read a draft and complete a review task. An **approval** is what a draft goes through when it is published with approval: the approver approves or rejects it, and an approved draft is published. The connector can start and manage reviews, and approve, reject or cancel approvals.

.. TODO screenshot: an approval task for a controlled document in Omnia, for reference

What you can ask for
********************

+ List the approval and review tasks assigned to you on a controlled-document site.
+ Read the details of an approval task or a review task.
+ Approve or reject a pending approval.
+ Cancel a running approval workflow.
+ Send a draft to review, add a reviewer, forward a review to someone else, or remove a reviewer.
+ Complete a review task, or cancel the whole review.

Approving and rejecting
***********************

Start from the list of tasks waiting for you:

::

   What approval tasks are waiting for me on https://contoso.sharepoint.com/sites/qms?

The connector always lists the tasks first and lets you pick one - it never guesses which task you mean. You then see the task's details: the document, the due date and any comments from the workflow.

::

   Approve the task for "Fire Safety Procedure", comment "Looks good"

::

   Reject it - the safety section is incomplete

You are asked whether you want to approve or reject, and whether to add a comment, unless you already said so. The task, the outcome and the comment are summarised back to you, and nothing is written until you confirm.

**Approving publishes the document.** Approval finishes the workflow in the same way as approving in Omnia, so the new edition is published (or scheduled) as part of it. Rejecting finishes the workflow without publishing.

.. TODO screenshot: Claude summarising an approval before it is confirmed

Cancelling an approval
**********************

::

   Cancel the approval workflow that is running on "Fire Safety Procedure"

Cancelling stops the workflow, for example when a draft has to be changed before anyone approves it.

Reviews
*******

Sending a draft to review
-------------------------

::

   Send the draft of "Fire Safety Procedure" to review by anna@contoso.com and
   erik@contoso.com, due 10 October, with the instruction "Check section 3"

At least **one reviewer** is needed, given by e-mail address. A due date and instructions are optional. Afterwards the connector reads the new review task back and warns you if it was cancelled straight away.

Changing who reviews
--------------------

::

   Add maria@contoso.com as a reviewer on that review

::

   Forward my review task for "Fire Safety Procedure" to erik@contoso.com

::

   Remove the review task that was sent to anna@contoso.com

Adding a reviewer keeps the review running. Forwarding hands a task to someone else, optionally with a comment. Removing a reviewer removes only that task; if it was the last open task, the review is completed.

Completing and cancelling
-------------------------

::

   Complete my review task for "Fire Safety Procedure", comment "No remarks"

::

   Cancel the review of "Fire Safety Procedure"

Cancelling a review ends every open review task on the document.

Good to know
************

+ Tasks belong to a **controlled-document site**, so working with them needs the site address - not a business profile or Publishing App scope. For approving and rejecting, the site address has to match the task's own site exactly.
+ **Everything runs as you.** You can only act on tasks you are allowed to act on in Omnia.
+ Approving and rejecting check that the **controlled-document library** is activated on the site first.
+ A task that is **already completed or cancelled**, or whose draft has already been published or removed, cannot be approved or rejected. The connector refuses with an explanation instead of sending an incomplete task to Omnia.
+ Task ids come from the task list. They are never invented, so ask for the list if you do not have one.
+ **Approval comes before publishing.** When you ask to approve a document, the approval tasks are completed first, and the connector never publishes a document in place of an approval.
+ Sending to review, completing a review and cancelling a review each take **two steps** in Omnia. If the second step fails, you are told that the first one already happened - for example that the review task was created - so you know what state it is in.
+ A **reason** can be given when cancelling a review, but it is not stored yet.

Actions
*******

+ ``Document.ListTasks`` - the document tasks on a site, see :doc:`/mcp/examples/document-management/document/index`.
+ ``ApprovalTask.Get`` - read an approval task.
+ ``ApprovalTask.ApprovePending`` - approve a pending approval, which publishes the edition.
+ ``ApprovalTask.RejectPending`` - reject a pending approval.
+ ``ApprovalTask.Process`` - complete an approval task with an approved or rejected outcome.
+ ``ApprovalTask.CancelWorkflow`` - cancel a running approval workflow.
+ ``ReviewTask.Get`` - read a review task.
+ ``ReviewTask.SendToReview`` - send a draft to one or more reviewers.
+ ``ReviewTask.AddReviewer`` - add a reviewer to a running review.
+ ``ReviewTask.Forward`` - forward a review task to another reviewer.
+ ``ReviewTask.RemoveReviewer`` - remove one reviewer's task.
+ ``ReviewTask.Complete`` - complete a review task.
+ ``ReviewTask.CancelWorkflow`` - cancel the whole review.
