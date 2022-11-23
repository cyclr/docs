---
title: Klaviyo Authentication
sidebar: cyclr_sidebar
permalink: klaviyo-connector
tags: [connector]
---

## Klaviyo setup

To set up the Klaviyo connector in Cyclr you need a [private API key](#get-a-private-api-key) for your Klaviyo account.

<a href="get-a-private-api-key">

### Get a private API key

You can find Klaviyo's guide on how to get a private API key [here](https://help.klaviyo.com/hc/en-us/articles/7423954176283). When you create a private API key, **Select Access Level** must be set to **Full Access Key** for the Klaviyo connector to function correctly within Cyclr.

## Cyclr account setup

When you install the Klaviyo connector in an account you will be asked for:

| Value               | Description                                                  |
| :------------------ | :----------------------------------------------------------- |
| **Private API Key** | The [private API key](#get-a-private-api-key) for your Klaviyo account. |

## Additional information

### Profile custom properties

Each Klaviyo profile can have custom properties associated with it. Within Cyclr, you can add additional method fields to create, update, or map custom properties. If you update a custom property that does not exist it will be created.

#### Add Create Profile custom properties

1. Go to the **Edit Connector** page.
2. Under the **Methods & Fields** heading, go to **Profiles > Create Profile**.
3. Under the **Request Fields** heading, select the **+** button.
4. Enter the following:

    | Value              | Description                                                  |
    | :----------------- | :----------------------------------------------------------- |
    | **Field Location** | The custom property name. This must have the format `data.attributes.properties.{PropertyName}`. |
    | **Display Name**   | The display name of the custom property within the Cyclr UI. |
    | **Description**    | The description of the custom property within the Cyclr UI. |
    | **Data Type**      | The data type of the custom property. This should be set to `Text`. |

5. Select **Create**.

#### Add Update Profile custom properties

1. Go to the **Edit Connector** page.
2. Under the **Methods & Fields** heading, go to **Profiles > Update Profile**.
3. Under the **Request Fields** heading, select the **+** button.
4. Enter the following:

    | Value              | Description                                                  |
    | :----------------- | :----------------------------------------------------------- |
    | **Field Location** | The custom property name. This must have the format `{PropertyName}`. |
    | **Display Name**   | The display name of the custom property within the Cyclr UI. |
    | **Description**    | The description of the custom property within the Cyclr UI. |
    | **Data Type**      | The data type of the custom property. This should be set to `Text`. |

5. Select **Create**.

#### Map Get Profile custom properties

1. Go to the **Edit Connector** page.
2. Under the **Methods & Fields** heading, go to **Profiles > Get Profile**.
3. Under the **Response Fields** heading, select the **+** button.
4. Enter the following:

    | Value              | Description                                                  |
    | :----------------- | :----------------------------------------------------------- |
    | **Field Location** | The custom property name. This must have the format `{PropertyName}`. |
    | **Display Name**   | The display name of the custom property within the Cyclr UI. |
    | **Description**    | The description of the custom property within the Cyclr UI. |
    | **Data Type**      | The data type of the custom property. This should be set to `Text`. |

5. Select **Create**.
