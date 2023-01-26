---
title: Salesforce Marketing Cloud information
sidebar: cyclr_sidebar
permalink: salesforce-marketing-cloud-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Upsert custom data extension rows

The Salesforce Marketing Cloud connector gives you have the ability to Upsert (create or update) a batch of data extension rows. When you use the **Upsert Custom Data Extension Rows** method, you need to provide custom fields for both the request and response objects.

You can provide custom fields either manually or with JSON script.

If you have a sample of the JSON that you want to post, you can generate the fields:

1. Select the magnifying glass icon.

   ![monday dot com api token](./images/sf_marketing_cloud_1.png)

2. Paste in the sample JSON.

   ![monday dot com api token](./images/sf_marketing_cloud_2.png)

3. Select **Generate**.

You can also add the fields manually:

1. Select the plus icon.

   ![monday dot com api token](./images/sf_marketing_cloud_3.png)

2. Enter the **Field Location**, **Display Name**, **Data Type** and, optionally, a **Description**.

   ![monday dot com api token](./images/sf_marketing_cloud_4.png)

3. Select **Create**.


> **Note**: You need to create fields for both the request and response fields.

![monday dot com api token](./images/sf_marketing_cloud_5.png)

### Request object requirements

* You need to include the property `keys` in your request object. Assign the property `keys` an object containing the primary key that you use to upsert the data.
* You need to start your mappings with an array. The endpoint expects an array of objects, even if the array only contains one item.

For example, if you generate fields from sample JSON:

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

If you add the fields manually, for `Field Location`:

**Invalid** - no parent array

> keys.EmailAddress

**Valid** - property has parent array

> [].keys.EmailAddress

</section>
