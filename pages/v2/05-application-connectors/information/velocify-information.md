---
title: Velocify information
sidebar: cyclr_sidebar
permalink: authenticate-velocify-information
tags: [connector-information]

linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Create Leads in Velocify

To create leads using the Velocify connector, you need to do the following steps:

1. Find and run the **List Fields** method to get an XML object containing all the fields that you can use.
2. Note the details of the fields you want to use in the **Create Lead** method.
3. In connector testing, add the fields you want to use to the connector in the following format: `soapenv:Envelope.Field_ID_{FieldId}`. For example, if the First Name field has an ID of 1 then the **Field Location** you need is `soapenv:Envelope.Field_ID_1` and you can set the **Display Name** to `First Name`.
![](./images/velocify_custom_field.png)
4. Repeat step 3 for every field you want to access, and then you can create fields.

</section>
