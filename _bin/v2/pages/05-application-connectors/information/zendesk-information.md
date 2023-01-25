---
title: Zendesk Information
sidebar: cyclr_sidebar
permalink: zendesk-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">
## Use Webhooks

In order to use Zendesk webhooks, your Zendesk connector needs to be authenticated against the account of a Zendesk Admin. 

</section>
<section class="card">
## Update deprecated Zendesk webhooks

Zendesk will soon deprecate HTTP targets within their API. To be compatible with this change, Cyclr has created new webhook methods that use webhooks instead of HTTP targets. As this is a Zendesk change, it means you have to replace these methods manually within your cycles. Information on Zendesk's deprecation of HTTP targets and conversion to webhooks can be found [here](https://support.zendesk.com/hc/en-us/articles/4408826284698-Announcing-the-deprecation-of-HTTP-targets-and-conversion-to-webhooks).

</section>
<section class="card">
## Remove deprecated webhooks

To remove deprecated Zendesk webhooks from a cycle:

1. Go to a cycle that uses a Zendesk webhook.
2. Select **Stop** to stop the cycle, and then select **Finish and Stop** to allow any transactions to complete.
3. Select **Delete step** to delete the webhook and then select **OK** to confirm the deletion. This automatically removes targets and triggers associated with the webhook from Zendesk.

</section>
<section class="card">
## Add new webhooks

To add the new Zendesk webhooks to a cycle:

1. Find the updated Zendesk webhook methods under **Application Connectors** > **Zendesk** > **Webhooks** in the cycle builder.
2. Drag the required webhook onto the cycle builder.
3. Connect the webhook back to the cycle.
4. Select **Step setup** for each step within the cycle and check for invalid mappings. Fix as required.
5. Select **Run** to restart the cycle. This automatically adds webhooks and triggers associated with the webhook to Zendesk.

</section>
