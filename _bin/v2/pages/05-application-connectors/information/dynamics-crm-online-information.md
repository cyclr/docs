---
title: Microsoft Dynamics
sidebar: cyclr_sidebar
permalink: dynamics-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">
## Additional Filter Condition

Some methods provide "Additional Filter Condition" field. This can be used to filter results. The full MS Dynamics documentation is [here](https://docs.microsoft.com/en-us/powerapps/developer/common-data-service/webapi/query-data-web-api#filter-results). 
e.g. "and myCustomBool eq true"
Warning: Ensure lowercase is used for the operators. i.e. AND will not work, and will work.

</section>
<section class="card">
## Additional Fields To Return
Some methods provide "Additional Fields To Return" field. This can be used to return addtional data. e.g. Add a custom response field to the method and add the custom field to Additional Fields To Return, to tell the API to return. If there is more than one field use "," seperator.

</section>
