---
title: BigCommerce Authentication
sidebar: cyclr_sidebar
permalink: bigcommerce-connector
tags: [connector]

---

# BigCommerce setup

You will need to create a store API account. Please see BigCommerce's documentation on how to obtain store API credentials [here](https://support.bigcommerce.com/s/article/Store-API-Accounts?language=en_US#creating).

# Cyclr setup

## Console setup

To setup the BigCommerce connector within your Cyclr console:

1. Go to your **Cyclr Console**.

2. Select **Connectors** > **Application Connector Library** at the top of the page.

3. Use the search box to find the **BigCommerce** connector.

4. Select the **Setup Required** icon.

5. Enter the below values, omitting this step will allow you to use different settings for each account on installation:

   | Value            | Description                                                  |
   | :--------------- | :----------------------------------------------------------- |
   | **Access Token** | The Access token of your BigCommerce account. Obtained by creating an API account or installing an app in a BigCommerce control panel. |
   | **Base URL**     | The Base URL of the API instance.                            |
   | **Store Hash**   | The store hash value.                                        |

6. Select **Save Changes**.

## Account setup

You will be asked for the following values when installing the BigCommerce connector within an account:

| Value            | Description                                                  |
| :--------------- | :----------------------------------------------------------- |
| **Access Token** | The Access token of your BigCommerce account. If you did not enter this in step 5 above. |
| **Base URL**     | The Base URL of the API instance. If you did not enter this in step 5 above. |
