---
title: Verint Engagement Data Management Authentication
sidebar: cyclr_sidebar
permalink: verint-engagement-data-management-connector
tags: [connector]
---

## Verint - Engagement Data Management Setup

### Requirements

To connect with Verint, you will need a **Username** and **Password**.
You will also need to know the **Domain** of the instance you would like to access.
If the link you would like to access is: https://odf4.verint.training/api/recording/textcapture/v1/ingestion
The **Domain** would be "odf4.verint.training".

## Cyclr setup
This section describes how to setup the connector in the console. No other setup is required.

### Console setup

To set up the Verint connector in Cyclr, go to your console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Verint Engagement Data Management connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | Value              | Description                                 |
   | :----------------- | :------------------------------------------ |
   | **Domain** | The domain of the application server or load balancer address. |
   | **Username** | The Username of the authorized user.                       |
   | **Password** | The Password of the authorized user.                       |

7. Select **Save**.

## Additional information
### Documentation

The API reference documentation can be found here:
https://connect.verint.com/developers/edm/w/api-reference/25356