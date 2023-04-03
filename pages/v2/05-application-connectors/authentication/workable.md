---
title: Workable Authentication
sidebar: cyclr_sidebar
permalink: workable-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

## Workable setup
To authenticate your connector, you need to get your Workable **Subdomain** and an **Access Token** from Workable. 

### Get your Sub Domain
You can find your Workable Sub Domain in the URL of your Workable frontend. For example, if your Workable URL is `https://mycompany.com`, then your subdomain is `mycompany.com`.

### Get the Access Token
You can generate the API credentials in Workable's frontend:

1. Go to the Workable frontend and log in with your details
2.  Select **Settings** and go to the **Integrations** section.
3.  Select **Generate Token** and make a note of the **User Token** or **Partner token**.

For more information on the access tokens, see Workable's API documentation on [Partner Tokens](https://workable.readme.io/reference/partner-token).

</section>
<section class="card">

## Cyclr setup

To set up the Workable connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Workable connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | Value              | Description                                 |
   | :----------------- | :------------------------------------------ |
   | **Sub Domain**     | The sub-domain of your Workable instance.                            |
   | **Access Token**   | Either a User Token or Partner Token that you [generate in Workable](#get-your-sub-domain).                             |

5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

</section>
