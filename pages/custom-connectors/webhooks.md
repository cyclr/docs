---
title: Custom Connector Webhooks
sidebar: cyclr_sidebar
permalink: custom-connector-webhooks
tags: [connector-creation, webhooks]
---
### Automatically Instantiated Webhooks Via API Call

When an API supports setting up a webhook, this is often the best option to choose, as it allows the user to create webhooks without having to leave Cyclr.
This method requires three methods to be created: one will create the webhook in the external site, the other will delete the webhook, and the final will be the webhook shell, in which both of the other methods are called.

#### Creating The Webhook
The method for creating the webhook will be the same as any method which creates a resource, only when you receive the ID in response it will be mapped to a special system field: `Cyclr_Webhook_Id`.
For example if the response from your POST is: 
```javascript
{"id": 1, "active": true}
```
Then you would setup your field mappings like this:
![](./images/create_webhook_mapping.PNG)

Doing this saves the ID into the `Cyclr_Webhook_Id` parameter, so that we are able to delete it at a later time.

#### Deleting The Webhook
This method will be called when the Webhook step is deleted from a cycle, and will delete the webhook from the system in which it was created.
As an example, you have to send a http DELETE request formatted as such: `https://webhookexample.com/webhooks/{Id}` you can format the URL in Cyclr as: `https://webhookexample.com/webhooks/{{Cyclr_Webhook_Id}}}`. Using the mergefield: `{{Cyclr_Webhook_Id}}` will pull in the webhook ID that was saved from the create call and populate the URL with the correct value

##### *Note On Using Cyclr_Webhook_Id In Script:*
If you need to interact with the webhook ID in script at all you must add it as a mergefield to the URL as above, and also create field mappings in the *Parameters* tab, as seen below:
![](./images/delete_webhook_parameter.png)
To then interact with this in script you can call 
```javascript 
method_request_parameters.Cyclr_Webhook_Id
```

#### The Parent Webhook Method
This is the method that the end user will interact with, and act as the trigger step for a cycle.
Under *Settings* in the method, select Webhook as the *Method Type*, and set both the *Create Webhook Method* and *Delete Webhook Method* fields, select the corresponding method. Once done it should look something like below:
![](./images/webhook_example_settings.PNG)

When creating the field mappings for your webhook, the only ones to populate should be *Request Format*. In here you should generate mappings for the data that will be posted to the webhook.