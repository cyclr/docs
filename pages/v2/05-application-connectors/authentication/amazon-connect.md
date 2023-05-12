---
title: Amazon Connect Authentication
sidebar: cyclr_sidebar
permalink: amazon-connect-connector
linkedpage: true
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
  
## Amazon Connnect setup

To connect with Cyclr, you need an AWS account. If you don't have an existing account, you can [sign up for one](https://aws.amazon.com/).

### Get authentication details

To authenticate your connector, you need the following authentication details:
*  Access Key ID
*  Access Secret Key
*  AWS Region
  
You can get the Access Key ID and Secret Access Key from your [IAM console](https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1.  From the navigation menu, select **Users**.
3.  Select your IAM user name (not the check box).
4.  Open the **Security credentials** tab, and then select **Create access key**.
5.  To see the new access key, select **Show**. Your credentials resemble the following:
    * Access key ID: `AKIAIOSFODNN7EXAMPLE`
    * Secret access key: `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`
6. To download the key pair, you can select **Download .csv file**.

### Create an Amazon Connect instance
  
In order to use the Amazon Connect connector with Cyclr, you need to set up a virtual contact center instance. For more information on how to set this instance up, see the [[Amazon Guide](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-instances.html).
  
You can also create developer and testing instances. For more information see the guide on how to [Create a dev (Sandbox) or test (QA) instance](https://docs.aws.amazon.com/connect/latest/adminguide/create-connect-instance.html).
  
If you need more information on how to find your instance, see the Amazon documentation on how to [find your Amazon Connect instance ID/ARN](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html).

</section>
<section class="card">
  
## Cyclr setup

To set up the Amazon Connect connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Amazon Connect connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | **Value**          | **Description**                             |
   | :----------------- | :------------------------------------------ |
   | **AWS Access Key** | The [Access Key](#get-authentication-details) from the AWS account.                               |
   | **AWS Secret Key** | The [Secret Key](#get-authentication-details) from the AWS account.                               |
   | **Aws Region**     | The AWS Region where your Amazon Connect services are available.          |

5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

</section>
