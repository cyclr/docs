---
title: Counterpoint
sidebar: cyclr_sidebar
permalink: counterpoint
tags: [connector]
---

## Counterpoint ##

This document will explain what is needed to setup access to Counterpoint and install the connector.

### Authentication Details Setup ###
1. Create a new company user through your Counterpoint portal.
2. Apply for developer API Keys by contacting NCR. More information about this can be found [here](https://github.com/NCRCounterpointAPI/APIGuide/blob/master/InstallationAndConfiguration/Licensing.md).

### Connector Setup ###
In the connector setup enter your server URL and API Key. The server URL should have the following format: "https://{URL}:{Port}".

Now enter the company user login details. The username will start with the company name, followed by a period and then the username. For example: "{CompanyName}.{UserName}".

More information about Authorization can be found [here](https://github.com/NCRCounterpointAPI/APIGuide/blob/master/Basics/Requests.md#authorization).