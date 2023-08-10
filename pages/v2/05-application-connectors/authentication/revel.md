---
title: <Connector name> authentication
sidebar: cyclr_sidebar
permalink: <connector name in lowercase, replace spaces with hyphens>-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Revel setup

### Requirements

To connect with Cyclr, you need to contact Revel directly for a Developer login.

### Get authentication details

To authenticate your connector, you need to get the authentication details. 

Go to the [<page name>](<link for page that shows authentication details>) page and make note of the <needed authentication details>.

</section>
<section class="card">

## Cyclr setup

To set up the Revel connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Revel connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | **Value**          | **Description**                             |
   | :----------------- | :------------------------------------------ |
   | **API Key**        | The API Key provided in your  xxxxxxxx      |
   | **<value name>**   | <description>                               |
   | **<default value>**| Cyclr fills this field by default.          |

5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.


### Account setup

Cyclr asks you for the below values when you install the Revel connector into an account:

   | **Value**          | **Description**                                                                                         |
   | :----------------- | :------------------------------------------------------------------------------------------------------ |
   | **Subdomain**      | The unique domain for the given client. E.g. for 'https://cyclr.revelup.com/resources' put in 'cyclr'.  |

> **Note**: You can use different details for different accounts.

</section>
