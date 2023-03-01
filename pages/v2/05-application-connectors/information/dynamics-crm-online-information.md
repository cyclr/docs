---
title: Microsoft Dynamics information
sidebar: cyclr_sidebar
permalink: dynamics-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">
## Additional Filter Condition

Some methods provide the **Additional Filter Condition** field, which you can use to filter results. For more information, view the full [MS Dynamics documentation](https://docs.microsoft.com/en-us/powerapps/developer/common-data-service/webapi/query-data-web-api#filter-results). 

For example, you can use operators:

`and myCustomBool eq true`

> **Note**: Use lowercase for the operators: `AND` doesn't work.

</section>
<section class="card">

## Additional Fields To Return

Some methods provide the **Additional Fields To Return** field, which you can use to return addtional data. For example, to tell the API to return a custom response field, add the custom field to **Additional Fields To Return**. If you want to add more than one field, use a comma separated list.

</section>
