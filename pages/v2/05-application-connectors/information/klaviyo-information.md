---
title: Klaviyo information
sidebar: cyclr_sidebar
permalink: klaviyo-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Profile custom properties

Each Klaviyo profile can have custom properties associated with it. Within Cyclr, you can add additional method fields to create, update, or map custom properties. If you update a custom property that doesn't exist, Cyclr creates that property.

### Add Create Profile custom properties

1. Go to the **Edit Connector** page.
2. Under the **Methods & Fields** heading, go to **Profiles > Create Profile**.
3. Under the **Request Fields** heading, select the **+** button.
4. Enter the following values:

    | Value              | Description                                                  |
    | :----------------- | :----------------------------------------------------------- |
    | **Field Location** | The custom property name. Use the format `data.attributes.properties.{PropertyName}`. |
    | **Display Name**   | The display name of the custom property in the Cyclr UI. |
    | **Description**    | The description of the custom property in the Cyclr UI. |
    | **Data Type**      | The data type of the custom property. Set this to `Text`. |

5. Select **Create**.

### Add Update Profile custom properties

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

### Map Get Profile custom properties

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
