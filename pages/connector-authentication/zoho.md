---
title: Zoho
sidebar: cyclr_sidebar
permalink: zoho
tags: [connector]

---

## Partner setup

This page explains how to setup access to Zoho so you can use the Zoho connector in Cyclr.

### OAuth Setup

You need to register your Cyclr Partner with Zoho by creating a **Client** in your [Zoho API Console](https://accounts.zoho.com/developerconsole).

Zoho's documentation on this can be found [here](https://www.zoho.com/accounts/protocol/oauth-setup.html).


1.  When asked which **Client Type** you want to create, select **Server-based Application**.

![A screenshot of the Client Type options.](./images/Zoho_ClientType.png)


2.  Enter an **Authorized Redirect URL** with the following format:

{% raw %}`https://{{Your Cyclr Service Domain}}/connector/callback`{% endraw %}

For example, ```https://app-h.cyclr.com/connector/callback```

> **Note**: You can find your **Service Domain** in your Cyclr console from the **Settings** menu then **General Settings**.

## Cyclr setup

### Account setup

Once you have your Client ID and Client Secret from Zoho, go to your Cyclr Console > **Connectors** > **Application Connector Library** and search for **Zoho CRM**. Select the padlock icon next to it to use these values every time you install the connector.

## Additional Information

### Scopes

The scopes are defaulted to "ZohoCRM.modules.ALL,ZohoCRM.users.ALL,ZohoCRM.org.ALL,ZohoCRM.settings.roles.ALL", however you can enter your own scopes if you wish to restrict the connectors access further.

See Zoho's documentation [here](https://www.zoho.com/crm/developer/docs/api/v2/scopes.html) on available scopes.

### Domain property

When installing a **Zoho CRM** Connector, use the domain part of the URL shown in the web browser when signed into the Zoho CRM account.

If working with a Zoho CRM Plus subscription, the Domain should be in the format ```https://crm.zoho.com``` as normal, and not ```https://crmplus.zoho.com```.

### List New/Updated Contacts By Page (incrementally)

To use this method, follow these steps to setup your cycle: 

1. Edit your **Generic Webhook** connector and add a custom field named `page`.

2. Create a new cycle named **Zoho Incremental method**, and use a **Generic Webhook** to connect it to the **List New/Updated Contacts By Page (Incrementally)** method. 

3. In the step settings of your **Generic Webhook**, select **Advanced Settings** and enter the following script.

   ```javascript
    function after_webhook() {   
        cyclr_storage_set('pageNumber', method_response.page);
       return true;
   }
   ```

4. In the step settings of **List New/Updated Contacts By Page (Incrementally)**, map the page to the **Generic Webhook** `page` field. 

5. Connect the true exit of **List New/Updated Contacts By Page (Incrementally)** to a **Decision** step that checks whether the **More Records?** field equals a **true** value.

6. Connect the false exit of **List New/Updated Contacts By Page (Incrementally)** to a **Set Last Successful Run Date**. 

7. Connect your **Decision** step true exit to a Delay step and set the wait time set to **2 seconds**.

8. Connect a **Generic Webhook HTTP POST method** to the Delay step. Set the **URL** to the **Generic Webhook URL** and set the `page` field to **ignore**.

9. In the **Advanced Settings** of the **HTTP Post** method, add the following script:

   ```javascript
   function before_action() {
       method_request.page = (+cyclr_storage_get('pageNumber') + 1);
       return true;
   }
   ```

   ![The zoho incremental cycle.](./images/zoho_incremental_cycle.png)

10. Connect the **Decision** step false exit to the **Set Last Successful Run Date** method from the **Utilities** category.

11. Create a Second Cycle and name it **Zoho Incremental Method Start**. 

12. Connect the **Generic Webhook HTTP Post method** step to the **List Contacts** method from in the **Contacts** category of the zoho connector.
    ![The zoho start cycle.](./images/zoho_start.png)

13. Run the  **Zoho Incremental Method** cycle, then run the **Zoho Incremental Method Start**. 
