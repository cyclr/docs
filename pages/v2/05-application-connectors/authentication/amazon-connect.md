---
title: Amazon Connect Authentication
sidebar: cyclr_sidebar
permalink: amazon-connect-connector
keywords: amazon-connect
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">


</section>
<section class="card">
## Partner Setup

First, login to your existing AWS account or [sign up for one.](https://aws.amazon.com/)

#### Retrieving API Details

*   [Login](https://console.aws.amazon.com/console/home) to the AWS account. Make sure the region is set correctly.
*   Navigate to the **IAM** service by clicking on **Services** and searching for **IAM**.
*   Under **Access Management**, click **Users**.
*   Add or edit a user. Make sure the user has the correct permissions.
*   Click on the newly created or edited user, and click **Security Credentials**. 
*   Create an **Access Key**. Note down then **Access Key ID** and **Access Secret Key**. This will be the only time you will be able to see the Secret Key, so keep it somewhere safe.

#### Create an Amazon Connect instance
  
  * The first step in setting up your Amazon Connect contact center is to create a virtual contact center instance. Each instance contains all the resources and settings related to your contact center. Refer to [Amazon Guide](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-instances.html) which provides detailed instructions on how to set it up.   
  * [Create a dev (Sandbox) or test (QA) instance](https://docs.aws.amazon.com/connect/latest/adminguide/create-connect-instance.html)
  * [Find your Amazon Connect instance ID/ARN](Find your Amazon Connect instance ID/ARN)
  
### Connector Setup

Setup the Amazon Connect App within Cyclr:

*   Go to the **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Amazon Connect**
*   Click the **Setup** button

Enter the following values:

**AWS Access Key**: The Access Key that we noted down earlier when we created a new access key.

**AWS Secret Key**:  The Secret Key that we noted down earlier when we created a new access key.
  
**Aws Region**:   The AWS Region where your Amazon Connect services are available.


Your Amazon Connect Connector is now set up. You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
  
 ### Add custom fields

Your records may contain custom fields which aren't mapped for each method's request or response fields. For example, method [Get Task Template](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetTaskTemplate.html) returns a list of custom tags.

To add mappings  for a custom field, you can follow the steps in the Cyclr documentation on how to [Add custom fields]([adding-custom-fields/](https://docs.cyclr.com/adding-custom-fields#manually-add-custom-fields)

To add a custom field, you need to provide the API field name for the **Field Location** of the custom field.

</section>
