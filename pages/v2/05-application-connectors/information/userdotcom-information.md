---
title: User.com information
sidebar: cyclr_sidebar
permalink: userdotcom-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Webhooks

You can configure webhooks so that the completion of specific events triggers the step.

In this example, the creation of a new user triggers the webhook, and you can use the cycle to retrieve that user's details.

### Create User.com automation

To configure the a webhook, you need to create an automation within User.com:

1. From your selected application's dashboard, go to **Automations**.

   ![user dot com interface](./images/userdotcom_6.png)

2. From the Automations page, select **Create automation**.

   ![user dot com interface](./images/userdotcom_7.png)

3. From the **Triggers** menu, drag the **New user** trigger onto the automation builder.

   ![user dot com interface](./images/userdotcom_8.png)

4. From the **Actions** menu, drag the **Api call** action onto the automation builder.

   ![user dot com interface](./images/userdotcom_9.png)

   ![user dot com interface](./images/userdotcom_10.png)

### Get the Webhook URL in Cyclr

1. In the template builder, drag the **User Created** webhook and **Get User By ID** method onto the grid.

   ![user dot com interface](./images/userdotcom_11.png)

   ![user dot com interface](./images/userdotcom_12.png)

2. Select **Step setup** on the **User Created** webhook to show the URL.

   ![user dot com interface](./images/userdotcom_13.png)

### Configure the automation in User.com

1. In the User<span></span>.com automation builder, select the **API call** module to configure it's settings

2. Enter the webhook's URL, add the header `Content-Type: application/json`, and select **Save**.

   ![user dot com interface](./images/userdotcom_14.png)

3. From the top-right corner of the automation builder, select **Save and exit**.

   ![user dot com interface](./images/userdotcom_15.png)

4. Enter a name for the automation. From the **Timing** drop-down, select **Each time the condition is met**, make sure **Run this action - enable** is activated, and select **Save**.

    ![user dot com interface](./images/userdotcom_16.png)

### Set up the webhook in Cyclr

1. In the Cyclr template builder, select **Field Discovery** for the **User Created** webhook. This activates the field discovery action.

    ![user dot com interface](./images/userdotcom_17.png)

    ![user dot com interface](./images/userdotcom_18.png)

2.  Create a test user in User.com to send to the webhook, to provide the webhook it with a user object to extract fields from.
   1. From the User<span></span>.com dashboard navigate to **Data > People**

      ![user dot com interface](./images/userdotcom_19.png)

   2. Select **Create user**, enter test data and select **Save**.

    ![user dot com interface](./images/userdotcom_20.png)

3. Check for a notification within the Cyclr workflow builder that the fields have been successfully received.

    ![user dot com interface](./images/userdotcom_21.png)

4. Map the required **User ID** within  the **Get User By ID**'s step setup.

    ![user dot com interface](./images/userdotcom_22.png)

5. Select **Run** in the top-left corner of the workflow builder.

When the cycle is active, each time a user is created, the webhook triggers the cycle to retrieve the new user's details.

</section>
