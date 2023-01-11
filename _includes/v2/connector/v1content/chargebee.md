
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

### Setting up your Account

To authenticate the connector you need your Chargebee [Domain name](https://www.chargebee.com/docs/2.0/sites-intro.html) and [API Key](https://www.chargebee.com/docs/2.0/api_keys.html).

You will obtain your Domain name once you've signed up to Chargebee. A "Complete Account Setup" email will be sent to your email ID. Click the link in the email to setup your password and domain name.

On your Chargebee site, go to 'Settings' > 'Configure Chargebee' > 'API Keys and Webhooks' > 'API Keys'. Any existing API keys are listed.

For further information setting up API Keys, see the [Official Chargebee documentation](https://www.chargebee.com/docs/2.0/api_keys.html).

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Setup your Chargebee connector within Cyclr:

- Go to your **Cyclr Console**
- Click the **Connectors** menu along the top
- Choose Connector Library
- Scroll down to **Chargebee**
- Click the **Setup** button

Enter the following values:

> **Chargebee Site**: Your [Chargebee Domain](https://www.chargebee.com/docs/2.0/sites-intro.html).
>
> **Username**: Your [API Key](https://www.chargebee.com/docs/2.0/api_keys.html).

Your Chargebee Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</div>

</section>

<section class="userguide" markdown="1">

## User Guide

<div class="section-content" markdown="1">

### Configuring Custom Fields

To setup custom fields within Chargebee use the steps below, you can find the official Chargebee documentation [here](https://www.chargebee.com/docs/2.0/custom_fields.html).

### Setup your Custom Fields within Chargebee:

1. Go to your **Chargebee Site**
2. Click **Settings** in the left side menu
3. Choose **Configue Chargebee**
4. Scroll down and click on **Custom fields**
   1. Choose where to create the Custom fields by selecting the drop down button in the top left **e.g Customer, Subscriptions...**
   2. Select the **field type** and fill in the details in the field creation screen that appears.
      **Field Label**: Text that will appear on the UI for hosted pages and invoices.
      **API Name**: Field reference for API calls and merges.

The custom fields are considered 'active', and will now be available only on the test site. You need to publish the fields to your live site to include custom field information in the invoices that you send to your customers, or in the hosted pages viewed by them. Ensure that you check how the fields work for all your use cases before pushing it to your live site.

### Publish Custom Field to Live Site within Chargebee:

1. In the **Custom Fields main page**, click Publish to Live and confirm changes.
2. The custom fields will now be available on your **LIVE** site.

If you're using In-app Checkout, navigate to **Settings > Configure Chargebee > Custom Fields** to make further changes in the **LIVE** site.

### Manually Adding Custom Fields within Cyclr:

To setup custom fields within Cyclr use the steps below, you can find the official Cyclr documentation [here](https://docs.cyclr.com/adding-custom-fields#example-field-locations).

Make sure to add these fields to all required methods e.g GET & UPDATE.

1. From the builder's sidebar, click to expand the app connector and click Settings

2. In the section named Methods and Fields, click to expand the category and then the method you wish to add fields to

3. Under Request Fields or Response Fields (depending on whether you're sending or receiving the field), click the + button to add a field

4. The following needs to be specified:
   - **Field Location** - These need to be named exactly the same as in ChargeBee, with the format "`API_Name`" e.g. "cf_plan_id".
   - **Display Name** - This is the "friendly" name as it will be shown in the user interface.
   - **Description** - You can optionally describe the field and provide documentation, for example how it is used.
   - **Data Type** - You can optionally define a data type for your field. If it is datetime then add the subtype to allow for type conversions between different standards.
   ![Custom fields guide](https://docs.cyclr.com/images/connector-custom-field.gif)
   **Field type, Data Types**
   - Single line text: 'Text' (maximum character limit is 99).
   - Multiline text: 'Text' (maximum character limit is 250).
   - Dropdown: 'Text'
   - Checkbox: 'Boolean'
   - URL: 'Text'
   - Email: 'Text'
   - Date picker: 'DateTime' subtype: 'yyyy-MM-dd'
   - Timestamp: 'DateTime' subtype: 'unix'
   - Numbers: 'Integer'

Your Custom fields are now setup!

### Configuring Meta Data

For more information on Meta Data, you can find the official Chargebee documentation [here](https://www.chargebee.com/docs/2.0/metadata.html).

#### Manually Adding Meta Data Custom Fields within Cyclr:

To setup Meta Data custom fields within Cyclr use the steps below, you can find the official Cyclr documentation [here](https://docs.cyclr.com/adding-custom-fields#example-field-locations).

Make sure to add these fields to all required methods e.g GET & UPDATE.

1. From the builder's sidebar, click to expand the app connector and click Settings

2. In the section named Methods and Fields, click to expand the category and then the method you wish to add fields to

3. Under Request Fields or Response Fields (depending on whether you're sending or receiving the field), click the + button to add a field

4. The following needs to be specified:

   - **Field Location** - Needs to be in this format "meta_data.`key`". This supports nested objects.
   - **Display Name** - This is the "friendly" name as it will be shown in the user interface.
   - **Description** - You can optionally describe the field and provide documentation, for example how it is used.
   - **Data Type** - You can optionally define a data type for your field. If it is datetime then add the subtype to allow for type conversions between different standards.

Your Meta Data Custom fields are now setup!


</div>

</section>

