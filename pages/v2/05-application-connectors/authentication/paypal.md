---
title: PayPal authentication
sidebar: cyclr_sidebar
permalink: paypal-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
  
## PayPal setup
To set up the PayPal connector you require the following:

*  A PayPal [Developer Account](https://www.paypal.com/signin/client?flow=provisionUser&country.x=US&locale.x=en_US).
*  A PayPal **Client ID** and **Client Secret**.

### Get authentication details

To authenticate your connector, you need to get the authentication details from your **Developer Account**:

1. Create a [Developer Account](https://www.paypal.com/signin/client?flow=provisionUser&country.x=US&locale.x=en_US) if you do not already have one. This automatically creates a business and personal account in a default app.
2. Select the **Developer Dashboard** to view your credentials.
3. Make a note of the **Client ID** and **Client Secret**.
4. For testing, make sure the toggle switch is set to **Sandbox**.

</section>
<section class="card">

## Cyclr setup

To set up the PayPal connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the PayPal connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

| Value              | Description                                    |
| :----------------- | :--------------------------------------------- |
| **Client ID**      | The Client Id from the Developer Dashboard.    |
| **Client Secret**  | The Client Secret from the Developer Dashboard. |
| **Environment**    | Choose between **Sandbox** and **Production**. |

5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

</section>
