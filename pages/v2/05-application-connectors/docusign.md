---
title: Docusign Connector Guide
sidebar: cyclr_sidebar
permalink: docusign-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## DocuSign setup

To use Cyclr to connect with the DocuSign API, you need to create an Application in the DocuSign account, as detailed below:

  > **Note**: A partner only has to create the application once. The client/customer doesn't need their own separate application within DocuSign.

1. Login to your DocuSign Portal.
2. Go to **Settings** > **Integrations** > **Apps and Keys**.
3. Select the **ADD APP AND INTEGRATION KEY** button.
4. Enter a name for your app.
5. Select **Authorization Code Grant**.
6. Add a secret key and copy this for later.
7. Add a **Redirect URI**, for example: {% raw %}https://{{YourCyclrServiceDomain}}/connector/callback{% endraw %}.
8. Enter a link to your privacy policy.
9. Save the application.

You need the integration key to set up the connector in Cyclr.
 
</section>
 <section class="card">

## Cyclr setup

To set up the DocuSign connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the <connector name> connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | Value              | Description                                 |
   | :----------------- | :------------------------------------------ |
   | **Client ID**   | The DocuSign `Integration Key`.               |
   | **Client Secret**   | The DocuSign `Secret Key`.                 |
   | **Callback URL** | Cyclr fills this field by default.          |
   | **Scopes** | **Optional**: You can leave this blank or you can reduce the scopes depending on the methods you require for interactions. This field is a space-separated list. Full list of scopes are [here](https://developers.docusign.com/platform/auth/reference/scopes/).          |

5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

### Account setup

### Account setup

Additional to any values you leave blank when you set up the connector, Cyclr also asks for the **Domain** when you install the connector into an account. You can select the correct domain with the dropdown:

* The Sandbox Domain is `account-d.docusign.com`.
* The Production Domain is `account.docusign.com`.

</section>
