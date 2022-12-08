---
title: Stripe (OAuth) Authentication
sidebar: cyclr_sidebar
permalink: stripe-oauth-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
# Partner setup

### Retrieving client ID

From the [Connect settings](https://dashboard.stripe.com/settings/applications) page of your Stripe dashboard, do the following:

1. Locate the **Integration** section.
2. Under **OAuth settings**, enable **OAuth for Standard accounts**.
3. Under **Redirects**, select **+ Add URI**.
4. Enter your Cyclr redirect URL as the **Redirect URI**. This has the format: `https://Your-Cyclr-Service-Domain/connector/callback`.
5. Select **Add URI**.
6. Make note of the **Live mode client ID**, this will be required to set the connector up in Cyclr. If testing mode is enabled, this field will be labelled as **Test mode client ID**.

**Note**: Your service domain can be found in your Cyclr console under **Settings** > **General Settings** > **Service Domain**.

### Retrieving secret key

From the [API settings](https://dashboard.stripe.com/apikeys) page of your Stripe dashboard, do the following:

1. Select **Reveal live key**. If testing mode is enabled, this will be labelled as **Reveal test key**.
2. Make note of the **Secret key**, this will be required to set the connector up in Cyclr.

# Cyclr setup

### Console setup

To set up your **Stripe (OAuth)** connector within your Cyclr console:

1. Go to your **Cyclr Console**.
2. Select **Connectors** > **Application Connector Library** at the top of the page.
3. Use the search box to find the **Stripe (OAuth)** connector.
4. Select the **Setup Required** icon.
5. Enter the below values, omitting this step will allow you to use different settings for each account on installation:

| Value             | Description                               |
| ----------------- | ----------------------------------------- |
| **Client ID**     | The client ID of your Stripe account.     |
| **Client Secret** | The client secret of your Stripe account. |

Click the **Save Changes** button.

### Account setup

You will be asked for the following values when installing the **Stripe (OAuth)** connector within an account:

| Value             | Description                                                                          |
| ----------------- | ------------------------------------------------------------------------------------ |
| **Client ID**     | The client ID of your Stripe account, if you did not enter this in step 5 above.     |
| **Client Secret** | The client secret of your Stripe account, if you did not enter this in step 5 above. |

</section>
