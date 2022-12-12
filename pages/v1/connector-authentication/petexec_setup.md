---
title: PetExec Connector Guide
sidebar: cyclr_sidebar
permalink: petexec-connector
tags: [connector]
---

## Setup

To authenticate the PetExec connector you will need a Client ID, Client Secret and the name of your account.

### Client ID & Client Secret

To obtain your Client ID and Client Secret, within your PetExec account:

1. Navigate to Company Preferences > Misc. Settings > Maintain API Applications

   ![petexec portal](./images/petexec_img_1.png)

2. Give the application a name

3. Enter a callback URL. This should be https://{Your Cyclr service domain e.g. <span>app-h.cyclr.</span>com}/connector/callback

4. Select the **report_read** and **owner_read** scopes

5. Click "Add Application"

You will be presented with your Client ID and Client Secret.

### Account Name

Your PetExec account as it is formatted in the URL. Example: if the URL for your account was https://<span>secure.mycompany.</span>net/ your account name would be mycompany.

### Connector Setup

1. Locate the PetExec connector

   > Cyclr Console > Connectors > Connector Library > PetExec

2. From the Edit Connector interface click 'Setup'

3. Enter your Client ID, Client Secret and PetExec Account Name

4. Click 'Next' and then 'Sign In'

5. You will be prompted to login to your PetExec account, after which you will be redirected to Cyclr

The connector is now authenticated and ready to use.
