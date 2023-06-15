---
title: Channel Advisor authentication
sidebar: cyclr_sidebar
permalink: channel-advisor-connector
tags: [connector]

---
{::options parse_block_html="true" /}
<section class="card">

## Channel Advisor setup

### Requirements

To connect with Cyclr, you need a Channel Advisor API Developer Account.

To obtain a **Developer API Key**, you need to request a [Channel Advisor developer account](https://complete.channeladvisor.com/DeveloperNetwork/RequestApiDevKey.aspx).

### Get authentication details

To authenticate your connector, you need to get the following authentication details: **Application ID**, **Shared Secret**, and **Refresh Token**. 

To view **Application ID** and **Shared Secret**, go to the [Developer Console](https://api.channeladvisor.com/DeveloperConsole) page.
  
Enter the redirect URI as 'https://connectordev.cyclr.uk/connector/callback'.
  
To view the **Refresh Token**, select **Add Integration and Request Tokens**.

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
