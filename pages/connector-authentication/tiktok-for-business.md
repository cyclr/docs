---
title: TikTok for Business Authentication
sidebar: cyclr_sidebar
permalink: tiktok-for-business-connector
tags: [connector]
---

# TikTok for Business setup

You need to do the following to setup the TikTok for Business connector:

1. Create a TikTok for Business Account.
2. Register as a developer.
3. Create a developer app.
4. Get an app ID and secret from your developer app.

### Create a TikTok for Business Account

TikTok for Business's guide on how to create an account can be found [here](https://ads.tiktok.com/marketing_api/docs?id=1738855099573250).

### Register as a developer

TikTok for Business's guide on how to register as a developer can be found [here](https://ads.tiktok.com/marketing_api/docs?id=1738855176671234).

### Create a developer app

TikTok for Business's guide on how to create a developer app can be found [here](https://ads.tiktok.com/marketing_api/docs?id=1738855242728450). When creating the app set the fields as follows:

| Field                       | Value                                                                                                                                                                                                     |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Advertiser redirect URL** | The OAuth redirect URL of your Cyclr account. This has the format `https://{Your Cyclr service domain e.g. app-h.cyclr.com}/connector/callback`.                                                        |
| **Scope of permission**     | The following scopes need to be enabled for the connector to function correctly:<br/>`Ad Account Management` > `Ad Account Information` > `Read Ad Account Information`<br/>`Audience Management` > `All` |

### Get an app ID and secret

Find your created app under the **My Apps** section of the TikTok for business website [here](https://ads.tiktok.com/marketing_api/apps/). Select the app you want to install the connector using and make note of the **App ID** and **Secret**. These are both required to install the TikTok for business connector.

# Cyclr setup

The TikTok for Business connector can be used with two different authentication types: `Production Installation` or `Sandbox Installation`. The production installation should be used for live production accounts and the sandbox installation should be used for sandbox accounts. The `Advertisers` > `List Advertisers` method will not function when using the sandbox installation. Please see the additional information section for details on [TikTok for Business sandbox account setup](#tiktok-for-business-sandbox-account-setup).

### Console setup (production)

To setup the TikTok for Business production connector within your Cyclr console:

1. Go to your **Cyclr Console**.
2. Select **Connectors** > **Application Connector Library** at the top of the page.
3. Use the search box to find the **TikTok for Business** connector.
4. Select the **Setup Required** icon.
5. Enter the below values, omitting this step will allow you to use different settings for each account on installation:

    | Value             | Description                                 |
    | ----------------- | ------------------------------------------- |
    | **Client ID**     | The app ID of your TikTok for Business app. |
    | **Client Secret** | The secret of your TikTok for Business app. |

6. Select **Save Changes**.

### Account setup (production)

You will be asked for the following values when installing the TikTok for Business production connector within an account:

| Value             | Description                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------ |
| **Environment**   | The environment to install the TikTok for Business connector in. Select **Production**.    |
| **Client ID**     | The app ID of your TikTok for Business account, if you did not enter this in step 5 above. |
| **Client Secret** | The secret of your TikTok for Business account, if you did not enter this in step 5 above. |

### Account setup (sandbox)

You will be asked for the following values when installing the TikTok for Business sandbox connector within an account:

| Value           | Description                                                                          |
| --------------- | ------------------------------------------------------------------------------------ |
| **Environment** | The environment to install the TikTok for Business connector in. Select **Sandbox**. |
| **API Key**     | The access token of your TikTok for Business app sandbox ad account.                 |

# Additional information

<a name="tiktok-for-business-sandbox-account-setup"></a>

### TikTok for Business sandbox account setup

TikTok for business has sandbox account functionality for testing. You can find TikTok for Business's guide on how to set this up [here](https://ads.tiktok.com/marketing_api/docs?id=1738855331457026). Make note of the **Access Token** generated when doing this as it will be needed when installing the sandbox installation version of the connector.
