
# Zendesk #

Zendesk OAuth 2 Setup:
---

In order to set up OAuth 2 in Zendesk log in to your account and go to `Admin -> API -> OAuth Clients` and click the `+` button to setup a new OAuth application.

Once you have entered the required information and clicked `Save` you will be shown a Secret.

You will need to copy both your Unique Identifier and Secret that were created during this setup - into the Client ID and Client Secret fields - in the Zendesk Connector setup in Cyclr - respectively.

# Updating deprecated Zendesk webhooks

Zendesk will soon deprecate HTTP targets within their API. To be compatible with this change, Cyclr has created new webhook methods that use webhooks instead of HTTP targets. As this is a Zendesk change, it means you have to replace these methods manually within your cycles. Information on Zendesk's deprecation of HTTP targets and conversion to webhooks can be found [here](https://support.zendesk.com/hc/en-us/articles/4408826284698-Announcing-the-deprecation-of-HTTP-targets-and-conversion-to-webhooks).

## Removing deprecated webhooks

To remove deprecated Zendesk webhooks from a cycle:

1. Go to a cycle that uses a Zendesk webhook.
2. Click **Stop** to stop the cycle running, and then **Finish and Stop** to allow any transactions to complete.
3. Click **Delete step** to delete the webhook and then click **OK** to confirm the deletion. This automatically removes targets and triggers associated with the webhook from Zendesk.

## Adding new webhooks

To add the new Zendesk webhooks to a cycle:

1. Find the updated Zendesk webhook methods under **Application Connectors** > **Zendesk** > **Webhooks** in the cycle builder.
2. Drag the required webhook onto the cycle builder.
3. Connect the webhook back to the cycle.
4. Click **Step setup** for each step within the cycle and check for invalid mappings. Fix as required.
5. Click **Run** to restart the cycle. This automatically adds webhooks and triggers associated with the webhook to Zendesk.
