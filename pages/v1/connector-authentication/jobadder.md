---
title: JobAdder Authentication
sidebar: cyclr_sidebar
permalink: jobadder-connector
tags: [connector]
---

# JobAdder setup

To authenticate the JobAdder connector, you will need the following pieces of information:

* `Client ID`
* `Client Secret`

To obtain the above and authenticate the connector, follow these steps:

### 1. Create a registered application in your JobAdder developer's profile
1. Log into the JobAdder developer area found [here](https://developers.jobadder.com/).
2. Sign in with your developer account.
3. Browse to the **Applications** area.
4. Select **Register a new application**.
5. Give the application a suitable name and description.
6. Enter the callback URL in the **Authorized redirect URIs** field. The callback URL has the following format:

`https://{Your Cyclr service domain e.g. app-h.cyclr.com}/connector/callback`

7. Select **Register application**.
8. Make a note of the `Client ID` and `Client Secret`.

### 2. Authenticate your connector
You can now use the `Client ID` and `Client Secret` to authenticate your JobAdder connector. Enter these details and you will be prompted to allow the application access to your JobAdder data.

Your JobAdder Connector is now set up! You can test it by installing it to one of your Cyclr accounts and using one of the methods to confirm it returns data.
