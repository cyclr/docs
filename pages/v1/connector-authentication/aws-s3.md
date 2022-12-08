---
title: AWS S3 Authentication
sidebar: cyclr_sidebar
permalink: s3-connector
keywords: s3
tags: [connector]
---

### Important Note about Bucket Names

Due to limitations in the Amazon S3 API, it's not possible to access a bucket's contents if its name contains a period (.)

## Partner Setup

First, login to your existing AWS account or [sign up for one.](https://aws.amazon.com/)

#### Retrieving API Details

*   [Login](https://console.aws.amazon.com/console/home) to the AWS account. Make sure the region is set correctly.
*   Navigate to the **IAM** service by clicking on **Services** and searching for **IAM**.
*   Under **Acccess Management**, click **Users**.
*   Add or edit a user. Make sure the user has the correct permissions.
*   Click on the newly created or edited user, and click **Security Credentials**. 
*   Create an **Access Key**. Note down then **Access Key ID** and **Access Secret Key**. This will be the only time you will be able to see the Secret Key, so keep it somewhere safe.

### Connector Setup

Setup the Amazon S3 App within Cyclr:

*   Go to the **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Amazon S3**
*   Click the **Setup** button

Enter the following values:

**AWS Access Key**: The Access Key that we noted down earlier when we created a new access key.

**AWS Secret Key**:  The Secret Key that we noted down earlier when we created a new access key.


Your Amazon S3 Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
