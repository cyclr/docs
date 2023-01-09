---
title: Zendesk Chat Authentication
sidebar: cyclr_sidebar
permalink: zendesk-chat-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Partner Setup

#### Retrieving public and private key
* Login to your Zendesk Chat front-end. 
* Click the **Settings** cog on the left side of the page, then **Account**.
* On the top horizontal bar click **API & SDKs**.
* Navigate to **API** section and click **Add API Client**
* Fill up the fields with the required information, Client Name, Company and enter your Cyclr redirect URL (https://``Your Service Domain``/connector/callback).
* Click **Create API Client**.
* After creating the API client a pop up window will appear showing Client ID and Client Secret, this client secret will only be fully displayed once, please keep it safe.

### Cyclr Setup

Setup your Zendesk Sell App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Search for **Zendesk Chat**
*   Click the **Setup** button

Enter the following values:

**Client ID**: Retrieved from the above steps.
**Client Secret**: Retrieved from the above steps.
**Sub Domain**: The first part of your account URL, ie. https://mycompanysubdomain.zendesk.com/, the subdomain would be "mycompanysubdomain".


Your Zendesk Chat Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</section>
