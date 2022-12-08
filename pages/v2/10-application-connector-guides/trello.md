---
title: Trello Authentication
sidebar: cyclr_sidebar
permalink: trello-connector
tags: [trello,connector]
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
## Partner Setup

To set up the Trello Connector you will need an API Key and a Secret.

1. You can find the API Key on the following page: [https://trello.com/app-key](https://trello.com/app-key)

2. Under **Allowed Origins** > **Current Origins** enter your callback URL:
<br><br>https://``Your-Service-Domain``/connector/callback<br><br>Your service domain can be found in your Cyclr console under Settings > General Settings > Service Domain.

3. Note the OAuth1 Secret:<br>![OAuth1 Secret](./images/oauth1secrettrello.png)

4. You can now enter the API Key from Step 1 and the Secret from Step 3 in your Cyclr Console, and authenticate the Trello Connector.

</section>
