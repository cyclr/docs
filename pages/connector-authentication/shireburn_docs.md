---
title: Shireburn Connector Guide
sidebar: cyclr_sidebar
permalink: shireburn-connector
tags: [connector]
---

## API Keys

The Shireburn connector is authenticated with two API Keys.

### Open API Key

To obtain an Open API Key you must first create a user account and assign that user the relevant permissions. The steps necessary to do this are described [here](http://indigohelp.shireburn.com/en/articles/3203157-how-to-obtain-an-open-api-key-in-indigo-beta).

### Azure API Key

To obtain your Azure API Key you must first create a developer account and subscribe to the 'Payroll Standard' product.
The steps necessary to do this are described [here](http://indigohelp.shireburn.com/en/articles/3203147-create-your-indigo-api-developer-account-and-subscribe-to-a-product-beta).

Once the state of your Payroll Standard subscription changes to 'Active' you will see a 'Primary Key'. This is your Azure API Key.

> It can take several hours for your subscription to be activated. If necessary contact Shireburn support for assistance.

## Authenticate The Connector

1. Locate the Shireburn connector

   > Cyclr Console > Connectors > Connector Library > Shireburn

2. From the Edit Connector interface click 'Setup'

3. Enter your Azure API Key (Primary Key) and click 'Next'

4. Enter your API Key (Open API Key) and click 'Next'

The connector is now authenticated and ready to use.

## User Guide

### Company & Employee Codes

Company and/or Employee codes are a required field throughout most methods in the Shireburn connector.

Company codes can be located as follows:

1. Login to Shireburn [here](https://indigo.shireburn.com/)

2. From the menu on the left of the page click 'Administration'

   ![shireburn interface](./images/shireburn_portal_1.png)

3. Click 'Companies'

   ![shireburn interface](./images/shireburn_portal_2.png)

4. Your company code/s will be displayed on the next page

   ![shireburn interface](./images/shireburn_portal_3.png)

Employee codes can be located as follows:

1. Login to Shireburn [here](https://indigo.shireburn.com/)

2. From the menu on the left of the page click 'Payroll'

   ![shireburn interface](./images/shireburn_portal_4.png)

3. Click 'Employees'

   ![shireburn interface](./images/shireburn_portal_5.png)

4. Your employee code/s will be displayed on the next page

   ![shireburn interface](./images/shireburn_portal_6.png)

Alternatively several methods within the connector will retrieve your employees' details, including their codes.
