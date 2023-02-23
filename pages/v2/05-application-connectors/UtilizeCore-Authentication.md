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
* **Password**.
* **Domain** 

The domain of the instance you want to access has selectable values, with the option of custom domain entry. For example, if the link you want to access is `https://msnw.staging.utilizecore.com/api/v2/vendors`, then the **Domain** is `msnw.staging.utilizecore.com`.

For more information on how to obtain the authentication values, see the UtilizeCore [API reference documentation](https://app.swaggerhub.com/apis-docs/utilizecore/utilizecore-mobile/2.0.0#/).

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
   | **Client ID** | The Client ID, authorized to access the desired application. |
   | **Client Secret**     | The Client Secret, authorized to access the desired application. |
   | **Username** | The Username of the authorized user.              |
   | **Password** | The Password of the authorized user. |
   | **Domain** (Optional) | The domain and subdomain of the request, used to target the correct resource. |

7. Select **Save**.

</section>
