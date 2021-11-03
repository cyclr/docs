---
title: Facebook Messenger Authentication
sidebar: cyclr_sidebar
permalink: facebook-messenger-connector
tags: [connector]
---

# Facebook Messenger API #


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

Go to your Cyclr Console > Connectors > Connector Library > Facebook Messenger API > Setup

**Client ID**: This is the App ID displayed after you create the Facebook app

**Client Secret**: This is the App Secret displayed after you create the Facebook app

Your Facebook Messenger API connector is now set up! 

Webhook
--------------

NOTE: Facebook Messenger only allows a singular webhook URL per application. 
This should only be configured once you have authenticated the connector, and have entered the value for the ``Verify Token``.

1) In Cyclr, drag the ``Facebook Messenger`` > ``Message`` step on to the builder.
2) Add a decision step and connect it to the webhook reciever. Any decision configuration will work. 
3) Open the settings of the ``Message`` Webhook, and copy the URL.
4) Run the cycle.
5) In the Facebook Developer Console, navigate to  ``Facebook Messenger`` > ``Settings``.
6) Under the Webhook section, set the ``Callback URL`` to the URL you have just copied, and the ``Verify Token``. This can be any alphanumeric value, as long as you enter the same value in Cyclr when authenticating the connector.
7) Save these settings, and Facebook will verify the webhook with Cyclr.

You have now configured a webhook. If the Webhook URL changes for any reason, you will need to reconfigure it using the steps above.

Official Facebook Documentation
---------
[https://developers.facebook.com/docs/apps/register](https://developers.facebook.com/docs/apps/register)
