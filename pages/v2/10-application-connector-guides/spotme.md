---
title: SpotMe Connector Guide
sidebar: cyclr_sidebar
permalink: spotme-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
# Setup


</section>
<section class="card">
## Authentication Credentials

To authenticate the SpotMe connector you will need a Workspace ID and an API Key.

1. [Login](https://backstage.spotme.com/) to your SpotMe account

2. From the Workspaces menu, either select an existing workspace or create a new one following the on-screen instructions

   ![workspace menu](./images/spotme_interface_1.png)

### Workspace ID

1. Your Workspace ID can be found in the URL after 'event/'

   ![workspace id](./images/spotme_interface_2.png)

### API Key

1. From the bottom left of your Workspace's dashboard you will see a circular icon with your user initials (for example CD for Cyclr Dev). Click this and then click your user name

   ![user menu](./images/spotme_interface_3.png)

2. You will be taken to your user profile. Select 'API tokens' and then click 'Create a token'

   ![token menu](./images/spotme_interface_4.png)

3. You will be prompted to enter an identifier for your new token. Supply a label and click 'Create'

   ![create token](./images/spotme_interface_5.png)

4. Your new token will be shown. This will be the only time you will see your token, so please take note of it in a secure place

   ![token](./images/spotme_interface_6.png)


</section>
<section class="card">
## Connector Setup

1. Locate the SpotMe connector

   > Cyclr Console > Connectors > Connector Library > SpotMe

2. From the Edit Connector interface click 'Setup'

3. Enter your Workspace ID and click 'Next'

4. Enter your API Key and click 'Next'

The connector is now authenticated and ready to use.

</section>
