---
title: UtilizeCore Authentication
sidebar: cyclr_sidebar
permalink: utilizecore-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

## UtilizeCore setup


To connect with UtilizeCore, you need the following authentication values:
* **Client ID**
* **Client Secret**
* **Username**
* **Password**
* **Environment** 
* **Subdomain**

If you need more information, contact your UtilizeCore account manager. The UtilizeCore API documentation can be found [here](https://app.swaggerhub.com/apis-docs/utilizecore/utilizecore-mobile/2.0.0#/).

</section>

<section class="card">

## Cyclr setup

To set up the UtilizeCore connector in Cyclr, go to your console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the UtilizeCore connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | Value              | Description                                 |
   | :----------------- | :------------------------------------------ |
   | **Client ID** | The Client ID authorized to access the instance. |
   | **Client Secret**     | The Client Secret authorized to access the instance. |
   
7. Select **Save**.

### Account setup

Cyclr asks you for the below values when you install the UtilizeCore connector into an account:

| Value           | Description                                                  |
| :-------------- | :----------------------------------------------------------- |
| **Username**    | The username of the authorized user.                         |
| **Password**    | The password of the authorized user.                         |
| **Environment** | The **Environment** indicates if your UtilizeCore instance is a staging or production one. This can be selected using the drop down list of options. |
| **Subdomain**   | The **Subdomain** makes up part of your UtilizeCore instance URL. For example, if your instance URL is `https://devs.staging.utilizecore.com/api/v2/vendors` then the subdomain is `devs`. |

> **Note**: You can use different details for different accounts.


</section>
