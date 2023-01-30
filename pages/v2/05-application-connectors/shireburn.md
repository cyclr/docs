---
title: Shireburn Connector Guide
sidebar: cyclr_sidebar
permalink: shireburn-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## API Keys

The Shireburn connector is authenticated with two API Keys.

### Open API Key

To obtain an Open API Key you must first create a user account and assign that user the relevant permissions. The steps necessary to do this are described [here](http://indigohelp.shireburn.com/en/articles/3203157-how-to-obtain-an-open-api-key-in-indigo-beta).

### Azure API Key

To obtain your Azure API Key you must first create a developer account and subscribe to the 'Payroll Standard' product.
The steps necessary to do this are described [here](http://indigohelp.shireburn.com/en/articles/3203147-create-your-indigo-api-developer-account-and-subscribe-to-a-product-beta).

Once the state of your Payroll Standard subscription changes to 'Active' you will see a 'Primary Key'. This is your Azure API Key.

> It can take several hours for your subscription to be activated. If necessary contact Shireburn support for assistance.


</section>
<section class="card">
## Authenticate The Connector

1. Locate the Shireburn connector

   > Cyclr Console > Connectors > Connector Library > Shireburn

2. From the Edit Connector interface click 'Setup'

3. Enter your Azure API Key (Primary Key) and click 'Next'

4. Enter your API Key (Open API Key) and click 'Next'

The connector is now authenticated and ready to use.

### How to find your Company Code
 1. Log into your Indigo Suite account

 2. Select Administration in the left navigation menu 

 3. Select Companies from the list of options

 4. Highlight and copy the code for your company
 
 5. Paste in the field below

</section>
