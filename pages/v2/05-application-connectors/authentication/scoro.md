---
title: Scoro Authentication
sidebar: cyclr_sidebar
permalink: scoro-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Partner Setup

First, login to your existing Scoro account, or sign-up for a free 14 day trial.

A note about methods that need specific authentication:

Methods in the following categories will need an API key to function:
*  Properties
*  Meters
*  Readings
*  Price Lists
*  Product Groups
*  Depot

Methods in these categories will need User Auth to function:
*  Bookmarks
*  Search
*  Webhooks

#### Retrieving User Auth Details

*   Log into the Scoro account
*   Click **Profile Settings** under your user profile in the top right
*   Click **Integrations** under the **Site Settings** category
*   At the bottom, under "General", click **Scoro API**. Make sure it is activated.
*   Make a note of the **"company_account_id"**.
*   If you are going to use the API key methods, make a note of the **API Key** under the **API KEY** header.

### Cyclr Setup

Setup your Scoro App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Scoro**
*   Click the **Setup** button

Enter the following values:

**Language**:  The language that you would like the data to be represented in. Default is set as "eng" for English.

**Company Name**: The name of your Scoro company. This can be found by reading the URL of your Scoro account. It is the part after "https://" and before ".scoro.com". For example, if your account URL was "https://companyName.scoro"

**Company Account ID**: This is the **company_account_id** that was retrieved from the integrations area in the previous step.

#### User Auth:

**Username**: The username that you use to login to your Scoro website.

**Password**: The password that you use to login to your Scoro website.

**Device Type**: The type of device you are using. For example, if you are using a computer, you could enter "computer".

**Device Name**: The device name you are using.

**Device ID**: The device ID that you are using.

#### API Key:

**API Key**: Enter the **API Key** that was retrieved from the integrations area in the previous step.

Your Scoro Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</section>
