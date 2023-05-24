---
title: EposNow Authentication
sidebar: cyclr_sidebar
permalink: eposnow-connector
tags: [connector]
---

<a name="eposnow-set-up"></a>

# EposNow set up

You need the following information to set up the EposNow connector in Cyclr:

- The [Epos Key ID and Epos Secret](#getting-the-client-id-and-client-secret)
  obtained by [creating an API Device](#create-an-api-device) in Epos Now.

<a name="create-an-api-device"></a>

### Create an API Device

You need to
[create an API Device](https://developer.eposnowhq.com/Setup/APISetup) to
[get the Epos Key and Epos secret](#getting-the-epos-key-and-epos-secret). You
can find EposNow's guide on creating an API Device in the Epos Now console
[here](https://developer.eposnowhq.com/Setup/APISetup).

**Note**: Each account has a limit on the number of API requests it can make.
When the number of requests exceeds this limit the API will return
`API Limit Exceeded` for any request. Check or update your EposNow API limits on
the API page found in the
[**Web Integrations**](https://developer.eposnowhq.com/Setup/ApiDevice) menu on
the EposNowHQ Backoffice.

<a name="getting-the-epos-key-and-epos-secret"></a>

### Getting the Epos ID and Epos Secret

You need a Epos Key and Epos Secret to authenticate the EposNow connector in
Cyclr. Before you can get these you need to
[create an API Device](https://developer.eposnowhq.com/Setup/APISetup). You can
find Epos Now's guide on getting the Epos Key and Epos Secret in the EposNow
console [here](https://developer.eposnowhq.com/Setup/ApiDevice).

# Cyclr set up

<a name="console-setup"></a>

### Console setup

To set up your EposNow connector within your Cyclr console:

1. Go to your **Cyclr Console**.
2. Select **Connectors** > **Custom Connectors** at the top of the page.
3. Use the search box to find the EposNow connector.
4. Select the **Setup Required** icon.
5. Enter the below values, omitting this step will allow you to use different
   settings for each account on installation:
   - **Username**: The [Epos Key](#getting-the-epos-key-and-epos-secret) of your
     EposNow account.
   - **Password**: The [Epos Secret](#getting-the-epos-key-and-epos-secret) of
     your EposNow account.
6. Select **Save Changes**.

Your EposNow connector is now set up! You can test it by installing it to a
Cyclr account and then executing one of the methods to confirm it returns data.
