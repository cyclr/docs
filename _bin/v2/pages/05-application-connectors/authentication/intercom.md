---
title: Intercom Authentication
sidebar: cyclr_sidebar
permalink: intercom-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Intercom setup

Intercom uses OAuth 2 for remote API access. Register Cyclr within Intercom as your own app to get the OAuth Client ID and Client Secret values you need for Cyclr to authenticate with Intercom.

For more information, see the official Intercom documentation:
* [Creating an App](https://developers.intercom.com/building-apps/docs/get-started-developing-on-intercom)
* [Setting up OAuth](https://developers.intercom.com/building-apps/docs/setting-up-oauth)


</section>
<section class="card">
## Cyclr setup

### Account setup

Cyclr asks you for the below values when you install the Intercom connector into an account:

| Value | Description |
| :------------- | :------------------------ |
| **Client ID**        | The Client ID from your Intercom account. |
| **Client Secret**    | The Client Secret from your Intercom account. |

You need to add a callback URL to use Intercom in your Cyclr console and accounts. The URL is {% raw %}`https://{{your Cyclr service domain}}/connector/callback`{% endraw %}.
> **Note**: You can find your Cyclr service domain in your Cyclr Console under **Settings** > **General Settings**.

### Required Permissions

Cyclr requires the following permissions to create integrations with Intercom:

* Read one user and one company
* Write conversations
* Read admins

### Choose the correct version

There are connectors for multiple versions of the Intercom API. The available endpoints differ in each version, so you need to use the connector that matches the version your Intercom app uses.

To find out which version your app is set to:

1. [Login](https://app.intercom.com/admins/sign_in?on_pageview_event=sign_in_nav) to your Intercom account.

2. Hover over the icon in the bottom left corner and select **Settings**.
   
3. From the settings page, select **Apps and integrations** > **Developer Hub**.

4. Once in the Developer Hub, select the relevant app.

5. The **Basic Information** page displays information about the app, including the version.
   
6. To change the version, select **Change version** and then select the version you want from the dropdown.
   
> **Note: You can view the [changelog](https://developers.intercom.com/building-apps/docs/api-changelog) for a detailed description of the differences between each API Version.**


</section>
