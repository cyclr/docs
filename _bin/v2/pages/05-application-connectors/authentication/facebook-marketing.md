---
title: Facebook Marketing Authentication
sidebar: cyclr_sidebar
permalink: facebook-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
# Facebook Marketing API

Facebook Marketing API uses OAuth 2. You should sign up for an application on Facebook first and get an OAuth client ID and client secret.

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
6. You should be faced with a screen entitled **Add Products to Your App**. Under **Facebook Login**, select ``Set Up``.
7. This should now be added.  In the menu on the left, select ``Facebook Login`` > ``Settings``.
8. Under Valid OAuth Redirect URIs enter ``https://Your Service Domain/connector/callback``<br>
(_Your service domain can be found in your Cyclr console under Settings > General Settings > Service Domain._) and click ``Save Changes``.
9. Under **App Review** on the left, select ``Permissions and Features``.

    Here you're going to set the permissions you'll be asking your user for when they see the consent screen.  

    The permissions you choose will vary depending on your use case, but you will always need advanced access to the user's public profile to allow them to sign in.  

10. Search for ``public_profile``, click ``Get Advanced Access``, and complete the confirmation screen.

    You will notice that Advanced Access to public_profile is granted automatically.  The other permissions will require a bit more admin.

11. For this example, we'll add the ``leads_retrieval`` permission, which is required if you are working with Form submissions.

12. Once you have requested Advanced Access on this (and any other permissions), you'll be invited to **Edit App Review Request**. Click this, complete all the required sections, and Submit for Review.

13. Under Settings, Basic on the left menu, you'll be able to complete any missing sections, and copy your App ID and App Secret.  Once your app has been approved by Facebook, you'll be able to use these to authenticate your App in Cyclr.

Authenticating your Facebook Cyclr Connector
--------------

Go to your Cyclr Console > Connectors > Connector Library > Facebook Marketing API > Setup

**Client ID**: This is the App ID displayed after you create the Facebook app

**Client Secret**: This is the App Secret displayed after you create the Facebook app


Your Facebook Marketing API connector is now set up! You can test it by installing it in one of your user accounts.

Official Facebook Documentation
---------
[https://developers.facebook.com/docs/apps/register](https://developers.facebook.com/docs/apps/register)


</section>
