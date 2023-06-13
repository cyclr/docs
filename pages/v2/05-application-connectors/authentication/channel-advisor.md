---
title: Channel Advisor authentication
sidebar: cyclr_sidebar
permalink: channel-advisor-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Channel Advisor setup

### Requirements

To connect with Cyclr, you need a Channel Advisor API Developer Account.

Request a [Channel Advisor developer account](https://complete.channeladvisor.com/DeveloperNetwork/RequestApiDevKey.aspx).
Here you'll obtain a `Developer API Key`.

### Get authentication details

To authenticate your connector, you need to get the authentication details. 

Go to the [Developer Console](https://api.channeladvisor.com/DeveloperConsole) page and make note of the `Application ID` and `Shared Secret` for your app.
  
Enter the redirect URI as 'https://connectordev.cyclr.uk/connector/callback'.
  
Select `Add Integration and Request Tokens`. Make a note of the `Refresh Token`.

</section>
<section class="card">

## Cyclr setup

To set up the Channel Advisor connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Channel Advisor connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | **Value**          | **Description**                                    |
   | :----------------- | :------------------------------------------------- |
   | **Application ID** | The ID for the application you created.            |
   | **Shared Secret**  | The secret for the application you created.        |
   | **Scopes**         | List of access scopes seperated with a space.      |
   | **Refresh Token**  | The refresh token for the application you created. |

5. Select **Next**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.
  
6. OAuth2 requires you to enter the below values:
  
   | **Value**          | **Description**                                           |
   | :----------------- | :-------------------------------------------------------- |
   | **Email**          | The email address associated with the developer account.  |
   | **Password**       | The password associated with the developer account.       |

</section>
