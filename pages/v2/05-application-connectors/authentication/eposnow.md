---
title: EposNow Authentication
sidebar: cyclr_sidebar
permalink: eposnow-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
  
## EposNow set up

### Requirements

You need to [create an API Device](https://developer.eposnowhq.com/Setup/APISetup) to
[get the Epos Key and Epos secret](#getting-the-epos-key-and-epos-secret). You can find EposNow's guide on creating an API Device in the Epos Now console [here](https://developer.eposnowhq.com/Setup/APISetup).

> **Note**: Each account has a limit on the number of API requests it can make.
When the number of requests exceeds this limit the API returns
`API Limit Exceeded` for any request. To check or update your EposNow API limits, go to the API page found in the [**Web Integrations**](https://developer.eposnowhq.com/Setup/ApiDevice) menu on
the EposNowHQ Backoffice.

### Get authentication details

You need a Epos Key and Epos Secret to authenticate the EposNow connector in
Cyclr. Before you can get these you need to [create an API Device](#requirements). For more information on how to obtain these authentication details, see [Epos Now's guide](https://developer.eposnowhq.com/Setup/ApiDevice) on how to get the Epos Key and Epos Secret in the EposNow
console.

</section>
<section class="card">
  
## Cyclr set up

To set up the EposNow connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the EposNow connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

 | **Value**          | **Description**                             |
 | :----------------- | :------------------------------------------ |
 | **Username**   | The [Epos Key](#get-authentication-details) of the EposNow account. |
 | **Password**   | The [Epos Secret](#get-authentication-details) of the EposNow account. |


5. Select **Save Changes**.

> **Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts.

</section>
