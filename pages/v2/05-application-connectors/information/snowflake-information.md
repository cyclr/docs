---
title: Snowflake information
sidebar: cyclr_sidebar
permalink: snowflake-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Create custom Table Rows objects

You can create custom **Table Rows** objects to have methods specific to a Snowflake table. These objects can automatically populate request and response fields for methods within the custom object. To create a custom object:

1. Go to the **Edit Connector** page for the Snowflake connector.
2. Under the **Methods & Fields** heading, locate the **Table Rows** category and select it to expand.
3. Select the red **Copy this Category to create a Custom Object Category** icon.
4. Use the dropdown menu to select the Snowflake table name.
5. Select **Copy**.

</section>
<section class="card">

## Use last successful run date in a Table Rows > List Rows inline merge field

The **Where** parameter can normally include the `{{LastSuccessfulRunDate}}` inline merge field to include the last successful run date:

```sql
CREATED_AT > '{{LastSuccessfulRunDate}}'
```

Due to how the Snowflake API paginates data, you can't use the `{{LastSuccessfulRunDate}}` inline merge field in this way. To work around this, you can use the **Table Rows > List Rows** method in a cycle:
1. Select **Step setup**.
2. Set **Skip Pre-POST Request?** to `True`.
3. Set **Where** to `Ignore`.
4. Enter the following script:
   ```javascript
   function before_action() {
       prePostRequest();
       return true;
   }
   
   function prePostRequest() {
       if (!prePostRequestCalledTrue()) {
           setRole();
           method_request_headers.where = `CREATED_AT > '${last_successful_run_date}'`;
           handlePrePostRequest();
           setIndex();
           action_data.prePostRequestCalled = true;
       }
   }
   
   function prePostRequestCalledTrue() {
       return action_data != null && action_data.prePostRequestCalled != null && action_data.prePostRequestCalled === true;
   }
   ```
5. Update line 9 of the script with the appropriate where clause. `last_successful_run_date` can be used to include the last successful run date.
6. Start the cycle.

</section>
