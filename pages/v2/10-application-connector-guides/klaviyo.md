---
title: Klaviyo Authentication
sidebar: cyclr_sidebar
permalink: klaviyo-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
## Klaviyo setup

To set up the Klaviyo connector in Cyclr you need a [private API key](#get-a-private-api-key) for your Klaviyo account.

<a href="get-a-private-api-key">

### Get a private API key

To see how to get a private API key, see [Klaviyo's guide](https://help.klaviyo.com/hc/en-us/articles/7423954176283). When you create a private API key, set **Select Access Level** to **Full Access Key** so the Klaviyo connector functions correctly within Cyclr.


</section>
<section class="card py-5 my-5">
## Cyclr account setup

When you install the Klaviyo connector in an account, Cyclr asks you for authentication details:

| Value               | Description                                                  |
| :------------------ | :----------------------------------------------------------- |
| **Private API Key** | The [private API key](#get-a-private-api-key) for your Klaviyo account. |


</section>
<section class="card py-5 my-5">
## Additional information

### Profile custom properties

Each Klaviyo profile can have custom properties associated with it. Within Cyclr, you can add additional method fields to create, update, or map custom properties. If you update a custom property that doesn't exist, it creates that property.

#### Add Create Profile custom properties

1. Go to the **Edit Connector** page.
2. Under the **Methods & Fields** heading, go to **Profiles > Create Profile**.
3. Under the **Request Fields** heading, select the **+** button.
4. Enter the following:

    | Value              | Description                                                  |
    | :----------------- | :----------------------------------------------------------- |
    | **Field Location** | The custom property name. Use the format `data.attributes.properties.{PropertyName}`. |
    | **Display Name**   | The display name of the custom property in the Cyclr UI. |
    | **Description**    | The description of the custom property in the Cyclr UI. |
    | **Data Type**      | The data type of the custom property. Set this to `Text`. |

5. Select **Create**.

#### Add Update Profile custom properties

1. Go to the **Edit Connector** page.
2. Under the **Methods & Fields** heading, go to **Profiles > Update Profile**.
3. Under the **Request Fields** heading, select the **+** button.
4. Enter the following:

    | Value              | Description                                                  |
    | :----------------- | :----------------------------------------------------------- |
    | **Field Location** | The custom property name. Use the format `{PropertyName}`. |
    | **Display Name**   | The display name of the custom property in the Cyclr UI. |
    | **Description**    | The description of the custom property in the Cyclr UI. |
    | **Data Type**      | The data type of the custom property. Set this to `Text`. |

5. Select **Create**.

#### Map Get Profile custom properties

1. Go to the **Edit Connector** page.
2. Under the **Methods & Fields** heading, go to **Profiles > Get Profile**.
3. Under the **Response Fields** heading, select the **+** button.
4. Enter the following:

    | Value              | Description                                                  |
    | :----------------- | :----------------------------------------------------------- |
    | **Field Location** | The custom property name. Use the format `{PropertyName}`. |
    | **Display Name**   | The display name of the custom property in the Cyclr UI. |
    | **Description**    | The description of the custom property in the Cyclr UI. |
    | **Data Type**      | The data type of the custom property. Set this to `Text`. |

5. Select **Create**.

</section>
