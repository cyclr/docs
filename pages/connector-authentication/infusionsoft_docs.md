---
title: Infusionsoft Connector Guide
sidebar: cyclr_sidebar
permalink: infusionsoft-Connector
tags: [Connector]
---

## Connector Setup

### Obtaining Authentication Credentials

The Infusionsoft Connector is authenticated with a Client ID, Client Secret, Username and Password.

#### Client ID And Client Secret

The Client ID and Client Secret will both come from your Keap developer account. (Keap is the parent company of Infusionsoft)

You will need a developer account and a registered App. When authenticating the Connector we will link this App to the desired Infusionsoft account using these credentials.

1. If you have an account, [log in](https://keys.developer.keap.com/accounts/login). If not, [create an account](https://keys.developer.keap.com/accounts/create)

2. From the far right of the top navigation bar, click your username/email and then click 'Apps'

   ![keap portal](./images/infusionsoft_1.png)

3. Click '+ NEW APP'

   ![keap portal](./images/infusionsoft_2.png)

4. Enter a name for the App and optionally a description

5. You must activate API access for this App by clicking the toggle switch pictured below

   ![keap portal](./images/infusionsoft_3.png)

6. Click 'CREATE'

7. Your Client ID (Key) and Client Secret (Secret) will be displayed under 'API Keys'

   ![keap portal](./images/infusionsoft_4.png)

### Authenticate The Connector

1. Locate the Infusionsoft Connector

   > Cyclr Console > Connectors > Connector Library > Infusionsoft

2. From the Edit Connector interface click 'Setup'

3. Enter your Client ID and Client Secret. Click 'Next'

4. On the next page click 'Sign In'

5. You will be redirected to the Infusionsoft interface, where you will be prompted to log in to the Infusionsoft account you want to link the Connector/App to.

   > Note: The login credentials required here are **not the credentials for your developer account**. We are linking the App from your developer account to the desired Infusionsoft account.

6. You may be prompted to select the Infusionsoft account you are linking the Connector/App to. If so, select that now

   ![keap portal](./images/infusionsoft_6.png)

7. Allow the App access

   ![keap portal](./images/infusionsoft_7.png)

8. You will be redirected to the Cyclr interface where the Connector is now authenticated and ready to use

### User Guide

The Create and Update Contacts functionality is handled with a single method 'Upsert Contacts'. This will perform a duplicate check within Infusionsoft for the entered email address. If a matching email address is found, the existing contact will be updated. If no match is found, a new contact will be created.

When entering a State or Country code it is advised that you use our Lookup feature, as the Infusionsoft API has strict requirements for valid Province and Country codes.

![keap portal](./images/infusionsoft_8.png)

![keap portal](./images/infusionsoft_9.png)
