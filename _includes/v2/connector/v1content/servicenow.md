
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

> Note: Before authenticating either of the ServiceNow connectors you must first obtain a **Personal Developer Instance** within ServiceNow. Details on how to do so can be found [here](https://developer.servicenow.com/dev.do#!/learn/learning-plans/orlando/technology_partner_program/app_store_learnv2_buildmyfirstapp_orlando_personal_developer_instances).

### Authentication Credentials

The authentication process for both connectors is largely the same.

To authenticate the ServiceNow connector you will need:

- **ServiceNow Instance** - Your ServiceNow Instance (eg. https://<span>{Instance}.service-now</span>.com/)
- **Username** - Your ServiceNow Instance Username
- **Password** - Your ServiceNow Instance Password

To authenticate the ServiceNow Table API connector you will need the above credentials with the addition of:

- **Table Name** - The name of the table you will be interacting with. This can be found by going to **System Definition** > **Tables** from your ServiceNow instance's dashboard

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

1. Locate the ServiceNow or ServiceNow Table API connector

   > Cyclr Console > Connectors > Connector Library > ServiceNow
   
   > Cyclr Console > Connectors > Connector Library > ServiceNow Table API

2. From the Edit Connector interface click 'Setup'

3. Follow the onscreen prompts to enter your authentication credentials

> Note: A separate instance of the ServiceNow Table API connector should be installed for each table you want to interact with.

</div>

</section>

<section class="userguide" markdown="1">

## User Guide

<div class="section-content" markdown="1">

There are currently two ServiceNow connectors available:

- **ServiceNow** : Provides access to various ServiceNow API's
- **ServiceNow Table API** : Provides full CRUD functionality for a ServiceNow table via the ServiceNow Table API

</div>

</section>

