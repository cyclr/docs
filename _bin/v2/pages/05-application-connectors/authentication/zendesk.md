---
title: Zendesk Authentication
sidebar: cyclr_sidebar
permalink: zendesk-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Zendesk setup

The Zendesk connector supports authentication with the following pairs of credentials:

-   A Zendesk account email and password.
-   A Zendesk account email and API token.

### Generate an API token

To generate an API token for your Zendesk account, please see Zendesk's [API documentation](https://support.zendesk.com/hc/en-us/articles/4408889192858-Generating-a-new-API-token).


</section>
<section class="card">
## Cyclr setup

There are two ways to install the connector into an account in Cyclr: with a password or with an API token.

### Install with email and password

Enter the following values when you install the Zendesk connector within an account:

| Field                 | Value                                                                                                                                                                             |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Zendesk Subdomain** | The Zendesk subdomain your Zendesk account exists under. For example, if your Zendesk account is under `http://mycompany.zendesk.com` then your Zendesk subdomain is `mycompany`. |
| **Username**          | The email of your Zendesk account.                                                                                                                                                |
| **Password**          | The password of your Zendesk account.                                                                                                                                             |

### Install with email and API token

Enter the following values when you install the Zendesk connector within an account:

| Field                 | Value                                                                                                                                                                             |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Zendesk Subdomain** | The Zendesk subdomain your Zendesk account exists under. For example, if your Zendesk account is under `http://mycompany.zendesk.com` then your Zendesk subdomain is `mycompany`. |
| **Username**          | The email of your Zendesk account followed by `/token`. For example, if the email of your Zendesk account is `me@example.com` then enter `me@example.com/token`.                  |
| **Password**          | The API token generated for your Zendesk account.                                                                                                                                 |


</section>
