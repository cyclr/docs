---
title: Sage Intacct Authentication
sidebar: cyclr_sidebar
permalink: sage-intacct-connector
tags: [connector]

---
{::options parse_block_html="true" /}
<section class="card">
## Sage Intacct setup
To authenticate the connector you need the following credentials:

| **Credential** | **Description** |
| ----------- | ----------- |
| **Web Services ID** and **Web Services Password**  |  Sage Intacct provides a Web Services sender ID and password for customers/partners with an active Web Services developer license. These credentials are not necessarily tied to a particular Sage Intacct company/user, so a Marketplace Partner can use a sender ID for any Sage Intacct company that has authorized that sender ID for Web Services.     |
| **Company Login ID** and **Company Login Password** | The user ID and password to log in to your/your company's Sage Intacct account.   |
| **Company ID** | The ID that you want to use to authenticate the user ID and password.       |
| **Location ID**  | **Optional**: Add a location ID to log in to a multi-entity shared company. Entities are typically different locations of a single company.  |

You can use a **Client ID** to log in to a distributed child company. The **Company Login ID** and **Company Login Password** access the console, not the target client company itself. To provide this, fill in the Company ID field with the following format: `myConsoleId|clientCompanyId|entityId`.

For more information on how to obtain these values, contact your Sage Intacct account manager.


</section>
<section class="card">
## Cyclr setup

To set up the Sage Intacct connector in Cyclr:

1. Go to your **Cyclr Console**.

2. Select **Connectors** > **Application Connector Library** at the top of the page.

3. Use the search box to find the **Sage Intacct** connector.

4. Select the **Setup Required** icon.

5. Enter the your **Web Services ID**, **Web Services Password**, **Company Login ID**, **Company Login Password** and **Company ID**. 

  *   Optionally, enter your **Location ID** if you log in to a multi-entity shared company. 

7. Select **Save Changes**.

>  **Note**: To use different settings for different accounts, leave the value blank. This means Cyclr asks for the value when you install the connector into an account.

</section>
