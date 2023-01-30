---
title: Clover Authentication
sidebar: cyclr_sidebar
permalink: clover-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">
# Clover

This guide is for setting up and installing the [Clover](https://cyclr.com/integrate/clover) connector.

#### Setup in Clover

Go to [clover.com/developers](https://www.clover.com/developers/) and create a new application.  
In the new application go to Settings and:

*   Update the Web Configuration setting Site URL to be your Cyclr Service Domain. Available from Cyclr Console > Settings > General Settings
*   Update the permissions setting checking everything other than "Process Credit Cards"
*   The App ID is the Client ID and the App Secret is the Client Secret.  Copy them as they are needed later.

#### Setup in Cyclr

If you don't need to use webhooks, login to your Cyclr Console and in the top menu go to Connectors > Connector Library. Find the Clover connector in the list and click its Setup button.

*   Set the Client ID as the App ID
*   Set the Client Secret as the App Secret

#### Install/Authenticate a connector

*   Enter the domain for Clover, either US or Europe
*   Click the sign in button
*   If required in the popup, install the application, then close the popup and the sign in button again.

</section>
