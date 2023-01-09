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

### Handling these Errors within Cyclr

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

### Example Transaction Error Webhook Payload

The information in the **Detail** property will contain the Response that was received.

This means it will change dependant on the API being called and how it formats its error Responses.  

If there are specific errors you wish to handle, you may need to force them to occur so that you can view the Response to see how that appears.
```json
{
    "Timestamp": "2019-08-08T11:25:34.0412055Z",
    "AccountId": "a2b35322-c966-4a29-95d7-065aaf12b127",
    "AccountExternalId": "account-id-in-your-application",
    "CycleId": "15643129-a29d-4957-865c-0495099fbbec",
    "StepId": "519713ff-57cf-49ef-9c00-f3a3e1569268",
    "TransactionId": "1564aae4-b82e-4712-a078-30a4e53c40d0",
    "Message": "Failed to call the method",
    "Detail": "404 Item not found\r\n{\"Code\":200,\"Message\":\"Item not found\"}\r\n\r\n\r\nHTTP Request:\r\nGET https://someapi.com/getitems/myID/ HTTP/1.1\r\nAccept: application/json\r\nApiKey:\r\nUser-Agent: Cyclr\r\nUser-Agent: (https://cyclr.com)"
}
```

</section>
