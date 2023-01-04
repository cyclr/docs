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
<section class="card">
## Additional information

### Scopes

The scopes default to `ZohoCRM.modules.ALL,ZohoCRM.users.ALL,ZohoCRM.org.ALL,ZohoCRM.settings.roles.ALL`, but you can enter your own scopes if you want to restrict the connector's access further.

For more information, see Zoho's documentation on [available scopes](https://www.zoho.com/crm/developer/docs/api/v2/scopes.html).

### List New/Updated Contacts By Page (incrementally)

To use this method, follow these steps to set up your cycle: 

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

5. Connect the true exit of **List New/Updated Contacts By Page (Incrementally)** to a Decision step that checks whether the **More Records?** field in  **List New/Updated Contacts By Page (Incrementally)** equals a `true` value.  
   > **Note**: If you need to manipulate the data, Connect the true exit of the **List New/Updated Contacts By Page (Incrementally)** method to any other required methods before connecting to the **Decision** step.)_

6. Connect your Decision step true exit to a Delay step and set the wait time to `2 seconds`.

7. Connect a **Generic Webhook HTTP POST method** to the Delay step. Set the URL to the **Generic Webhook URL** and set the `page` field to **ignore**.

8. In the **Advanced Settings** of the **HTTP Post** method, add the following script:

   ```javascript
   function before_action() {
       method_request.page = (+cyclr_storage_get('pageNumber') + 1);
       return true;
   }
   ```

   ![The zoho incremental cycle.](./images/zoho_incremental_cycle.png)

9. Run the  **Zoho Incremental Method** cycle.

10. Send a **POST** request to your **Generic Webhook URL** with an API testing software, such as [Postman](https://www.postman.com/). The body of your request should as follows: 

    ```json
    {
    "page": 1
    }
    ```

    > **Note**: To update the last successful run date of your cycle please drag the the **Update Last Successful Run Date** Method located in the **Utilities**  Category onto your cycle and run the step. 

</section>
