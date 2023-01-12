---
title: SMRT Connector Guide
sidebar: cyclr_sidebar
permalink: smrt-connector
tags: [connector]
---

## Authentication

To authenticate the SMRT connector you will need the name of your SMRT account and an API Key.

### Account Name

This is the account name as formatted in your smrtapp url. For example if your smrt account url was https://mycompany.smrtapp.com your account name for authentication purposes would be mycompany.

### API Key

To obtain your API Key, from the main menu go to:

1. **Reports**
2. From The KPI Dashboard click **KPI Config**
3. Click the **Categories** tab
4. Select **Orders**
5. Select any KPI report
6. Click the wrench button in the upper right corner
7. Click **Generate API Code**

A modal will appear with a sample cURL request. The long string after "Bearer" is your API Key.

![API Key](./images/smrt_auth.png)

### Connector Setup

1. Locate the SMRT connector

   > Cyclr Console > Connectors > Connector Library > SMRT

2. From the Edit Connector interface click 'Setup'

3. Enter your SMRT account name, click 'Next'

4. Enter your API Key, click 'Next'

The connector is now authenticated and ready to use.
