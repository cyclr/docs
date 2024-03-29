---
title: Install a partner connector
sidebar: cyclr_sidebar
permalink: partner-connector
tags: [launch, marketplace, guide]
menus:
    embedding:
        title: Install a partner connector
        identifier: partner-connector
        toggleonly: menutoggleonly
        weight: 3
---
{::options parse_block_html="true" /}
<section class="card">
## What is a Partner Connector?

Your Partner Connector is your application's connector. When installing Launch or Marketplace to a new account you can install your application's connector - the Partner Connector - into the account at the same time, so your users will not be expected to authenticate against your platform during the LAUNCH or Marketplace flow.


</section>
<section class="card">
## Set up a Partner Connector

First you need to make sure that you have a partner connector set up. To do this from your console, go to **Templates** > **Template Connectors**. 

If the connector you want to set as your partner connector isn't in the list of **Installed Application Connectors**, select the **Install New Application** button in the top right corner of the page to install it.

Once the connector in the list of installed application connectors, select the **Standard** toggle to set the connector to **Native**.

![An example of connectors set to standard and native.](./images/partner-connector-standard-native.png)

</section>
<section class="card">

## Fetch the Required Fields

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
        "PartnerConnector": {
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

</section>
