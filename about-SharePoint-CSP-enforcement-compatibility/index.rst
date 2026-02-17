About SharePoint CSP enforcement compatibility
=================================================

Microsoft is making changes to the way scripts are allowed to be loaded from SharePoint framework, a technology used to integrate 3rd-party components into SharePoint Online.

These changes also affects Omnia, when loaded within a SharePoint page, after **March 1 2026**.

Actions needed
****************
1. Verify that Omnia is updated to version 7.9.28 or later.
2. Generate a new SPFx package. Follow the instructions found in Tenant > System > Microsoft 365 > SPFx Instruction.
3. Upload the SPFx package to the SharePoint add-in catalog site and make sure it is deployed.
4. Test that everything works, by loading a SharePoint page with Omnia components and appending ?csp=enforce to the query string.

Need more time?
******************
You can post-pone the enforcement of the stricter script-loading rules until June 1 2026. To do so, run the following PowerShell command as a SharePoint Administrator: Set-SPOTenant -DelayContentSecurityPolicyEnforcement $true
 
Need assistance?
*******************
If you need assistance, reach out to your Customer Success Team or post a support ticket. 
