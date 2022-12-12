---
title: PowerOffice Go Authentication
sidebar: cyclr_sidebar
permalink: poweroffice-go-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
## Partner Setup

#### Retrieving application key and client key
* [Register](https://api.poweroffice.net/Web/docs/index.html#/Common/Registration.md) as a developer to obtain an application key.
* Email PowerOffice Go support to retrieve an application key after account registration.
* You can also retrieve the client key once your application has been activated.

### Cyclr Setup

Setup your PowerOffice Go App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **PowerOffice go**
*   Click the **Setup** button

Enter the following values:

**Client ID**: This is the application key retrieved from above.

**Client Secret**: This is the client key retrieved from above.

**Environment**: The environment you would like to use the connector with. This can be either the "Demo" (https://api-demo.poweroffice.net) or "Live" (https://api.poweroffice.net) environment.

Your PowerOffice Go Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</section>
