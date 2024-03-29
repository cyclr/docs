---
title: Salesforce SOAP Authentication
sidebar: cyclr_sidebar
permalink: salesforce-soap-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Partner Setup

#### Retrieving Details

You will need a security token to authenticate with Salesforce. This will have been sent to your email when creating your account. If you no longer have access to this token, you can reset it.

Use this link to reset your token: `https://\<**yoursalesforcehostname**>/_ui/system/security/ResetApiTokenEdit?retURL=%2Fui%2Fsetup%2FSetup%3Fsetupid%3DPersonalInfo&setupid=ResetApiToken`

Or through your account:

*   Login to your Salesforce Account.
*   Click on "Settings", under your profile picture.
*   Click "Rest My Security Token" under the "My Personal Information".
*   A security token will be sent to your email address. Note it down.

### Cyclr Setup

Setup your Salesforce SOAP App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Salesforce SOAP**
*   Click the **Setup** button

Enter the following values:

**Username**:  Enter your Salesforce username/email.

**Password**:  This is a combination of your Salesforce password and your security token. Enter the following: "\<SalesforcePassword>\<SecurityToken>". For example, if your password was "letmein" and your security token was "1234", you would enter "letmein1234" (without the quotation marks).


Your Salesforce SOAP Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</section>
