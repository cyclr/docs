---
title: Quora Ads
sidebar: cyclr_sidebar
permalink: quoraads-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Partner Setup

### Setting up your Account

For your API integrations to work, you must [Email](ads-api-help@quora.com) Quora ads the following details:

- Redirect URI: https://*Your Cyclr service domain e.g. app-h.cyclr.com*/connector/callback
- Quora user (*with access to your advertising dashboard*) to associate the client to.
- A name for your application. 

Once registration is complete, the associated user can view their client ID and secret [here](https://www.quora.com/ads/oauth_client_data)

For further information setting up authentication, please see the [Official Quora Ads documentation](https://www.quora.com/ads/api9169a6d6e9b42452d500a61717d87d15d5fa49ec5b53030741178130#section/Authentication).


</section>
<section class="card">
## Cyclr Setup

Setup your Quora Ads within Cyclr:

- Go to your **Cyclr Console**
- Click the **Connectors** menu along the top
- Choose Connector Library
- Select the  **Quora Ads** Connector
- Click the **Setup** button

Enter the following values:


> **Client ID**: Your [Client ID](https://www.quora.com/ads/oauth_client_data).
>
> **Client Secret**: Your [Client Secret](https://www.quora.com/ads/oauth_client_data).

Your Quora Ads Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</section>
