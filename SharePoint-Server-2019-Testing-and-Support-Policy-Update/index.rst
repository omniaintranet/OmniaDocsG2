SharePoint Server 2019 – End of Support and Omnia Testing Policy Update
=========================================================================

Microsoft has announced that SharePoint Server 2019 will reach end of extended support on **July 14 2026**, in accordance with the Microsoft Fixed Lifecycle Policy.

Microsoft references:

- `SharePoint Server 2019 lifecycle information <https://learn.microsoft.com/lifecycle/products/sharepoint-server-2019>`_
- `Microsoft Fixed Lifecycle Policy <https://learn.microsoft.com/lifecycle/policies/fixed>`_

In alignment with Microsoft’s lifecycle policy and support timelines, Omnia is updating its platform testing and compatibility policy for Omnia on-prem products.

Change in Omnia Testing Scope
-----------------------------

Starting from **Omnia On-Prem version 7.10**, Omnia will **no longer be tested on SharePoint Server 2019**.

From this version onward:

- SharePoint Server 2019 will be removed from our official test matrix.
- No ongoing validation, regression testing, or certification will be performed on SharePoint 2019.
- New features and updates will be verified exclusively against **SharePoint Server Subscription Edition (SE)**.


Impact for Existing Customers
-----------------------------

- Omnia versions released prior to version 7.10 will retain their documented compatibility with SharePoint Server 2019.
- After version 7.10, SharePoint 2019 compatibility will no longer be validated or guaranteed.
- Customers running SharePoint 2019 are advised to plan their upgrade to SharePoint Server Subscription Edition (SE) before Microsoft’s end of extended support date (**July 14, 2026**).

Running business-critical solutions on a platform that has reached end of support may result in:

- Lack of security updates from Microsoft
- Increased operational and compliance risks
- Limited ability to receive vendor support

Recommendation
--------------

To ensure continued supportability, security updates, and full compatibility with future Omnia releases, we recommend upgrading to **SharePoint Server Subscription Edition (SE)** in accordance with Microsoft’s lifecycle guidance.