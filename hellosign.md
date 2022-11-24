---
title: HelloSign Authentication
sidebar: cyclr_sidebar
permalink: hellosign-connector
tags: [connector]
---

# HelloSign setup

To install the HelloSign connector you will need to setup and/or obtain either:

- An API key for your HelloSign account.
- Or a client ID and client secret by setting up OAuth2.0 authentication for your HelloSign account.

## Obtain an API key

You can find HelloSign's documentation on API accounts [here](https://faq.hellosign.com/hc/en-us/articles/360035403131-HelloSign-API-accounts-and-how-to-find-your-API-key) and on where to find your API key [here](https://faq.hellosign.com/hc/en-us/articles/236400127-Where-to-find-your-API-Key).

## Setup OAuth2.0 authentication

You can find HelloSign's documentation on setting up OAuth2.0 authentication [here](https://developers.hellosign.com/docs/oauth/walkthrough/#app-setup). When creating an HelloSign app, set the **OAuth callback URL** to your Cyclr callback URL. This has the format: `https://{Your Cyclr service domain e.g. app-h.cyclr.com}/connector/callback`. Once you have created a HelloSign app, view the details of the app and make note of the **Client ID** and **Client Secret**.

# Cyclr setup

The HelloSign connector can be installed using either API Key or OAuth2 authentication.

## API key setup

### Account setup

You will be asked for the following values when installing the HelloSign connector within an account:

| Value        | Description                                                  |
| :----------- | :----------------------------------------------------------- |
| **Base URL** | The URL of the server you are connecting to. By default this will be `https://api.hellosign.com/v3`. |
| **API Key**  | The API key for your HelloSign account.                      |

## OAuth2 setup

### Console setup

To setup the HelloSign connector within your Cyclr console:

1. Go to your **Cyclr Console**.
2. Select **Connectors** > **Application Connector Library** at the top of the page.
3. Use the search box to find the **HelloSign** connector.
4. Select the **Setup Required** icon.
5. Enter the below values, omitting this step will allow you to use different settings for each account on installation:

   | Value             | Description                              |
   | :---------------- | :--------------------------------------- |
   | **Client ID**     | The client ID of your HelloSign app.     |
   | **Client Secret** | The client secret of your HelloSign app. |

6. Select **Save Changes**

### Account setup

You will be asked for the following values when installing the HelloSign connector within an account:

| Value             | Description                                                  |
| :---------------- | :----------------------------------------------------------- |
| **Base URL**      | The URL of the server you are connecting to. By default this will be `https://api.hellosign.com/v3`. |
| **Client ID**     | The client ID of your HelloSign app, if you did not enter this in step 5 above. |
| **Client Secret** | The client secret of your HelloSign app, if you did not enter this in step 5 above. |

