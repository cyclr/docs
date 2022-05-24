<section class="authentication" markdown="1">

## Authentication

| **Type** | Basic |
| **Description** | Note when entering your Username and Password: if you have a Username and Password for Zendesk, enter them when requested. If not, enter your Email Address followed by "/token" (e.g. "me@example.com/token") and use your Zendesk API Token as the Password. |
{: .table .vheader}

</section>

<section class="zendesk-set-up" markdown="1">

## Zendesk set up

If you are not using a username and password to authenticate your Zendesk connector, then you need to generate a Zendesk API token. Zendesk's documentation on generating an API token can be found [here](https://support.zendesk.com/hc/en-us/articles/4408889192858-Generating-a-new-API-token).

</section>

<section class="cyclr-set-up" markdown="1">

## Cyclr set up

You will be asked for the following values when installing the Zendesk connector within an account:

-   **Subdomain**: The address of your Zendesk help centre or web portal.
-   **Username**: Your Zendesk account username or your Zendesk account email address followed by "/token"
-   **Password**: Your Zendesk account password or API token if you using an email address as your username.

Your Zendesk connector is now setup! You can test it by executing one of the methods to confirm it can return some data.

</section>

<section class="additional-information" markdown="1">

## Additional information

<div class="updating-deprecated-zendesk-webhooks" markdown="1">

### Updating deprecated Zendesk webhooks

Zendesk will soon deprecate HTTP targets within their API. To be compatible with this change, Cyclr has created new webhook methods that use webhooks instead of HTTP targets. As this is a Zendesk change, it means you have to replace these methods manually within your cycles. Information on Zendesk's deprecation of HTTP targets and conversion to webhooks can be found [here](https://support.zendesk.com/hc/en-us/articles/4408826284698-Announcing-the-deprecation-of-HTTP-targets-and-conversion-to-webhooks).

</div>

<div class="removing-deprecated-webhooks" markdown="1">

### Removing deprecated webhooks

To remove deprecated Zendesk webhooks from a cycle:

1. Go to a cycle that uses a Zendesk webhook.
2. Click **Stop** to stop the cycle running, and then **Finish and Stop** to allow any transactions to complete.
3. Click **Delete step** to delete the webhook and then click **OK** to confirm the deletion. This automatically removes targets and triggers associated with the webhook from Zendesk.

</div>

<div class="adding-new-webhooks" markdown="1">

### Adding new webhooks

To add the new Zendesk webhooks to a cycle:

1. Find the updated Zendesk webhook methods under **Application Connectors** > **Zendesk** > **Webhooks** in the cycle builder.
2. Drag the required webhook onto the cycle builder.
3. Connect the webhook back to the cycle.
4. Click **Step setup** for each step within the cycle and check for invalid mappings. Fix as required.
5. Click **Run** to restart the cycle. This automatically adds webhooks and triggers associated with the webhook to Zendesk.

</div>

</section>
