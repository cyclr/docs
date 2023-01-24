---
title: User.com Connector Guide
sidebar: cyclr_sidebar
permalink: userdotcom-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">
## Authentication

To authenticate the User<span></span>.com connector you will need your application's subdomain and API Key.

### Obtaining Your Authentication Credentials

1. [Login](https://app.user.com/accounts/login/) or [create an account](https://app.user.com/accounts/register/)

2. Select an existing application or create a new one. You must provide a subddomain for your application upon it's creation

   ![user dot com interface](./images/userdotcom_1.png)

   ![user dot com interface](./images/userdotcom_2.png)

3. From your selected application's dashboard, navigate to **Settings > Setup & integrations**

   ![user dot com interface](./images/userdotcom_3.png)

4. You will be redirected to a page where your application's key and subdomain are presented. (Note: This API Key is **not to be confused with the API Key used for authentication**, the API Key used for authentication will be a 64 character length string)

   ![user dot com interface](./images/userdotcom_4.png)

5. Using the credentials obtained in step 4, you can now access your Public REST API Key (used for authentication) at the following location:

   https://**Subdomain**.user.com/api/**ApplicationKey**/credentials/

   > So with the example credentials above our URL would be: `https://example.user.com/api/ABC123/credentials/`

6. Your Public REST API key should be present, if not you can generate a new one

   ![user dot com interface](./images/userdotcom_5.png)

### Connector Setup

1. Locate the User<span></span>.com connector

   > Cyclr Console > Connectors > Connector Library > User<span></span>.com

2. From the Edit Connector interface click 'Setup'

3. Enter your Subdomain, click 'Next'

4. Enter your API Key (64 character Public REST API key), click 'Next'

The connector is now authenticated and ready to use.

</section>
