
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

To authenticate the OpenCRM connector you will need an **API Key**, **Pass Key** and your OpenCRM account name.

### API Key and Pass Key

These credentials should be issued by OpenCRM's support team or your OpenCRM account manager. Please contact support@opencrm.co.uk for more information.

### OpenCRM Account

This is your account name as it appears in the url when logged into OpenCRM. 

For example if the url is `https://mycompany.opencrm.co.uk` your account name for the API purposes is **mycompany**.

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

- Go to your **Cyclr Console**
- Click the **Connectors** menu along the top
- Choose **Connector Library*
- Search for OpenCRM
- Click the **Setup** button
- Enter your `Pass Key`and `OpenCRM account name`
- Click **Next**
- Enter your `API Key`
- Click **Next**

The connector is now authenticated and ready to use.

</div>

</section>

<section class="userguide" markdown="1">

## User Guide

<div class="section-content" markdown="1">

## Adding Custom Fields

Your records may contain custom fields which by standard are not mapped each method's request or response fields. The API field names for custom fields can be found in your custom field settings within OpenCRM. An example of a custom field API field name is "cf_123".

Once you have identified the custom field you want to add mappings for these can be added following the steps from this guide: https://docs.cyclr.com/adding-custom-fields

Most importantly, the API field name is what should be provided for the Field Location of the custom field.

The format varies slightly depending on whether the field is for a singular or plural method. ie. Get Contact or List Contacts.

| Method Name           | Response/Request Field | Field Location           | Example   |
| :-------------------- | :--------------------- | :----------------------- | :-------- |
| Upsert Contact        | Request                | <em>APIFieldName</em>    | cf_123    |
| Get Contact           | Response               | <em>APIFieldName</em>    | cf_123    |
| List Contacts         | Response               | [].<em>APIFieldName</em> | [].cf_123 |
| List New Contacts     | Response               | [].<em>APIFieldName</em> | [].cf_123 |
| List Updated Contacts | Response               | [].<em>APIFieldName</em> | [].cf_123 |

</div>

</section>

