---
title: JotForm Connector Guide
sidebar: cyclr_sidebar
permalink: jotform-connector
tags: [connector]
---

## Setup

To authenticate the JotForm connector you will need an API Key and the API Domain.

### API Key

To obtain your API Key, within JotForm:

1. Navigate to **(icon in top-right corner) > Settings > API > API KEYS**

2. If there is not already a key present, click 'Create New Key'

3. The permissions should be set to 'Full Access'

### API Domain

This is the API Domain you would like to use. For example, "api.jotform.com" for US and "eu-api.jotform.com" for EU. Custom domains are also supported.

To find out which server your JotForm account uses:

1. Navigate to **(icon in top-right corner) > Settings > Data**

2. If the "Europe Datacenter" box is checked your account uses the EU server. If it's unchecked your account uses the non-EU (US) server.

### File Access

In order to download files using the connector you must disable one of the privacy settings in JotForm as follows:

1. Navigate to **(icon in top-right corner) > Settings**

2. Scroll down to the 'Privacy' category of checkboxes

3. Make sure the 'Require log-in to view uploaded files' checkbox is **not selected**

### Connector Setup

1. Locate the JotForm connector

   > Cyclr Console > Connectors > Connector Library > JotForm

2. From the Edit Connector interface click 'Setup'

3. Enter your API Domain (api.jotform.com for US, eu-api.jotform.com for EU or you can enter a custom URL)

4. Click 'Next'

5. Enter your API Key

6. Click 'Next'

The connector is now authenticated and ready to use.
