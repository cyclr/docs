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

To connect with Cyclr, you need a [LineLeader Enroll Account](https://login.lineleader.com/login?from=enroll). Service accounts are recommended for this purpose, 
 and can be created from within LineLeader Enroll by clicking Settings > Staff Settings > Service Accounts > Create Service Account. 
  
Note, only LineLeader Enroll users with the System Privilege of "Service Accounts" will be able to create service accounts. 



### Get authentication details

To authenticate your connector, you need to get the username and password associated with your service account. 
  They can be found in your LineLeader Enroll Dashboard by clikcin Settings > Staff Settings. Service accounts will be listed at the bottom of the page. 


Select the service account you intend to use Cyclr with and make a note of the username and password. 

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


### Account setup

Cyclr asks you for the below values when you install the <connector name> connector into an account:

   | Value              | Description                                 |
   | :----------------- | :------------------------------------------ |
   | **Username**       | The username of your web service account.   |
   | **password**       | The password of your web service account.   |
   | **URL**            | Choose the corresponding region (US/AUS).   |

> **Note**: You can use different details for different accounts.

</section>
