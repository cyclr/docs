---
title: Mailchimp Authentication
sidebar: cyclr_sidebar
permalink: mailchimp-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
## Partner Setup

To authenticate the Mailchimp connector you will need a `Client ID` and `Client Secret`.  These are obtained by setting up an application within your Mailchimp account.

### Setting up an application in Mailchimp

1. Navigate to the [Registered Apps](https://us1.admin.mailchimp.com/account/oauth2/) page in your Mailchimp account.
2. Click the [Register An App](https://us19.admin.mailchimp.com/account/oauth2/client/) link.
3. Fill out the **Register An App** form.
4. When completing the form, you will be asked for a **Redirect URI**.  You should enter<br/>
    <br/>
    https://``Your Service Domain``/connector/callback<br/>
    <br/>
    > Your service domain can be found in your Cyclr console under **Settings** > **General Settings** > **Service Domain**.
5. Once you have completed the form, click **Create**, and you will be presented with a `Client ID` and `Client Secret`.  You can now use these to authenticate your application.

For more information you can visit the official documentation here:

<a href="https://mailchimp.com/developer/guides/access-user-data-with-oauth-2/#register-your-application">https://mailchimp.com/developer/guides/access-user-data-with-oauth-2/#register-your-application</a>

</section>
