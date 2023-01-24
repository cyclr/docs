---
title: Facebook Messenger Authentication
sidebar: cyclr_sidebar
permalink: facebook-messenger-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">
# Facebook Messenger API


Facebook Messenger API uses OAuth 2. You should sign up for an application on Facebook first and get an OAuth client ID and client secret.

> Note: The process of having your app approved by Facebook may be lengthy (~5 days).

Setting up your Partner App
-------------
1. Log into your Facebook account.
2. Create a Facebook Developer account if you don’t already have one: [https://developers.facebook.com](https://developers.facebook.com)
3. Go to ``My Apps``: [https://developers.facebook.com/apps](https://developers.facebook.com/apps)
4. Click ``Create App``, and select Business as the app type.

    Complete the following sections:

    * **App Display Name** This is the name your users will see when they grant consent to access their data.
    * **App Purpose** (set to ``Clients``.)

5. Click ``Create App`` (You will then be asked to enter your password).
6. You should be faced with a screen entitled **Add Products to Your App**. Under **Facebook Messenger**, select ``Set Up``.
7. This should now be added.  In the menu on the left, select ``Facebook Login`` > ``Settings``.
8. Under Valid OAuth Redirect URIs enter ``https://Your Service Domain/connector/callback``<br>
(_Your service domain can be found in your Cyclr console under Settings > General Settings > Service Domain._) and click ``Save Changes``.
9. In the menu on the left, select ``Facebook Messenger`` > ``Settings``. Scroll down to the ``Access Tokens`` section , and select ``Add or Remove Pages``. 
10. Complete the required steps, adding the Facebook page you wish to use.
11. Under Settings, Basic on the left menu, you'll be able to complete any missing sections, and copy your App ID and App Secret.  Once your app has been approved by Facebook, you'll be able to use these to authenticate your App in Cyclr.


Authenticating your Facebook Cyclr Connector
--------------

Go to your Cyclr Console > Connectors > Application Connector Library > Facebook Messenger API > Setup

**Client ID**: The App ID of your Facebook app.

**Client Secret**: The App Secret of your Facebook app.

**Scopes**: This is a comma separated list of scopes to request from Facebook during authentication.  For detail on the scopes please visit the [official documentation.](https://developers.facebook.com/docs/permissions/reference/)

**Verify Token**: This is used for Webhook validation. For more details please see the Webhook section below.

Your Facebook Messenger API connector is now set up! 

</section>
