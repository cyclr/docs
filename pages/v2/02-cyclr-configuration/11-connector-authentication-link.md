---
title: OAuth authentication link
sidebar: cyclr_sidebar
permalink: connector-authentication-link
tags: [accounts]
menus:
    cyclr-configuration:
        title: Connector authentication link
        identifier: connector-authentication-link
        toggleonly: menutoggleonly
        weight: 11
---
{::options parse_block_html="true" /}
<section class="card">'

If your customer doesn't have access to Cyclr and doesn't want to share their credentials with you, you can allow them to authenticate an account connector themselves. To allow the customer to authenticate a connector, you can use an authentication link and token.

You can email the link and token to your customer so that they can access Cyclr just to authenticate a particular account connector.

1.  Go to the account that contains the connector you want to authenticate.
2.  Open the **Connectors** menu.
3.  Select **Edit Connector** next to the connector to be authenticated.
4.  Select **Generate Setup Token**.
  *  **Note**: Tokens you generate here expire after 5 minutes by default.  To edit the expiration time, use the date picker.
5.  Select **Generate** to see the token and a link to a web page where your user can enter it.

### Tokens

You can only use the token once, so you may need to go through these steps again if your user starts but doesn't complete the authentication.

If you need to authenticate more than one account connector, you can generate and send multiple setup tokens to your client but they should complete the authentication of each connector before they move on to the next.

</section>
