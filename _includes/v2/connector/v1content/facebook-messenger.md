
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Facebook Marketing API uses OAuth 2. Register  an application on Facebook to get an OAuth `Client ID` and `Client Secret`.

*Note*: The process of having your app approved by Facebook may be lengthy (approx 5 days).

## Setting up your Partner App

1. Log into your Facebook account.
2. Create a [Facebook Developer account](https://developers.facebook.com) if you don't have one
3. Go to **My Apps**: [https://developers.facebook.com/apps](https://developers.facebook.com/apps)
4. Click **Create App**, and select **Business** as the app type
5. Complete the following sections:
    - *App Display Name* : the name your users will see when they grant consent to access their data
    - *App Purpose* set to *Clients*
6. Click *Create App* and enter your password when prompted
7. On the *Add Products to Your App* screen, select *Facebook Messenger* > *Set Up*
8. In the menu on the left, select **Facebook Login > Settings**
9. Under Valid OAuth Redirect URIs enter `https://Your Service Domain/connector/callback`. Find your service domain in your Cyclr console under *Settings > General Settings > Service Domain* 
10. Click **Save Changes**
11. In the menu on the left, select **Facebook Messenger > Settings**. Scroll down to the **Access Tokens** section , and select **Add or Remove Pages**
12. Complete the required steps, adding the Facebook page you wish to use
13. Under **Settings > Basic** on the left menu, complete any missing sections, and copy your `App ID` and `App Secret`
14. Once Facebook approves your app, use `App ID` and `App Secret` to authenticate your App in Cyclr.

### Official Facebook Documentation

See the [Facebook Developer Register](https://developers.facebook.com/docs/apps/register) page for more information.

</div>

</section>

<section class="setup partner" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Go to your **Cyclr Console > Connectors > Application Connector Library > Facebook Messenger API > Setup**

**Client ID**: The `App ID` of your Facebook app.

**Client Secret**: The `App Secret` of your Facebook app.

**Scopes**: This is a comma separated list of scopes to request from Facebook during authentication.  For detail on the scopes please visit the [official documentation.](https://developers.facebook.com/docs/permissions/reference/)

**Verify Token**: This is used for Webhook validation. For more details please see the Webhook section below.

Your Facebook Messenger API connector is now set up! 

</div>

</section>

<section class="userguide" markdown="1">

## User Guide

<div class="section-content" markdown="1">

### Webhook Setup

Facebook Messenger webhooks utilise a single webhook URL, this requires some configuration inside your Facebook application.

1. Navigate to **Cyclr Console > Connectors > Application Connector Library > Facebook Messenger > Setup**
2. Set the **Verify Token** to an alphanumeric string of your choice. Make a note of this.
3. Copy the **Webhook URL** to your clipboard.
4. Navigate to the [Facebook Developers App Dashboard](https://developers.facebook.com/apps), and select the application you use with Cyclr.
5. Within this application, navigate to **Products > Messenger > Settings**.
6. Scroll down to the Webhook section.
7. Click the **Edit Callback URL** button, a dialog will open.
8. Paste the **Webhook URL** from your clipboard, and enter the **Verify Token** you took note of earlier.
9. Click **Verify and Save**, Facebook will then verify the endpoint.

Your application is now set up for Webhooks using Cyclr.

### Webhook Usage

1. Drag the Webhook step from the sidebar into the Builder.
2. Open the Webhook settings, and enter the Page ID.
3. Connect the Webhook to another step.
4. Click **Run** to start the Cycle. This contacts Facebook and subscribes this page to message Webhooks.

To remove the Webhook and cancel the Page subscription, stop the Cycle, and **Delete** the Webhook step.

The Webhook step deletion triggers Cyclr to contact Facebook and unsubscribe the Page from message Webhooks.

### Webhook Field Configuration

The body of the incoming message varies according to the message type received; for this reason, only a set of core fields are mapped by default.

Use the Edit Connector page to add the relevant fields. 

See the [Facebook message events documentation](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages) for more information.

### Adding New Facebook Pages

To use a new Facebook page with an already authenticated connector, reauthenticate with Facebook.
During the OAuth flow, use the **Edit Settings** button to select the new page, and grant permission.

### Roles & Test Users

If your application has not been approved by Facebook, the only users that can interact with it must be set within the developer console. 

To create a test user, click the menu on the left, and select **Roles > Test Users**.

</div>

</section>
