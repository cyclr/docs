---
title: Handle transaction errors
sidebar: cyclr_sidebar
permalink: transaction-error-webhook
tags: [cyclr-config]
menus:
    cyclr-configuration:
        title: Handle transaction errors
        identifier: transaction-error-webhook
        toggleonly: menutoggleonly
        weight: 8
---
{::options parse_block_html="true" /}
<section class="card">
Cyclr can be configured to make an HTTP Request if an error occurs in a running Cycle as a way of alerting you or your support staff.

This is performed as an HTTP POST Request to a URL you specify and contains JSON structured data in its Request Body..

The URL could be for an external system, or for a Webhook Step in a Template or Cycle within your Cyclr Partner, allowing you to process the data using Decision Steps, etc as you would any other data in Cyclr.  You could install a **Slack** or **SendGrid** Connector as a way to alert you and perhaps one of the database Connectors to log the data as well.

If you choose to use a Template or Cycle for this, you should install the **Error Webhook** Connector which knows the structure of the Request Body so is simpler to setup than using a standard **Generic Webhook** Connector's **Webhook** Method.

</section>
<section class="card">

## Handling these Errors within Cyclr

1. We'd recommend creating a separate Folder perhaps called "Monitoring" to put your Template or Cycle into.  It's up to you whether you do this in your Cyclr Console as a Template or create a new Account dedicated to these sorts of tasks.
2. Install the **Error Webhook** Connector - it has a **Webhook** Method which knows the structure of Cyclr's error Requests.
3. Add that Connector's Webhook Step to your Cycle.
4. In the Webhook's Step Setup, copy the `Webhook URL`.
5. Go to your Cyclr Console, and select `Settings` > `General Settings`.
6. Tick the box for `Enable Transaction Error Webhook`
7. Paste in the URL you copied in Step 4.
8. Click Save.

Now you can go back to the Cycle where you added the Webhook Step, and add any Decision Steps, etc to filter how errors will be handled.

In the example below, any errors relating to "Account 12345" will trigger a message in Slack.

![](/images/triggerslackfromerror.png)

### Account-level Override

If you wish, you can choose to handle errors in particular Cyclr Accounts differently by using the Account-level override.

In your Cyclr Console, go to the Accounts menu then Account Management, click Settings for the Account you wish to set this for and use the **Transaction Error Webhook** options.

</section>
<section class="card">

## Example Transaction Error Webhook Payload

The information in the **Detail** property will contain the Response that was received.

This means it will change dependant on the API being called and how it formats its error Responses.  

If there are specific errors you wish to handle, you may need to force them to occur so that you can view the Response to see how that appears.
```json
{
    "Timestamp": "2023-04-11T07:37:47.455544Z",
    "AccountId": "0bd9f087-8db9-46e9-8640-e8eb8a6fd635",
    "AccountExternalId": "0bd9f087-8db9-46e9-8640-e8eb8a6fd635",
    "AccountName": "Templates",
    "CycleId": "a2115f94-4ee6-4c4b-a03c-f89ce5ec41ed",
    "CycleName": "SF Updated Opps to Google",
    "StepId": "5c881e9f-5a38-4544-9b36-562baf4a2e71",
    "StepName": "Get Account",
    "StepType": 1,
    "TransactionId": "284bc7b4-4321-4c97-aa2f-370f9627d244",
    "Message": "Failed to call the method",
    "Detail": "404 Not Found\r\n[{\"errorCode\":\"NOT_FOUND\",\"message\":\"Provided external ID field does not exist or is not accessible: AAA\"}]\r\n\r\n\r\nHTTP Request:\r\nGET https://dw0000000ljgkeaa-dev-ed.my.salesforce.com/services/data/v43.0/sobjects/Account/AAA?fields=Name HTTP/1.1\r\nAccept: application/json\r\nAuthorization: REDACTED\r\nUser-Agent: Cyclr, (https://cyclr.com)",
    "IncidentLevel": "Error"
}

```

</section>
