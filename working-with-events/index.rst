Working with events
===========================

Using a number of options in Omnia, together with a few dedicated options, information can be published about different kinds of events (training sessions is one example) and event managers can handle registration of participants for the event.

Prerequisite: The tenant feature "Event management" must be active for any event options to be available.

**Note!** Event manager is not a separate permission, it's a term we use for the person that creates and manages an event. The permission an event manager needs is Editor, for the page where the event is managed.

Important event options that can be available:

+ Users can register to a participant list. The list keeps track of available seats.
+ Users can register to a standby list if all seats are taken.
+ Colleagues can be moved from the standby list to the participant list by an event manager.
+ Users can register a number of (not named) colleagues that will accompany them to the event.
+ A user can register for others.
+ Users can edit or remove their own registrations.
+ External users that has been invited in Entra ID, can use the event management options.
+ Event managers can create new events, can edit all registrations and remove registrations if needed.
+ Event managers can export the participant list to Excel and can communicate with participants through Email. (Work Email is used).
+ Event managers needs Editor permissions.

If event management is connected to an Outlook calendar, this additional option is used:

+ The participant list displays a status icon to indicate if the registered user has accepted the event in his or her calendar. 

**Note!** The service account used for event management can not be ADFS connected. If your organization uses ADFS, create and use a cloud-only account for this purpose instead.

**Note!** In Omnia on-prem, use personal Exchange calendars. Support for Exchange server 2016 and 2019.

**Note!** Events should not be used in combination with variations. If multiple variations of an event is created, each variation is treated as a separate event.

There's a number of settings available to decide how event Management will work. It can for example be set that a reservation list should not be available and that users should not be able to register for others.

There's two specific blocks available for event management (see the links below). In all other aspects, you use available options in Omnia for page types so event administrators can create pages with the information they want to display for the event.


.. toctree::
   :titlesonly:

   /setup/eventmanagement/index
   /blocks/blocks-event-management/index
   creating-new-event/index
   copy-event/index
   administer-event/index
   register-for-event/index
   implementation-example/index

