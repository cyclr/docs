---
title: Access CRM Connector Guide
sidebar: cyclr_sidebar
permalink: access-crm-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">

## Handle calculated fields

If you want to add calculated fields to the response mappings of any methods, end the **Field Location**'s name with `\_calc`. If your calculated field name doesn't include `\_calc`, the API throws an error because your calculated field doesn't exist on the object definition.

For example:

A field location of **myCalculatedField** results in a failed request.

A field location of **myCalculatedField_calc** results in a successful request.

</section>
