---
title: Salesforce Upsert Setup
sidebar: cyclr_sidebar
permalink: salesforce-upsert-setup
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Additional information

### Using the Upsert Methods
 
Once you have setup your External ID field you are ready to use the corresponding Upsert method.

1. Copy the API Name of your External ID field from Salesforce:

    **Salesforce Classic**
    ![](./images/salesforce_custom_fields_api_name.png)

    **Lightning Experience**
    ![](./images/salesforce_custom_fields_api_name-lightning.png)

2. Go to setup the Upsert method in Cyclr, and insert the copied value into the 'External ID Field', and map your External ID value to the 'External ID' field.
    ![](./images/salesforce_custom_fields_cyclr.png)

</section>
