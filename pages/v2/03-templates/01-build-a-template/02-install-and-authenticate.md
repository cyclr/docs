---
title: Install an application connector
sidebar: cyclr_sidebar
permalink: install-and-authenticate
tags: [templates]

menus:
    build-a-template:
        title: Install an application connector
        identifier: install-and-authenticate
        toggleonly: menutoggleonly
        weight: 2
---
{::options parse_block_html="true" /}
<section class="card">

You can create cycle templates to connect and transfer data with third party applications. To build an integration for a specific application, you need to use the specific application connector. Each application connector contains steps and methods that you can use to create the integration. 

To further customize your integrations, you can also use utility connectors and tools. For more information on connectors, see the [connector introduction](connector-introduction) page.


</section>
<section class="card">

## Install the connector

You can install a new application connector from in the template builder:

1. Select **Application Connectors** from the sidebar on the right side of the window.
2. Select **Add Application** to install a new application connector.
3. Use the search bar to find the connector you want to install and select **Install**.
4. Enter a name and description to help you identify the connector.
5. To [authenticate](#authenticate) the connector, select **Next** and enter the authentication values you want to use. <br>    **Note**: You also have the option to skip this step and install with the connector without authentication.

</section>
<section class="card">

## Authenticate

To test a template, you need to authenticate the connectors you use so that Cyclr can connect and transfer data. Each application connector has an [authentication guide](http://connector-guides) that you can use. The guide details what you need to set up in the third party application, and the authentication details that you need.

Once you authenticate your connector, Cyclr returns you to the template builder and displays the connector in the right sidebar.

</section>
<section class="card">

## Related pages

*  [Application connector guides](connector-guides)
*  [Utility connectors](utility-connectors)

</section>