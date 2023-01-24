---
title: Access CRM Connector Guide
sidebar: cyclr_sidebar
permalink: access-crm-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

### Handling Calculated Fields

If you wish to add calculated fields to the response mappings of any methods you must end the Field Location's name with "\_calc" (underscore calc). If your calculated field name does not include "\_calc" the API will throw an error, as your calculated field does not exist on the object definition.

For example:

A field location of **myCalculatedField** will result in a failed request.

A field location of **myCalculatedField_calc** will result in a successful request.

</section>
