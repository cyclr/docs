---
title: Fabric Authentication
sidebar: cyclr_sidebar
permalink: fabric-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Fabric setup

### Requirements

To connect with Cyclr, you need:

- A Client ID
- A Client Secret
- An Authorization URL/Domain
- An Authorization Server ID
- A Tenant ID (Also known as Account ID)
- The name of the environment (Also known as the "stage")

Optionally, you can also include:

- A Sales Channel ID
- A Source value

The Client ID, Client Secret, Authorization URL and Authorization Server ID can be found on your application information page. (https://live.copilot.fabric.inc/home/developer-tools/app/api/)

The Tenant ID can be found on your account details page. (https://live.copilot.fabric.inc/home/account-details)

For more information, see the Fabric documentation on authentication (https://developer.fabric.inc/reference/identity-developer-guide-concepts).

</section>
<section class="card">

## Cyclr setup

To set up the Fabric connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Fabric connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | **Value**          | **Description**                             |
   | :----------------- | :------------------------------------------ |
   | **Client ID**   | The Client ID of your application.      |
   | **Client Secret**   | The Client Secret of your application.   |
   | **Auth URL**| The domain of your authorization URL. For example, if your authorization URL is "https://cyclr-test.login.fabric.inc/oauth2/jnd2fsnci8z1mWXG3950", you should enter "cyclr-test.login.fabric.inc".      |
   | **Auth Server ID**| The identifier of the auth server you would like to target, found in the authorization URL. For example, if your authorization URL is "https://cyclr-test.login.fabric.inc/oauth2/jnd2fsnci8z1mWXG3950", you should enter "jnd2fsnci8z1mWXG3950".       |
   | **Tenant ID**| Your account ID, found in the fabric console.       |
   | **Environment**| The name of the environment you would like to access. Also known as a stage.       |
   | **Sales Channel ID (Optional)**| The sales channel ID of the of the source you would like to access.       |
   | **Source (Optional)**| The source you would like to access.       |
   | **Scopes (Optional)**| This field allows for custom scopes to be used during authorization       |

5. Select **Save Changes**.

> **Note**: If you leave any values (other than scopes) blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.


### Account setup

Cyclr asks you for the below values when you install the Fabric connector into an account:

   | **Value**          | **Description**                             |
   | :----------------- | :------------------------------------------ |
   | **Client ID**   | The Client ID of your application.      |
   | **Client Secret**   | The Client Secret of your application.   |
   | **Auth URL**| The domain of your authorization URL. For example, if your authorization URL is "https://cyclr-test.login.fabric.inc/oauth2/jnd2fsnci8z1mWXG3950", you should enter "cyclr-test.login.fabric.inc".      |
   | **Auth Server ID**| The identifier of the auth server you would like to target, found in the authorization URL. For example, if your authorization URL is "https://cyclr-test.login.fabric.inc/oauth2/jnd2fsnci8z1mWXG3950", you should enter "jnd2fsnci8z1mWXG3950".       |
   | **Tenant ID**| Your account ID, found in the fabric console.       |
   | **Environment**| The name of the environment you would like to access. Also known as a stage.       |
   | **Sales Channel ID (Optional)**| The sales channel ID of the of the source you would like to access.       |
   | **Source (Optional)**| The source you would like to access.       |

> **Note**: You can use different details for different accounts.

</section>