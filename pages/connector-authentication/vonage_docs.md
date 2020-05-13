---
title: Vonage Connector Guide
sidebar: cyclr_sidebar
permalink: vonage-connector
tags: [connector]
---

# Setup

To pair the Vonage connector with a Vonage application you will need an **Application ID**, **Private Key**, **API Key** and **API Secret**.

## Vonage Credentials

Sign in to the Vonage dashboard [here](https://dashboard.nexmo.com/sign-in) if you already have an account. If not create one [here](https://dashboard.nexmo.com/sign-up).

### Application ID and Private Key

1. Select 'Your applications' from the left hand menu

   ![vonage dashboard](./images/vonage_dashboard_1.png)

2. Either select an existing application or create a new one

   ![vonage dashboard](./images/vonage_dashboard_2.png)

3. Your **Application ID** will be displayed, make a note of that and then click 'Edit'

   ![vonage dashboard](./images/vonage_dashboard_3.png)

4. Scroll down to where a Public Key is displayed. Click 'Generate public and private key'

   ![vonage dashboard](./images/vonage_dashboard_4.png)

5. The private key should download to your system

6. Make sure to scroll to the bottom of the page and click 'Save Changes'. Failure to do so will result in authorization errors when making calls to the Vonage API

   ![vonage dashboard](./images/vonage_dashboard_5.png)

7. Open the private key file. Copy all text **excluding** '-----BEGIN PRIVATE KEY-----' and '-----END PRIVATE KEY-----'. In this screenshot it would be lines 2 - 27

   ![vonage dashboard](./images/vonage_dashboard_6.png)

### API Key and API Secret

1. From your [account settings](https://dashboard.nexmo.com/settings) you will find your **API Key** and **API Secret**

   ![vonage dashboard](./images/vonage_dashboard_7.png)

## Connector Setup

1. Locate the Vonage connector

   > Cyclr Console > Connectors > Connector Library > Vonage

2. From the Edit Connector interface click 'Setup'

3. Enter your **Application ID**, **Private Key**, **API Key** and **API Secret**. Click 'Next'

The connector is now configured to interact with your Vonage application.

## User Guide

When retrieving the information associated with a phone number, using the 'Get Number Details' method, you have the option to retreive the contact name associated with that phone number. To do this set the **Cnam** query parameter to **true**.

> Note: The Cnam functionality is only applicable to US phone numbers.

![vonage dashboard](./images/vonage_dashboard_8.png)
