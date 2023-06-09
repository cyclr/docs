---
title: Insightly authentication
sidebar: cyclr_sidebar
permalink: insightly-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Insightly setup

### Requirements

To connect with Cyclr, you need an Insightly Account. To make an account, go to the [Insightly](https://login.insightly.com/) site and sign in as a new user.

### Get authentication details

To authenticate your connector, you need to get the **API Key** and **API URL** from your Insightly account. To find these authentication values, select the user account in the top right corner of the Insightly window and go to **User Settings** > **User Settings**. From there you can view the API section.

Once logged into the Insightly site, the API key and API URL can be located via navigating to the user account in the top right corner and selecting, `User Settings > User Settings` and reviewing the API section.

Record your API Key and API URL.

</section>
<section class="card">

### Account setup

Cyclr asks you for the below values when you install the Insightly connector into an account:

| **Value**          | **Description**                                                                       |
| :----------------- | :------------------------------------------------------------------------------------ |
| **Pod**            | If your API URL is 'https://api.na1.insightly.com/v3.1/', then your Pod is 'na1'. |
| **Username**       | Use the Insightly API Key as the Username.                                            |
| **Password**       | Leave the Password blank.                                                             |

> **Note**: You can use different details for different accounts.

</section>
