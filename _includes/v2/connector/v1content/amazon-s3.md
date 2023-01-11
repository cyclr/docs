
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content required" markdown="1">

**Bucket Names**

You cannot access a bucket's contents if the bucket name contains a period (.)

This is a limitation in the Amazon S3 API.

</div>


<div class="section-content" markdown="1">

Login to your existing AWS account or [sign up for one.](https://aws.amazon.com/)

Retrieve API Details

- [Login](https://console.aws.amazon.com/console/home) to the AWS account. Make sure the region is set correctly.
- Click on **Services** and find  **IAM**.
- Under **Acccess Management**, click **Users**.
- Add or edit a user. The user must have the correct permission to use the connector.
- Click on the newly created or edited user
- Click **Security Credentials**. 
- Create an **Access Key**. 
- Note the **Access Key ID** and **Access Secret Key**. You cannot view the Secret Key again after creating the Access Key.

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Setup the Amazon S3 App within Cyclr:

- Go to the **Cyclr Console**
- Click the **Connectors** menu along the top
- Choose Connector Library
- Scroll down to **Amazon S3**
- Click the **Setup** button

Enter the following values:

**AWS Access Key ID**: The Access Key ID noted on creating the Access Key.

**AWS Secret Key**:  The Secret Key noted on creating the Access Key. 

Your Amazon S3 Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</div>

</section>