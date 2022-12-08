---
title: Cardpointe Authentication
sidebar: cyclr_sidebar
permalink: Cardpointe-connector
tags: [connector]
---

## Partner Setup

First, login to your existing Cardpointe account or [sign up for one.](https://cardpointe.com/account/registration#/registration)


#### Retrieving Login Details

*   [Login](https://accounts.cardconnect.com/auth/realms/cardconnect/protocol/openid-connect/auth?response_type=code&client_id=cardpointe&redirect_uri=https%3A%2F%2Fcardpointe.com%2Faccount%2Fsso%2Flogin&state=d5709227-41e8-4ae3-8a7d-41ec3bcd8536&login=true&scope=openid) to your Cardpointe Account.
*   You will need your Site URL to be able to interact with your data.

### Cyclr Setup

Setup your Cardpointe App within Cyclr:

*   Go to **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Cardpointe0**
*   Click the **Setup** button

Enter the following values:

**Domain**:  The Domain of the site you're integrating with.

**Username**:  The username that matches the Domain and MerchantID to make calls with.

**Password**:  The password that matches the Domain and MerchantID to make calls with.


The Cardpointe Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
