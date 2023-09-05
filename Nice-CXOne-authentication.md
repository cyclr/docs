---
title: Nice CXOne authentication
sidebar: cyclr_sidebar
permalink: nice-cxone-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Nice CXOne setup

### Register Application

To setup up the Nice CXOne connector, you need to register an Application. You can find Nice CXOne's guide to do this [here](https://developer.niceincontact.com/Documentation/ApplicationRegistration).

### Get authentication details

To authenticate your connector, you need a Client ID, Client Secret, an Access Key ID, and Access Key Secret. 

Your Client ID and Client Secret can be obtained through the [application registration](https://developer.niceincontact.com/Documentation/ApplicationRegistration) process and will be provided by CXOne.

Your Access Key ID and Access Key Secret can be obtained by:

1. Click Profile in the right corner of the CXone top navigation bar.

2. Click **My Profile** from the drop-down.

3. Click **Access Keys**. Click **Add access key**.

   Note:

   You can only view the **Secret Access Key** while you are in the My Profile window. Once you exit the window, you will no longer be able to view the secret key.

If you have any trouble obtaining an Access Key ID and Access Key Secret, follow [this guide](https://help.nice-incontact.com/content/globalfeatures/myprofile/myprofile.htm) or contact your Nice CXOne account manager.

</section>

<section class="card">

## Cyclr setup

To set up the Nice CXOne connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Nice CXOne connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | **Value** | **Description**                  |
   | :-------- | :------------------------------- |
   | username  | Your application's Client ID.    |
   | password  | Your application's Client Secret |

5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

### Account setup

Cyclr asks you for the below values when you install the Nice CXOne connector into an account:

| **Value**         | **Description**                                              |
| :---------------- | :----------------------------------------------------------- |
| Access Key ID     | The user access key id from a user on the business unit you want to make the API call against. |
| Access Key Secret | The user access key secret from a user on the business unit you want to make the API call against. |

> **Note**: You can use different details for different accounts.

</section>