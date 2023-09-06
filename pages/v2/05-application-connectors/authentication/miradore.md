---
title: Miradore authentication
sidebar: cyclr_sidebar
permalink: miradore-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Miradore setup

### Create API Key
1. Login into your Miradore account
2. Start by navigating into System > Infrastructure diagram in Miradore's Navigation menu.
3. In the infrastructure diagram, you should see a grey API icon indicating that the API has not yet been activated. Hover on the icon, and click the Activate button.
4. Wizard for activating the API should appear on top of the page. In the first step of the wizard, read the acknowledgment and tick the checkbox. Once you're done you can proceed by clicking Activate now.
5. After successful activation, the icon of the API should turn blue. Hover on the blue icon, and click Create key in order to generate an authentication key for the API.
6. In the next step, you are asked to enter a name for the API authentication key. This is important especially if you are going to create multiple authentication keys to be used with different information systems.
7. Next, create the API key. Write it down in a secure place, for security reasons, it cannot be seen from the Miradore user interface afterward.



For more information, see the Miradore documentation on [Getting started with API](https://www.miradore.com/knowledge/integrations/getting-started-with-api/).

</section>
<section class="card">

## Cyclr setup

To set up the Miradore connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Miradore connector.

3. Select the **Setup Required** icon.

4. Enter the Sub Domain then click Next. Then enter API key and the API secret, they have to be joined by a colon (e.g. key:secret):

   | **Value**           | **Description**                                                                 |
   | :-----------------  | :------------------------------------------------------------------------------ |
   | **Site Name**      | The name of your site.                                         |
   | **API Key**         | The API key from the Parter Connect subscription email.                         |


5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

</section>
