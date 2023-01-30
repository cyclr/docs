---
title: Access CRM Connector Guide
sidebar: cyclr_sidebar
permalink: access-crm-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Setup

To authenticate the Access CRM connector you will need an API key and Integrator Key. Both are supplied by Access. Please contact your Access account manager to be issued these credentials.

### Connector Setup

1. Locate the Access CRM connector

   > Cyclr Console > Connectors > Connector Library > Access CRM

2. From the Edit Connector interface click 'Setup'

3. Enter your Integrator Key, click 'Next'

4. Enter your API Key, click 'Next'

The connector is now authenticated and ready to use.


</section>
<section class="card">
## Additional information

### Handling Calculated Fields

If you wish to add calculated fields to the response mappings of any methods you must end the Field Location's name with "\_calc" (underscore calc). If your calculated field name does not include "\_calc" the API will throw an error, as your calculated field does not exist on the object definition.

For example:

A field location of **myCalculatedField** will result in a failed request.

A field location of **myCalculatedField_calc** will result in a successful request.

</section>
