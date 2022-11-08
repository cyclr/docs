---
title: Zoho
sidebar: cyclr_sidebar
permalink: zoho
tags: [connector]

---

## Partner Setup ##

This document explains how to setup access to Zoho and to install the Zoho CRM Connector.

### OAuth Setup ###

You'll need to register your Cyclr Partner with Zoho by creating a "Client" in your [Zoho API Console](https://accounts.zoho.com/developerconsole).

[Zoho's own documentation on this can be found here](https://www.zoho.com/accounts/protocol/oauth-setup.html)


* When asked which **Client Type** you wish to create, choose "Server-based Application".

![](./images/Zoho_ClientType.png)

<br/>

* Enter an **Authorized Redirect URI** using this format:

{% raw %}`https://{{Your Cyclr Service Domain}}/connector/callback`{% endraw %}

e.g. ```https://app-h.cyclr.com/connector/callback```

You can find your **Service Domain** within your Cyclr Console from the **Settings** menu then **General Settings**.

### Connector Setup ###

Once you have your Client ID and Client Secret from Zoho, go to your Cyclr Console then Connectors > Application Connector Library, search for **Zoho CRM**, click the Padlock button next to it and set them so they're used every time when installing the Connector.

## Scopes

The scopes are defaulted to "ZohoCRM.modules.ALL,ZohoCRM.users.ALL,ZohoCRM.org.ALL,ZohoCRM.settings.roles.ALL", however you can enter your own scopes if you wish to restrict the connectors access further.

See Zoho's documentation [here](https://www.zoho.com/crm/developer/docs/api/v2/scopes.html) on available scopes.



## Domain property

When installing a **Zoho CRM** Connector, use the domain part of the URL shown in the web browser when signed into the Zoho CRM account.

If working with a Zoho CRM Plus subscription, the Domain should be in the format ```https://crm.zoho.com``` as normal, and not ```https://crmplus.zoho.com```.



## Additional Information

## List New/Updated Contacts By Page (Incrementally)

### In order to use this method follow these steps to setup your cycle: 

1. Edit your **Generic Webhook** connector and add a custom field named `page`.

2. Design a new cycle named **Zoho Incremental method** , use a **Generic Webhook** connect it to the **List New/Updated Contacts By Page (Incrementally)** method. 

3. In the Step settings of your **Generic Webhook**, click **Advanced Settings**

   ```javascript
    function after_webhook() {   
        cyclr_storage_set('pageNumber', method_response.page);
       return true;
   }
   ```

3. In the Step settings of **List New/Updated Contacts By Page (Incrementally)** map the page to the webhook `page` field. 

4. Connect the true exit **List New/Updated Contacts By Page (Incrementally)** to a **Decision** step which checks whether the **More Records?** field equals a **true** value.

5. Connect the false exit **List New/Updated Contacts By Page (Incrementally)** to a **Set Last Successful Run Date**. 

6. Connect your **Decision** step true exit to a Delay step with the wait time set to **2 seconds**.

7. Connect a **Generic Webhook HTTP POST method** to the Delay step. Set the **URL** to the webhook **URL** and set the `page` field to ignore.

8. In the **Advanced Settings** of the **HTTP Post** Method add the following script:

   ```javascript
   function before_action() {
       method_request.page = (+cyclr_storage_get('pageNumber') + 1);
       return true;
   }
   ```


   ![zoho_incremental_cycle](https://github.com/cyclr/docs/tree/master/images/zoho_incremental_cycle.png)

8. Connect the **Decision** step false exit to the **Set Last Successful Run Date** method located in the **Utilities** category.
9. Connect the **Decision** step true exit to a Delay
10. Create a Second Cycle Named **Zoho Incremental Method Start**. 
11. Connect **Generic Webhook HTTP Post method** to the **List Contacts** method located in the **Contacts** Category of the zoho connector.
    ![zoho_start](https://github.com/cyclr/docs/tree/master/images/zoho_start.png)
12. Run the  **Zoho Incremental Method** cycle, then Run the **Zoho Incremental Method Start**. 
