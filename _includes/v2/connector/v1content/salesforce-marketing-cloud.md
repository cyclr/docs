
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Please refer to [this document](https://docs.cyclr.com/salesforce-connector) for a guide to authenticating Salesforce connectors.


</div>

</section>

<section class="userguide" markdown="1">

## User Guide

<div class="section-content" markdown="1">

### Upsert Custom Data Extension Rows

The Salesforce Marketing Cloud connector gives you have the ability to Upsert (create or update) a batch of data extension rows.

When using the method 'Upsert Custom Data Extension Rows', custom fields must be provided for both the request and response objects.

You can do this is one of two ways:

If you have a sample of the JSON that will be posted you can:

1. Click the magnifying glass icon

   ![monday dot com api token](./images/sf_marketing_cloud_1.png)

2. Paste in the sample JSON

   ![monday dot com api token](./images/sf_marketing_cloud_2.png)

3. Click 'Generate'

Or you can add the fields manually:

1. Click the plus icon

   ![monday dot com api token](./images/sf_marketing_cloud_3.png)

2. Enter the Field Location, Display Name, Data Type and (optionally) a Description

   ![monday dot com api token](./images/sf_marketing_cloud_4.png)

3. Click 'Create'

Your custom fields will be created. This process should be carried out for both the request and response fields.

![monday dot com api token](./images/sf_marketing_cloud_5.png)

**Important**

1. Your request object must include the property 'keys'. This is assigned an object containing the primary key you will be using to upsert the data

2. Your mappings must start with an array. This endpoint expects an array of objects, even if that array only contains one item

For example, if generating fields from sample JSON:

```json
Invalid - no keys property

{
  "values: {
    "FirstName": "John",
    "LastName": "Doe"
  }
}
```

```json
Invalid - no parent array

{
  "keys": {
    "EmailAddress": "test@test.com"
  },
  "values: {
    "FirstName": "John",
    "LastName": "Doe"
  }
}
```

```json
Valid - keys property and parent array

[
  {
    "keys": {
      "EmailAddress": "test@test.com"
    },
    "values: {
      "FirstName": "John",
      "LastName": "Doe"
    }
  }
]
```

If adding fields manually, for Field Location:

**Invalid** - no parent array

> keys.EmailAddress

**Valid** - property has parent array

> [].keys.EmailAddress


</div>

</section>
