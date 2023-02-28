---
title: Verint Engagement Data Management Authentication
sidebar: cyclr_sidebar
permalink: verint-engagement-data-management-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

## Verint - Engagement Data Management Setup

### Requirements

To connect with Verint, you need the **Username** and **Password** of the Verint account, and the **Domain** of the instance you want to access. You can find the domain in the URL of your Verint instance. For example, if the link is `https://odf4.verint.training/api/recording/textcapture/v1/ingestion`, then your domain is `odf4.verint.training`.

For more information, see the Verint [API reference documentation](https://connect.verint.com/developers/edm/w/api-reference/25356).

</section>
<section class="card">

## Cyclr setup


To set up the Verint connector in Cyclr, go to your console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Verint Engagement Data Management connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | Value              | Description                                 |
   | :----------------- | :------------------------------------------ |
   | **Domain** | The domain of the application server or load balancer address. |
   | **Username** | The Username of the authorized user.                       |
   | **Password** | The Password of the authorized user.                       |

7. Select **Save**.

</section>
