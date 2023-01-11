
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

To authenticate the Mailchimp connector you need a `Client ID` and `Client Secret`.  

Set up an application within your Mailchimp account to obtain these:

- Go to the [Registered Apps](https://us1.admin.mailchimp.com/account/oauth2/) page in your Mailchimp account
- Click the [Register An App](https://us19.admin.mailchimp.com/account/oauth2/client/) link
- Complete the **Register An App** form
    For the **Redirect URI** enter  your service domain
    - Go to your Cyclr console
    - Go to  **Settings** > **General Settings** > **Service Domain**
    - Note the service domain part of the url :
        https://``Your Service Domain``/connector/callback
- Click **Create**
- Note the `Client ID` and `Client Secret`  

Use these to authenticate your application.

See the [official documentation](https://mailchimp.com/developer/guides/access-user-data-with-oauth-2/#register-your-application<) for more information.

</div>

</section>

