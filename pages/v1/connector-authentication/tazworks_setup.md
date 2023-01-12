---
title: Tazworks Connector Guide
sidebar: cyclr_sidebar
permalink: tazworks-connector
tags: [connector]
---
Tazworks Setup
---------------
For Cyclr to connect with the Taxworks

1. Login to the Tazworks Developer Portal [here](https://developer.tazworks.com), note access to this portal is IP restricted.
2. Follow the Tazworks [documentation](https://developer.tazworks.com/#registration) to create an application.
3. In the `Info` tab you can set the API access (Orders) and CRA Registration.
4. The API is IP restricted so you will need to add the Cyclr servers IP address that can be found [here](https://docs.cyclr.com/cyclr-ip-whitelisting)4. Under the token tab you can create your API token needed for the connector.
5. Speak to your Tazworks Account Manger, and they can help with the setup. You will also need the base Domain depending on the Tazworks environment you are connecting to.

Connector Setup
---------------
The Connector now can be installed using the credentials obtained in the above steps:

**Domain**: `The domain that you want to use the API on. Can be set to "api-sandbox.instascreen.net" to use the sandbox for development/testing purposes.`

**API Key**: `This is the API token generated in steps above`
