---
title: Zendesk Authentication
sidebar: cyclr_sidebar
permalink: zendesk-connector
tags: [connector]
---

# Zendesk setup

The Zendesk connector supports authentication with the following pairs of credentials:

-   A Zendesk account email and password.
-   A Zendesk account email and API token.

### Generating an API token

To generate an API token for your Zendesk account, please see Zendesk's documentation [here](https://support.zendesk.com/hc/en-us/articles/4408889192858-Generating-a-new-API-token).

# Cyclr setup

There are two ways to install the connector into an account in Cyclr:

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

# Additional information

### Updating deprecated Zendesk webhooks

Zendesk will soon deprecate HTTP targets within their API. To be compatible with this change, Cyclr has created new webhook methods that use webhooks instead of HTTP targets. As this is a Zendesk change, it means you have to replace these methods manually within your cycles. Information on Zendesk's deprecation of HTTP targets and conversion to webhooks can be found [here](https://support.zendesk.com/hc/en-us/articles/4408826284698-Announcing-the-deprecation-of-HTTP-targets-and-conversion-to-webhooks).

### Removing deprecated webhooks

To remove deprecated Zendesk webhooks from a cycle:

1. Go to a cycle that uses a Zendesk webhook.
2. Click **Stop** to stop the cycle running, and then **Finish and Stop** to allow any transactions to complete.
3. Click **Delete step** to delete the webhook and then click **OK** to confirm the deletion. This automatically removes targets and triggers associated with the webhook from Zendesk.

### Adding new webhooks

To add the new Zendesk webhooks to a cycle:

1. Find the updated Zendesk webhook methods under **Application Connectors** > **Zendesk** > **Webhooks** in the cycle builder.
2. Drag the required webhook onto the cycle builder.
3. Connect the webhook back to the cycle.
4. Click **Step setup** for each step within the cycle and check for invalid mappings. Fix as required.
5. Click **Run** to restart the cycle. This automatically adds webhooks and triggers associated with the webhook to Zendesk.
