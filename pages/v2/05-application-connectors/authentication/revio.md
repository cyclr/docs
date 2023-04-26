---
title: Rev.io Authentication
sidebar: cyclr_sidebar
permalink: revio-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

## Rev.io setup

To authenticate your connector, you need to get the username and password of the Rev.io account.

You also need to know your Rev.io instance, as you need to enter the username in the format `username@{clientcode}`, where `{clientcode}` is your Rev.io instance. For example, if your instance is `CompanyA.rev.io`, your `{clientcode}` is `CompanyA`. 

> **Note**: To run API calls against the Rev.io sandbox instead of a live instance, use `api_sandbox` as the `{clientcode}`.      


</section>
<section class="card">

## Cyclr setup

To set up the Rev.io connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Rev.io connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | **Value**          | **Description**                             |
   | :----------------- | :------------------------------------------ |
   | **Username**   | The username you use to log into your Rev.io instance.                        |
   | **Password**   | The password you use to log into your Rev.io instance.                        |

5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

</section>
