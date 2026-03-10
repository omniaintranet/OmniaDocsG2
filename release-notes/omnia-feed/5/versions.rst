5.1.0
========================================

- Fixed an issue where images with large size sometime cannot  be displayed (#125486).
- Added missing Danish localization for some admin settings (#125102).
- Fixed several issues where users cannot access an business profile in Omnia Feed because of unauthorized error (#124324, #123881, #124146, #123961, #125257, #124718). IMPORTANT: For this fix to work, it is required to give consent to the Omnia app again.
- Replacing images in news articles are now working correctly in Omnia Feed (#123589).
- Improved performance and stability.

5.2.16
========================================

- Images added after the news articles have been synced to Omnia Feed now shown correctly.
- Fixed an session expired issue when switching business profile after leaving the app idle for 30 minutes.
- Fixed the issue that the app sometime crashes when signing out.
- Removed the option to query based on "Current page".
- When signing in to Omnia Feed with incorrect domain, the error message "Organization not found" will now be displayed until the next sign in attempt, instead of disappearing after 3 seconds. 
- Small UI fix for the highlight of articles with new comments.
- Improved UX by show an indicator while images are being loaded.
- Fixed the link to Privacy Policy.
- Fixed an issue on iOS when the cursor on the textbox for login form always jump to the beginning when text is too long.


5.2.19
========================================
- Fixed an issue where some users with specific domains cannot login to Omnia Feed.
- Omnia Feed now works correctly with Microsoft Authenticator on Android.
- Fixed UI glitch in the header for some iOS devices.

5.2.20
========================================
- Fixed the issue with news targeting does not work correctly when page has a variation with only draft version. (#126481)
- Improved the stability of the API for resolving page collection from URL in Omnia Feed settings.
