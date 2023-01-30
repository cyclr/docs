---
title: Podio Connector Guide
sidebar: cyclr_sidebar
permalink: podio-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">
## Authentication

### Podio Interface

To authenticate the connector you will need a **Client ID** and **Client Secret** for the Podio App you wish to interact with.

To generate these values, follow [this link](https://podio.com/settings/api) and then under 'API Key Generator':

1. Enter the name of the application you wish to interact with
2. Enter a return URL (redirect URL)

   > The redirect URL should be https://{service domain}/connector/callback. Your service domain can be found in your Cyclr console under Settings > General Settings > Service Domain.

3. Click 'Generate API Key'

### Cyclr Interface

1. Locate the Podio connector in the Cyclr console

   > Cyclr Console > Connectors > Connector Library > Podio

2. Click the open padlock and on the next page enter the **Client ID** and **Client Secret**.

The connector is now authenticated and ready to use.

> It may be the case that you require access to multiple Apps within one Podio account. Our tests have shown that authenticating the connector with one Client ID and Client Secret should give full functionality to the connector across all methods.

</section>
