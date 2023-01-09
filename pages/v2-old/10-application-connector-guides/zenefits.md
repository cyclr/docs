---
title: Zenefits Authentication
sidebar: cyclr_sidebar
permalink: zenefits-connector
tags: [connector]

---
{::options parse_block_html="true" /}
<section class="card">
## Zenefits setup

You need to register your application with Zenefits and request access to scopes before you can use the Zenefits connector. To authenticate your connector, you need the unique Client ID and Client Secret from your registered Oauth application. Refer to the [Zenefits documentation](https://developers.zenefits.com/docs/auth) for information on how to obtain credentials.


</section>
<section class="card">
## Cyclr setup

To set up the Zenefits connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Zenefits connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | Value             | Description                                                  |
   | :---------------- | :----------------------------------------------------------- |
   | **Base URL**      | The Base URL of your application’s API instance. The default value is https://api.zenefits.com. |
   | **Client ID**     | The Client ID from your Zenefits account.                    |
   | **Client Secret** | The Client Secret from your Zenefits account.                |

5. Select **Save Changes**.

> **Note**: To use different settings for different accounts, leave the value blank. This means Cyclr asks for the value when you install the connector into an account.



</section>
