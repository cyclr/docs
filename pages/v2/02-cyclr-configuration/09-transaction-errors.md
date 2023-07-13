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
        weight: 9
---
{::options parse_block_html="true" /}
<section class="card">

## Set up alerts

You can configure Cyclr to make an HTTP request to alert your or your support staff if an error occurs in a running cyclr.

Cyclr performs this alert as an HTTP `POST` request with JSON structured data in the request body. You can specify the URL Cyclr sends the request to.

You can use a URL for an external system, or the URL of a webhook step in cycle in your Cyclr account. 


## Handle the errors in Cyclr

If you send the HTTP request to a Cyclr webhook URL, you can use Cyclr tools, such as decision steps, to process the data. You can also use other connectors. For example, you can install a **Slack** connector to send an alert message, or a database connector to log data.

To make the process easier if you want to use a cycle, you can use the **Error Webhook** connector since it’s set up according to the structure of the error data in the request body.

To set up a cycle to handle errors, you need the webhook URL:

1. Create a new template. 
2. Install the **Error Webhook** connector
3. Add the **Webhook** step to your cycle.
4. Select **Step Setup** and copy the **Webhook URL**.
5. In the console, go to **Settings** > **General Settings**.
6. Select the **Enable Transaction Error Webhook** toggle, paste the webhook URL into the field, and select **Save**.
7. Go back to the template and define the rest of the cycle according to what you want to do with the error data.

### Example

For example, in the cycle below, any errors that relate to `Account 12345` trigger a message in Slack:

![A screenshot of a webhook cycle that triggers a Slack message.](/images/triggerslackfromerror.png)

</section>
<section class="card">

## Handle errors in specific accounts

You can handle errors differently in specific accounts since the account level settings override the general console settings.

To configure how a specific account handles transaction errors, go to **Accounts** > **Account Management**, and select the account’s **Settings** icon. Any transaction error settings you configure on this page only apply to this account.

</section>
<section class="card">

## Example Transaction Error Webhook Payload

The `Detail` property contains the response that Cyclr receives. This means it changes depending on the API that’s called and how it formats its error responses.

If there are any specific errors you want to handle, you can force the error to occur and view the response to see the format.

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

### List of possible Message responses

* Trigger Skipped
* Transaction Stopped
* Out of retries
* Failed to authenticate the connector
* Required source is empty
* Webhook failed
* Failed to build the request
* Response data not in expected format
* Failed to call the method
* Response data fields missing
* Step data cannot be split
* Failed to split transaction step data
* Failed to save the webhook response
* Failed to return the webhook response
* Failed to build the webhook response
* Failed to find the webhook source key
* Failed to get webhook trigger step data
* Failed to find webhook trigger step
* Wait Until Failed To Run
* Wait Until is over retention period
* Field is not a valid DateTime
* WaitUntil step is missing wait criteria

</section>
