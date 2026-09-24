Controlled-document library
===========================

Controlled documents live in a controlled-document library on the site of a Teamwork app. The library is a feature of that Teamwork app, and the connector can activate it once the app's site exists.

.. TODO screenshot: a controlled-document library on a Teamwork app site, for reference

What you can ask for
********************

+ Activate the controlled-document library on a Teamwork app.
+ Check whether the activation has finished.

Example
*******

The library is activated on a Teamwork app you have already created - see :doc:`../teamwork-app/index`:

::

   Activate the controlled-document library on the Quality Management team app

.. TODO screenshot: Claude reporting that activation is in progress

Activation takes a while. The first answer is usually that it is **in progress**, together with the site it is being activated on. Ask again to follow it:

::

   Check whether the controlled-document library on Quality Management is activated yet

Once it reports **activated**, the library is ready to receive controlled documents.

.. TODO screenshot: the activated controlled-document library in the Omnia interface

Good to know
************

+ Activating the library needs a **business profile** scope. The connector does not work around Omnia's permission model - without the right to activate features on the Teamwork app you get Omnia's own refusal.
+ The Teamwork app's **site must exist first**. Straight after a Teamwork app is created its site is still being provisioned, and activation is refused until it is there - wait a moment and ask again.
+ Asking again is safe. Activating a library that is already active, or already being activated, changes nothing and simply reports where it stands.
+ If activation fails, the reason Omnia gives is passed back to you.
+ Deactivating the library is not supported through the connector.

Actions
*******

+ ``ControlledDocumentLibrary.Activate`` - activate the controlled-document library on a Teamwork app, or check how far the activation has come.
