---
title: Trustpilot Connector Guide
sidebar: cyclr_sidebar
permalink: trustpilot-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Creating An App

Follow the steps outlined in [this guide](https://support.trustpilot.com/hc/en-us/articles/207309867-Getting-started-with-Trustpilot-s-APIs#create-manage-applications-3) to create an application in the Trustpilot console.

> The redirect URI should be https://{service domain}/connector/callback. Your service domain can be found in your Cyclr console under Settings > General Settings > Service Domain.


</section>
<section class="card">
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


</section>
