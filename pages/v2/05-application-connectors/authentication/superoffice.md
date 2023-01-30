---
title: SuperOffice Authentication
sidebar: cyclr_sidebar
permalink: superoffice-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## SuperOffice set up

To set up the Kareo connector, you need the following authentication values from your SuperOffice account:

*  Username
*  Password

You also need the **API Domain** of your SuperOffice API instance. For example. if your api address is `https://www.example.com/crm/api/v1/`, the domain you need is`www.example.com/crm`.



</section>
<section class="card">
## Cyclr set up

To set up the SuperOffice connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the SuperOffice connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | Value              | Description                                 |
   | :----------------- | :------------------------------------------ |
   | **Domain**   | The external web address for your SuperOffice API instance.    |
   | **Username**   | The SuperOffice account username.                           |
   | **Password**| The SuperOffice account password.          |

5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.




</section>
