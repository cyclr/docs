---
title: Trustpilot Connector Guide
sidebar: cyclr_sidebar
permalink: trustpilot-connector
tags: [connector]
---

## Creating An App

Follow the steps outlined in [this guide](https://support.trustpilot.com/hc/en-us/articles/207309867-Getting-started-with-Trustpilot-s-APIs#create-manage-applications-3) to create an application in the Trustpilot console.

> The redirect URI should be https://{service domain}/connector/callback. Your service domain can be found in your Cyclr console under Settings > General Settings > Service Domain.

## Authentication

1. In your Cyclr console, go to 'My Connectors' from the top right drop down menu.

   ![connector setup](./trustpilot_1.png)

2. From your connector list 'Edit connector' for Trustpilot.

   ![connector setup](./trustpilot_2.png)

3. From the Edit Connector page click 'Setup' where you will be prompted to enter the following details:

   | Name          | Description                            |
   | ------------- | -------------------------------------- |
   | Client ID     | Your Trustpilot applications 'API Key' |
   | Client Secret | Your Trustpilot applications 'Secret'  |
   | Username      | Your Trustpilot Username               |
   | Password      | Your Trustpilot Password               |

4. Click 'Next'.

The connector is now authenticated and ready to use.

## User guide

You will need a 'Business Unit ID' for most requests, without it you will receive a '403 - Forbidden' response. The recommended way of obtaining that is by using the 'Search For Business Units' method as the first step in your cycles.

It is worth noting that some endpoints are classified as Private by Trustpilot. This means that the logged in user must have permissions to access that Business Unit ID's data. If the logged in user does not have those permissions you will receive a '403 - Forbidden' response.
