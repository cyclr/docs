---
title: PetExec Connector Guide
sidebar: cyclr_sidebar
permalink: petexec-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

## PetExec setup

To authenticate the PetExec connector, you need a **Client ID**, **Client Secret** and the name of your account.

### Client ID & Client Secret

To obtain your Client ID and Client Secret, within your PetExec account:

1. Navigate to **Company Preferences** > **Misc. Settings** > **Maintain API Applications**.

<img src="./images/petexec_img_1.png" alt="The Petexec portal." width = 550px>

2. Name your application.

3. Enter a callback URL. This should be `https://{YourServiceDomain}/connector/callback`. For example, `https://app-h.cyclr.com/connector/callback`.

4. Select the **report_read**, **owner_read** and **scheduled_service_read** scopes.

5. Select **Add Application**.

PetExec then presents you with your **Client ID** and **Client Secret**.

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

</section>
