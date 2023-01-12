---
title: Bookeo Authentication
sidebar: cyclr_sidebar
permalink: bookeo-connector
tags: [connector]
---

<a name="bookeo-setup"></a>
# Bookeo setup

You need the following to set up the Bookeo connector in Cyclr:
-   A Bookeo application and the [secret key](#getting-a-secret-key) associated with it.
-   An [API key](#getting-an-api-key), generated when your Bookeo application is installed within a Bookeo account.

<a name="getting-a-secret-key"></a>
### Getting a secret key

You can find Bookeo's guide on how to register an application to get a secret key [here](https://www.bookeo.com/api/setup/) under the **Registering your application** section.

<a name="setting-permissions"></a>
### Setting permissions

Once you have created an application, use the **Authorisation URL** to allow clients to install your Bookeo application to their Bookeo account. The Cyclr Bookeo connector requires the following permissions to function: `customers_r_all`,`bookings_r_all`,`payments_r_all`. Multiple permissions should be entered as a comma separated list. An authorisation URL for a Bookeo application for Cyclr has the following format: `signin.bookeo.com/?authappid=XYZ&permissions=customers_r_all,bookings_r_all,payments_r_all`.

<a name="client-setup"></a>
# Client setup

<a name="getting-an-api-key"></a>
### Getting an API key

Clients install your Bookeo application to their account using the authorization URL obtained in the [previous section](#setting-permissions). You can find Bookeo's guide on how to get an API key [here](https://www.bookeo.com/api/setup/) under the **Obtaining user authorization for your application** section.

<a name="cyclr-setup"></a>
# Cyclr setup

<a name="console-setup"></a>
### Console setup

To set up your Bookeo connector within your Cyclr console:

1. Go to your **Cyclr Console**.
2. Select **Connectors** > **Application Connector Library** at the top of the page.
3. Use the search box to find the Bookeo connector.
4. Select the **Setup Required** icon.
5. Enter the below values, omitting this step will allow you to use different settings for each account on installation:
    | Value          | Description                                                         |
    | :------------- | :------------------------------------------------------------------ |
    | **Secret Key** | The [secret key](#getting-a-secret-key) of your Bookeo application. |
6. Select **Save Changes**.

<a name="account-setup"></a>
### Account setup

You will be asked for the following values when installing the Bookeo connector within an account:
| Value          | Description                                                                                                    |
| :------------- | :------------------------------------------------------------------------------------------------------------- |
| **API Key**    | The [API key](#getting-an-api-key) of your client's Bookeo account.                                            |
| **Secret Key** | The [secret key](#getting-a-secret-key) of your Bookeo application, if you did not enter this in step 5 above. |
