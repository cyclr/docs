---
title: Less Annoying CRM Connector Guide
sidebar: cyclr_sidebar
permalink: less-annoying-crm-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Connector Setup

### Obtaining Authentication Credentials

The Less Annoying CRM connector is authenticated with a User Code and an API Key. A guide to obtain these values is detailed [here](https://www.lessannoyingcrm.com/help/topic/api_getting_started/Generating_API_Token).

To summarize:

1. If you have an account with Less Annoying CRM, [log in](https://www.lessannoyingcrm.com/login/). If not, [sign up](https://www.lessannoyingcrm.com/Signup) for an account

2. At the top of [this](https://www.lessannoyingcrm.com/app/settings/api) page you should find your User Code and API Token. If these do not yet exist click "Generate a new API Token"

### Authenticate The Connector

1. Locate the Less Annoying CRM connector

   > Cyclr Console > Connectors > Connector Library > Less Annoying CRM

2. From the Edit Connector interface click 'Setup'

3. Enter your User Code and click 'Next'

4. In the API Key field enter your API Token and click 'Next'.

The connector is now authenticated and ready to use.

</section>
<section class="card">

## Additional information

Within the three Pipeline methods (List, List New and List Updated) you have access to our lookup feature for each of the request fields.

![lookup feature](./images/less_annoying_crm_1.png)

![lookup feature](./images/less_annoying_crm_2.png)

Pipeline ID is the only required field but the request can optionally be filtered by Status and User ID.

</section>
