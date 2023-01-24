---
title: Zoho
sidebar: cyclr_sidebar
permalink: zoho
tags: [connector]


---
{::options parse_block_html="true" /}
<section class="card">
## Partner setup

This page explains how to setup access to Zoho so you can use the Zoho connector in Cyclr.

### OAuth Setup

To register your Cyclr Partner with Zoho, create a **Client** in your [Zoho API Console](https://accounts.zoho.com/developerconsole).

For more information, see [Zoho's documentation](https://www.zoho.com/accounts/protocol/oauth-setup.html).


1. When it asks which **Client Type** you want to create, select **Server-based Application**.

   ![A screenshot of the Client Type options.](./images/Zoho_ClientType.png)


2. Enter an **Authorized Redirect URL** with the following format:

   {% raw %}`https://{{Your Cyclr Service Domain}}/connector/callback`{% endraw %}

   For example, ```https://app-h.cyclr.com/connector/callback```.

> **Note**: You can find your **Service Domain** in your Cyclr console from the **Settings** menu then **General Settings**.


</section>
<section class="card">
## Cyclr setup

Once you have your Client ID and Client Secret from Zoho, go to your Cyclr Console:

1.  Go to **Connectors** > **Application Connector Library** and search for **Zoho CRM**. 
2.  Select the padlock icon next on **Zoho CRM**.
3.  Enter the Client ID and Client Secret to use these values every time you install the connector. For Information on obtaining your **Client Id** and **Client Secret** please refer to [Zoho's documentation on registering a client](https://www.zoho.com/accounts/protocol/oauth-setup.html).

> **Note**: If you leave these fields blank, Cyclr asks you to enter them when you install the connector into an account.

### Domain property

When you install the **Zoho CRM** connector, use the domain part of the URL that shows in the web browser when you are signed into the Zoho CRM account.

If you have a Zoho CRM Plus subscription, use the normal domain format `https://crm.zoho.com` instead of `https://crmplus.zoho.com`.



</section>
