---
title: AWS EC2 Authentication
sidebar: cyclr_sidebar
permalink: ec2-connector
tags: [connector]
---

## Partner Setup

First, login to your existing AWS account or [sign up for one.](https://aws.amazon.com/)

#### Retrieving API Details

*   [Login](https://console.aws.amazon.com/console/home) to the AWS account. Make sure the region is set correctly.
*   Navigate to the **IAM** service by clicking on **Services** and searching for **IAM**.
*   Under **Acccess Management**, click **Users**.
*   Add or edit a user. Make sure the user has the correct EC2 permissions; the **EC2InstanceConnect** permission is required to use the connector.
*   Click on the newly created or edited user, and click **Security Credentials**. 
*   Create an **Access Key**. Note down then **Access Key ID** and **Access Secret Key**. This will be the only time you will be able to see the Secret Key, so keep it somewhere safe.

### Connector Setup

Setup the Amazon EC2 App within Cyclr:

*   Go to the **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Amazon EC2**
*   Click the **Setup** button

Enter the following values:

**AWS Access Key**: The Access Key that we noted down earlier when we created a new access key.

**AWS Secret Key**:  The Secret Key that we noted down earlier when we created a new access key.


Your Amazon EC2 Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
