
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Less Annoying CRM authentication requires:
- User Code
- API Key

See the [API guide](https://www.lessannoyingcrm.com/help/topic/api_getting_started/Generating_API_Token) for more information.


1. [Log in](https://www.lessannoyingcrm.com/login/) to an existing account or [sign up](https://www.lessannoyingcrm.com/Signup)
2. Go to the [API Settings](https://www.lessannoyingcrm.com/app/settings/api) page
3. Note your `User Code` and `API Token` shown at the top of the page
4. Click **Generate a new API Token** if  `User Code` and `API Token` are not shown

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

1. Find the Less Annoying CRM connector

   > **Cyclr Console** > **Connectors** > **Connector Library** > **Less Annoying CRM**

2. From the Edit Connector interface click **Setup**

3. Enter your `User Code` and click **Next**

4. In the `API Key` field enter your `API Token` and click **'Next**

The connector is now authenticated and ready to use.

</div>

</section>

<section class="userguide" markdown="1">

## User Guide

<div class="section-content" markdown="1">

These Pipeline methods provice access to our lookup feature for each of the request fields:
- List
- List New
- List Updated

![lookup feature](./images/less_annoying_crm_1.png)

![lookup feature](./images/less_annoying_crm_2.png)

Pipeline ID is the only required field.  

The request can optionally be filtered by Status and User ID.

</div>

</section>
