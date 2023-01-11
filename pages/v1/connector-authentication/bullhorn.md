---
title: Bullhorn Authentication
sidebar: cyclr_sidebar
permalink: bullhorn-connector
tags: [connector]
---

# Bullhorn

## Partner Setup

To authenticate the Bullhorn connector you will need a Client ID and Client Secret.  If you do not already have these, you or a listed Account / Support Contact will need to get in touch with Bullhorn Support to have credentials set up.

If asked for a callback URI during this process, give

https://``Your Service Domain``/connector/callback 

Your service domain can be found in your Cyclr console under Settings > General Settings > Service Domain.

Once you have your Client ID and Secret, you will be able to use these details to authenticate the connector.

## FAQ

### Apache Tomcat Error

After you are redirected to Bullhorn during the authentication process, sometimes Bullhorn displays an Apache Tomcat error like this:

![Bullhorn Redirect Error](./images/bullhorn-redirect-error.png)

This is a known issue with Bullhorn. The solution is to clear the Bullhorn cookies in your browser, or open Cyclr and authenticate the connector in a private window.

## User Guide

### Retrieving Custom Objects

> Note: This currently only applies to the Job Order methods

To retrieve custom object fields with your Job Order requests the steps to do so are:

1. Find the fields of the custom object using the method Job Orders > Get Custom Object Fields

   ![Custom Object Fields](./images/bullhorn_cf_1.png)

2. Add the fields of the custom object to the desired method with the Field Location [data].**CustomObjectName**.[data].**FieldName** for List New Job Orders or List Updated Job Orders, or data.**CustomObjectName**.[data].**FieldName** for Get Job Order. For Example (with List New Job Orders):

   ![Add Custom Fields](./images/bullhorn_cf_2.png)
   
3. Add the custom object name and field names to the Custom Objects parameter when making the request. The format must be ObjectName(FieldName,FieldName,FieldName). For example:

   ![Add Query](./images/bullhorn_cf_3.png)
