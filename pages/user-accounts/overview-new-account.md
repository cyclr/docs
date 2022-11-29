---
title: Overview
sidebar: cyclr_sidebar
permalink: overview-new-account
tags: 
---

This article gives an overview on setting up a new Cyclr Account using the Cyclr API.

Useful links:
* [Cyclr Concepts article](./cyclr-concepts) for an explanation of some of the terms used here.
* [Cyclr **Interactive API Reference** links](./testing-cyclr-api) for all available endpoints.  Also enables you to make calls.


### Accessing Cyclr's API

To make calls to the Cyclr API, you'll need to identify your **Cyclr Instance**, then make an API call to obtain an **Access Token**.

* [Identify your Cyclr Instance](./testing-cyclr-api) - find the appropriate **API Domain** to use in your API calls.
* [Get an Access Token](./cyclr-api-authentication)



### Creating an Account

Typically, each of your own clients will have their own Cyclr Account to store their data and integrations (Cycles) to keep them separate from your other clients' data.

To create a new Cyclr Account, you would call the ```POST /v1.0/accounts``` API endpoint as described [in this article](./create-account).



### Installing Account Connectors

If a Cyclr Connector was built to work with your own system's API as part of signing up to use Cyclr (or your Plan allows you to create a Custom Connector to do this yourself), you may wish to add that into your Accounts as you create them so it's always available.  You can also install any other Account Connectors that you expect to use in Cycles so they're there when you need them.

*Note: When installing a Template, Cyclr will automatically add any missing Account Connectors to the Account so you don't have to use API calls to add all of them.*


To install an Account Connector call one of the ```POST /v1.0/connectors/.../install``` API endpoints as shown here in the [Cyclr **Interactive API Reference**](./testing-cyclr-api):

![Cyclr API Connector Install Endpoints](./images/cyclr-api-connector-install-endpoints.png)

\
Initially, you might need to get the details of a Connector you want to install so make a Request to the ```GET /v1.0/connectors``` endpoint using the application's name in the ```query``` QueryString parameter to search for it, e.g. ```GET /v1.0/connectors?query=salesforce```.  Cyclr will return any matches and you can then use the Name (and Version, if set) in future ```/install``` calls.

\
Depending on the authentication mechanism of the Connector (ApiKey, OAuth 1.0/2.0, Basic, etc) you'll need to [provide the authentication details to Cyclr differently](./authenticate-account-connector).

\
If you allow your clients to access Cyclr Accounts themselves, you may wish to provide the ```IsPartnerIntegrationConnector: true``` flag when installing your system's Connector to prevent authentication details or Connector-level settings being accessible through Cyclr's interface.


### Installing Templates

Once you have an Account, you can install Templates into it for any integrations the client will be using.

You can see what's available by calling the ```GET /v1.0/templates``` endpoint to [list available Templates](./list-available-templates).

You can then [install a Template](./install-from-template) by calling ```POST /v1.0/templates/{id}/install```.
