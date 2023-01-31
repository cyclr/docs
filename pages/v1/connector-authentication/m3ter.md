---
title: M3ter Authentication
sidebar: cyclr_sidebar
permalink: m3ter-connector
tags: [connector]
---

# M3ter setup

You need to do the following to setup the M3ter connector:

1. Generate an API Key and Secret for a Service User
2. Get an organisation ID.

## Generate an API Key and Secret for a Service User

Please see M3ter's documentation on how to generate an API Key and Secret for a Service User [here](https://www.m3ter.com/docs/guides/authenticating-with-the-service/service-authentication#generating-an-api-key-and-secret-for-a-service-user).

## Get an organisation ID

Please see M3ter's documentation on how to get an organisation ID [here](https://www.m3ter.com/docs/guides/managing-organization-and-users/viewing-and-editing-organization#viewing-details-and-editing-configuration).

# Cyclr setup

## Console setup

To setup the M3ter connector within your Cyclr console:

1. Go to your **Cyclr Console**.

2. Select **Connectors** > **Application Connector Library** at the top of the page.

3. Use the search box to find the **M3ter** connector.

4. Select the **Setup Required** icon.

5. Enter the below values, omitting this step will allow you to use different settings for each account on installation:

   | Value             | Description                              |
   | :---------------- | :--------------------------------------- |
   | **Access Key ID** | The Access Key ID of your M3ter account. |
   | **API Secret**    | The API Secret of your M3ter account.    |

6. Select **Save Changes**.

## Account setup

You will be asked for the following values when installing the M3ter connector within an account:

| Value               | Description                                                  |
| :------------------ | :----------------------------------------------------------- |
| **Access Key ID**   | The Access Key ID of your M3ter account. If you did not enter this in step 5 above. |
| **API Secret**      | The API Secret of your M3ter account. If you did not enter this in step 5 above. |
| **Environment**     | The M3ter environment to use.                                |
| **Organisation ID** | The M3ter organization ID of  the organization to access.    |
