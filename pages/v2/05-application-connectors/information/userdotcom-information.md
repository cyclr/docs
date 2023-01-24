---
title: User.com Connector Guide
sidebar: cyclr_sidebar
permalink: userdotcom-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

### Webhooks

You have the ability to configure webhooks, triggered upon the completion of specified events.

In this example we will configure a webhook that is triggered upon the creation of a new user. We will then retrieve that user's details.

1. From your selected application's dashboard, go to **Automations**

   ![user dot com interface](./images/userdotcom_6.png)

2. From the Automations page, **Create automation**

   ![user dot com interface](./images/userdotcom_7.png)

3. From the **Triggers** menu, drag **New user** onto the automation builder

   ![user dot com interface](./images/userdotcom_8.png)

4. From the **Actions** menu, drag **Api call** onto the automation builder

   ![user dot com interface](./images/userdotcom_9.png)

   ![user dot com interface](./images/userdotcom_10.png)

5. Now back within Cyclr, drag the **User Created** webhook and **Get User By ID** method onto the workflow builder

   ![user dot com interface](./images/userdotcom_11.png)

   ![user dot com interface](./images/userdotcom_12.png)

6. Click 'Step setup' (the cog icon) for the **User Created** webhook. This will expose it's URL

   ![user dot com interface](./images/userdotcom_13.png)

7. Now back within the User<span></span>.com automation builder, click the **API call** module to configure it's settings

8. Enter the webhook's URL and add the header **Content-Type**: **application/json**. Click 'Save'

   ![user dot com interface](./images/userdotcom_14.png)

9. From the top-right corner of the automation builder, click 'Save and exit'

   ![user dot com interface](./images/userdotcom_15.png)

10. Enter a name for the automation, from the 'Timing' drop-down select 'Each time the condition is met', make sure 'Run this action - enable' is activated, and click 'Save'

    ![user dot com interface](./images/userdotcom_16.png)

11. Back in Cyclr's workflow builder, select 'Field Discovery' for the **User Created** webhook. This will activate the field discovery action

    ![user dot com interface](./images/userdotcom_17.png)

    ![user dot com interface](./images/userdotcom_18.png)

12. We need to create a test user which will be sent to the webhook, providing it with a user object to extract the fields from

13. From the User<span></span>.com dashboard navigate to **Data > People**

    ![user dot com interface](./images/userdotcom_19.png)

14. Click 'Create user', enter some dummy data and click 'Save'

    ![user dot com interface](./images/userdotcom_20.png)

15. You should receive a notification within the Cyclr workflow builder that the fields have been successfully received

    ![user dot com interface](./images/userdotcom_21.png)

16. You can now map the required **User ID** within **Get User By ID**'s step setup.

    ![user dot com interface](./images/userdotcom_22.png)

17. Now that the workflow has been configured click 'Run' in the top-left corner of the workflow buider

The workflow is now active. Each time a user is created, the webhook will be triggered and the new user's details will be retrieved.

</section>
