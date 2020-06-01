---
title: Install a Partner Connector with LAUNCH or Marketplace
sidebar: cyclr_sidebar
permalink: partner-connector
tags: [launch, marketplace, guide, partner connector]
---

What is a Partner Connector?
---
Your Partner Connector is your application's connector. When installing Launch or Marketplace to a new account you can install your application's connector - the Partner Connector - into the account at the same time, so your users will not be expected to authenticate against your platform during the LAUNCH or Marketplace flow.

Setting up a Partner Connector
---

First you will need to make sure that you have a partner connector set up.
To do this from your console go to `Templates -> Template Connectors`. 

If the connector you wish to set as your partner connector is not in the list of *Installed Application Connectors* you must first [install it](installing-connectors).

Once the connector in the list of installed application connectors, toggle the *Standard* button so that it says *Native*.

![Generic Host Application](./images/partner_connector_standard.png)

![Generic Host Application](./images/partner_connector_native.png)

Your Partner Connector is now set up.

Fetch the Required Fields
---
To install the Partner Connector via Launch or Marketplace you will first need to fetch the prerequisite fields:

- Name
- Version
- AuthValue
- Properties

You can get the by calling the `/account/connectors` endpoint, which will return a list of all the connectors installed into your account. The Partner Connectors `IsPartnerIntegrationConnector` attribute will be true.

 Here are the relevant fields from the response:

    {
        "Name": "Example Partner Connector",
        "AuthValue": "Auth value for the connector.",
        "IsPartnerIntegrationConnector": true,
        "Properties": [
            {
                "Name": "Subdomain",
                "Value": "value",
                "Id": 41,
                "AccountConnectorId": 33
            },
            {
                "Name": "Region",
                "Value": "value",
                "Id": 42,
                "AccountConnectorId": 33
            }
        ]
    }

**Note:** `AuthValue` and `Properties` may be empty depending on the specific setup of the connector, if that is the case they can be ignored when creating the deploy request.

Once you have fetched the Partner Connector properties you can include them in the body of your request to deploy LAUNCH or Marketplace:

    {
        "Username": "user@example.com", 
        "Password": "password",
        "AccountId": "0000000-0000-0000-0000-000000000000",
        "partnerConnector": {
            "Name": "Example Partner Connector",
            "AuthValue": "Auth value for the connector.",
            "Properties": [
                {
                    "Name": "Subdomain",
                    "Value": "value",
                    "Id": 41,
                    "AccountConnectorId": 33
                },
                {
                    "Name": "Region",
                    "Value": "value",
                    "Id": 42,
                    "AccountConnectorId": 33
                }
            ]
        }
    }

For more details on deploying to Launch or Marketplace:

- [Deploying Launch](launch-deployment)
- [Deploying Marketplace](marketplace-deployment)
