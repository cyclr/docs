---
title: Custom connector introduction
sidebar: cyclr_sidebar
permalink: connector-introduction
tags: [connector-creation]
menus:
    custom-connectors:
        title: Custom connector introduction
        identifier: connector-introduction
        toggleonly: menutoggleonly
        weight: 1
---
{::options parse_block_html="true" /}
<section class="card">
## What is a Cyclr custom connector?

A custom connector allows you to integrate apps that aren’t in our [connector library](http://cyclr.com/connectors/). You can also use a custom connector to connect your own private apps and websites.

>  **Note**:  Not all price plans include access to the custom connector builder. If available, you can access the builder in the console, under the **Connectors** tab.

There are two ways to add a custom connector:
*  Create a connector.
*  Import an API specification for a connector.

For both methods, you can add [scripts](connector-scripting) to further customise the connector.


</section>
<section class="card">
## Create a connector in the console

You can create a connector in the Cyclr console through a process of specification.

To create a connector, go to your console:
1.  Go to **Connectors** > **Custom Connectors**.
2.  Select the **+** button, in the top right corner of the page.
3.  Enter a **Name** to identify the connector with, and select **Create**.

### Manually create the connector specification

 To create a connector without the need to write a coded integration, select the **Edit** icon (located to the right of the connector release) and fill out the fields in the Connector manager.

The manager works with the API to define properties such as the following:

| Property | Description | 
| --- | --- |
| Description | Gives the details of the Application's API, such as name, description, and version. |
| Authentication Method | Determines how the connector connects to the target API, such as OAuth, API key, and login. |
| Rate limiting & Throttling | Defines how frequently the connector makes calls to the API. |
| Methods / Endpoints | Defines the endpoints for the API. |

### Import a connector specification

If you import a connector, check the connector details to make sure it's set up correctly. You can still manually edit an imported connector if you need to make changes.

To import an existing API specification with the OpenAPI discovery tool:

1.  Select the **Generate From OpenAPI specification** button next to connector name.
2.  Enter the URL location.

    >**Note**: Cyclr supports OpenAPI versions 2.0 and 3.0.x in either JSON or YAML format.

To import a JSON file specification:

1. Select the **Import From JSON** button next to the connector name.
2. Enter the JSON script.
</section>
