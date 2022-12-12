
<section class="authentication" markdown="1">

## Authentication

| Type      | None |
| Description | https://docs.aws.amazon.com/aws-backup/latest/devguide/authentication.html |
{: .table .vheader}

</section>

<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Login to your existing AWS account or [sign up for one.](https://aws.amazon.com/)

### Retrieving API Details

- [Login](https://console.aws.amazon.com/console/home) to the AWS account. Make sure the region is set correctly.
- Click on **Services** and find for **IAM**.
- Under **Acccess Management**, click **Users**.
- Add or edit a user. The user  must the **AWSBackupFullAccess** permission to use the connector.
- Click on the newly created or edited user
- Click **Security Credentials**. 
- Create an **Access Key**. 
- Note down then **Access Key ID** and **Access Secret Key**. You cannot view the Secret Key again after creating the Access Key.

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Setup the AWS Backup App within Cyclr:

- Go to the **Cyclr Console**
- Click the **Connectors** menu along the top
- Click **Connector Library**
- Scroll down to **AWS Backup**
- Click the **Setup** button

Enter the following values:

**AWS Access Key**: The Access Key noted on creating the Access Key.

**AWS Secret Key**:  The Secret Key noted on creating the Access Key.

Your AWS Backup Connector is now setup!

</div>
</section>