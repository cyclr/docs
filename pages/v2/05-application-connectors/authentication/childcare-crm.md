---
title: ChildCare CRM authentication
sidebar: cyclr_sidebar
permalink: childcare-crm-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

## ChildCare CRM setup

### Requirements

To connect with Cyclr, you need a [LineLeader Enroll Account](https://login.lineleader.com/login?from=enroll). Service accounts are recommended for this purpose. To create a service account from within LineLeader Enroll, select **Settings** > **Staff Settings** > **Service Accounts** > **Create Service Account**. 

> **Note**: Only LineLeader Enroll users with the **Service Accounts** System Privilege can create service accounts.

### Get authentication details

To authenticate your connector, you need to get the username and password associated with your service account. To find these authentication values in your LineLeader Enroll Dashboard, go to **Settings** > **Staff Settings** and you can view the service accounts listed at the bottom of the page. Select the service account you intend to use Cyclr with and make a note of the username and password. 

</section>
<section class="card">

## Cyclr setup

To set up the ChildCare CRM connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the ChildCare CRM connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | Value              | Description                                 |
   | :----------------- | :------------------------------------------ |
   | **Username**       | The username of your web service account.   |
   | **password**       | The password of your web service account.   |
   | **URL**            | Choose the corresponding region (US/AUS).   |

5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.
