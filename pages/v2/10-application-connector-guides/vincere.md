---
title: Vincere Connector Guide
sidebar: cyclr_sidebar
permalink: vincere-connector
tags: [connector]
---

Vincere Setup
---------------

For Cyclr to connect with the Vincere API you will need to select a suitable user account within Vincere. This account will require setting up, the steps to complete this are below.

_NOTE: We have experienced issues when using the Safari web browser so would recommend using another browser._

1. Login to the Vincere Application using the account specific URL, e.g. {%raw%}https://{{yourdomain}}.vincere.io/loginForm.do{%endraw%}
2. Select Settings > Marketplace
3. Select the API Tab
4. Click "Create new token" button, this will display the API Key
5. Click "Create new Client ID" button, this will display the Client ID
6. Enter the callback URL using your Cyclr Partner's **Service Domain** into the "Callback URL" field, e.g. <br /> {% raw %}https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback{% endraw %}. <br /> Your Service Domain can be found in your Cyclr Partner Console under Settings > General Settings > Service Domain.


Connector Setup
---------------

The Connector now can be installed using the credentials obtained in the above steps:

**Client ID**: _Vincere Client ID_

**Secret**: _Leave this blank_

**Domain**:  _yourdomain_ (see your URL when accessing Vincere, {%raw%}https://{{yourdomain}}.vincere.io{%endraw%})

**API Key**: _Vincere API Key_


Using Custom Fields
-------------------

When using custom fields, the mapping of the Field Location will vary based on the custom field's "type".

For example when using Candidate custom fields:

1. Run the method "Get Candidate Custom Fields" to list the available custom fields
2. Pay close attention to the "Key" and "Type" fields in the response

If we now want to add a custom field to "Get Candidate" the Field Location, depending on the custom field's type, would be as follows:

| Custom Field Type  | Field Location                                | Example                |
| :----------------- | :-------------------------------------------- | :--------------------- |
| TEXT_BOX           | The custom field's Key                        | 12345678901234567890   |
| TEXT_AREA          | The custom field's Key                        | 12345678901234567890   |
| CHECK_BOX          | The custom field's Key within square brackets | [09876543210987654321] |
| SELECT_BOX         | The custom field's Key within square brackets | [09876543210987654321] |
| RADIO              | The custom field's Key within square brackets | [09876543210987654321] |
| MULTIPLE_SELECTION | The custom field's Key within square brackets | [09876543210987654321] |

   ![custom fields for get methods](./images/vincere_custom_fields_1.png)

When using List methods such as "List New Candidate Records", make sure to include the correct parent array. For example **[items]**.

   ![custom fields for list methods](./images/vincere_custom_fields_2.png)
   
A guide for adding custom fields to a method can be found [here](https://docs.cyclr.com/adding-custom-fields).
