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

Go to your Cyclr Console > Connectors > Application Connector Library > Facebook Messenger API > Setup

**Client ID**: The App ID of your Facebook app.

**Client Secret**: The App Secret of your Facebook app.

**Scopes**: This is a comma separated list of scopes to request from Facebook during authentication.  For detail on the scopes please visit the [official documentation.](https://developers.facebook.com/docs/permissions/reference/)

**Verify Token**: This is used for Webhook validation. For more details please see the Webhook section below.

Your Facebook Messenger API connector is now set up! 

Webhook Setup
--------------
Facebook Messenger webhooks utilise a single webhook URL, this requires some configuration inside your Facebook application.

1. Navigate to Cyclr Console > Connectors > Application Connector Library > Facebook Messenger > Setup
2. Set the **Verify Token** to an alphanumeric string of your choice. Make a note of this.
3. Copy the **Webhook URL** to your clipboard.
4. Navigate to the [Facebook Developers App Dashboard](https://developers.facebook.com/apps), and select the application you use with Cyclr.
5. Within this application, navigate to Products > Messenger > Settings.
6. Scroll down to the Webhook section.
7. Click the **Edit Callback URL** button, a dialog will open.
8. Paste the **Webhook URL** from your clipboard, and enter the **Verify Token** you took note of earlier.
9. Click **Verify and Save**, Facebook will then verify the endpoint.

Your application is now set up for Webhooks using Cyclr.

Webhook Usage
--------------
1. Drag the Webhook step from the sidebar into the Builder.
2. Open the Webhook settings, and enter the Page ID.
3. Connect the Webhook to another step.
4. Click **Run** to start the Cycle. This will contact Facebook and subscribe this page to message Webhooks.

If you wish to remove the Webhook and cancel the Page subscription, you must stop the Cycle, and **Delete** the Webhook step. 
The deletion of the Webhook step will trigger Cyclr to contact Facebook and unsubscribe the Page from message Webhooks.

Webhook Field Configuration
--------------
The body of the incoming message will vary depending on the message type received; for this reason, only a set of core fields are mapped by default.
Please use the Edit Connector page to add the fields you wish to use. Documentation for Facebook message events is available [here](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages).

Adding New Facebook Pages
--------------
To use a new Facebook page with an already authenticated connector, you will need to reauthenticate with Facebook.
During the OAuth flow, use the **Edit Settings** button to select the new page, and grant permission.

Roles & Test Users
--------------
If your application has not been approved by Facebook, the only users that will be able to interact with it must be set within the developer console. To create a test user, click the menu on the left, and select ``Roles`` > ``Test Users``.

Official Facebook Documentation
---------
[https://developers.facebook.com/docs/apps/register](https://developers.facebook.com/docs/apps/register)
