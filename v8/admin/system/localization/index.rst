Localization
=====================================

The localization editor is used to view translations of different labels in different languages, edit these translations, and export the translated labels.

For translation, or simply editing, of Email messages from Omnia, see this page for more information: :doc:`Tokens in Omnia Emails </admin-settings/tenant-settings/system/tokens-in-emails/index>`

Selecting FILTER you can decide what is displayed in the list and what you will work with:

.. image:: localization-view-mode-v8.png

View mode
************
Choose to display all or some:

.. image:: localization-view-mode-menu-v8.png

+ **All**: No surprise here, show all within the selected service.
+ **Has been customized**: Lists all labels that has been edited directly here, without export. For more information, see below.
+ **have update**: Lists all labels that have been updated.
+ **Have missing translation**: In order to view the labels that have yet not been translated, select this option.

Omnia service
***************
Here you can select the part of omnia that you would like to view the labels of. If the purpose is translating labels, then each part needs to be translated, since each part has different labels

.. image:: localization-service-v8.png

**Note!** If the name of the service ends with "worker", it must not be translated.

Language
************
Select language for the output here, from the available tenant languages. 

.. image:: localization-language-v8.png

If the purpose is translating untranslated labels, it can be useful to create output for both English (United states), that is the base language for Omnia, and the language you wish to translate to. You can then always check existing translations and see the labels in the base language.

Available languages are set up under Tenant-Settings-Regional settings, see: :doc:`Regional settings </admin-settings/tenant-settings/settings/index>`

Export
***********
When you have selected settings, click EXPORT to export the lis to a file.

The texts that needs to be translated are now exported to a json file. The file is placed in the Downloads folder on your computer.

Just correcting a few translations
************************************
If you only need to correct one, or a few, translations, you don't need to download the file/files. You can then simply change the translation directly here. 

**important note!** This method is what is called "Has been customized" in the View mode selector. Changes you make this way are NOT overwritten if you import a translated JSON file to the system, which also means changes that the Omnia translation staff do is not implemented for these labels/messages.

Don't forget to save when you're done.

