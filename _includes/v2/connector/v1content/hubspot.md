
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Create an App within HubSpot::

**NB**: This part can be completed once, by a Cyclr Partner.  The client/customer does not need their own separate App within HubSpot.

1. Login to the HubSpot Developer Portal [here](https://app.hubspot.com/signup-v2/developers)
2. Follow the HubSpot [documentation](https://developers.hubspot.com/docs/faq/how-do-i-create-an-app-in-hubspot) to create an application
3. In the `Auth` tab you will see a `Client ID` and `Client Secret`.  Note these to use in Cyclr's Connector setup.
4. Note the `Redirect URL` that creates the link between your Cyclr Console and HubSpot: it is shown on the page where the `Client ID` and `Client Secret` are entered.  It has the form
`https://[Your Cyclr Service Domain]/connector/callback`
5. You do not need to set Scopes at this point : see next section for details on this

### Scopes

You do not need to set scopes at this point. The default scopes of `crm.objects.contacts.read` and `crm.objects.contacts.write` will be requested by the Cyclr Connector if you leave the input empty. 

If you enter your own scope-list, this will override the default values. 

#### IMPORTANT NOTE (November 2021)

The way that HubSpot handles contact scopes has recently changed:

[https://developers.hubspot.com/docs/api/oauth/contacts-scope-migration](https://developers.hubspot.com/docs/api/oauth/contacts-scope-migration)

This should not affect you if you have set up a new HubSpot App, but contact Cyclr Support if you have any questions.

If you have an _existing_ HubSpot app this is likely to have been auto-migrated by HubSpot in early November 2021.  This shouldn't affect your integrations, but we'd recommend upgrading your Account Connector to the latest version at your earliest opportunity.


### Permissions

To use the Products and Line Items methods, the user must be assigned a [paid Sales Hub seat](https://knowledge.hubspot.com/articles/kcs_article/account/manage-sales-hub-and-service-hub-paid-users) within HubSpot.

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

The Connector now can be installed using the credentials obtained in the above steps:

- **Client ID**: `Client ID`
- **Secret**: `Client Secret`
- **Scopes/Optional**: This defines what permissions will be requested on the consent screen presented to your users.  

By default, all users are asked to consent to the following permissions/scopes:
- `crm.objects.contacts.read`
- `crm.objects.deals.read`
- `crm.objects.companies.read`

Where appropriate users are asked to consent to optional scopes:
- ``content``
- ``reports``
- ``e-commerce``
- ``forms``

If you need to request *alternative* scopes/optional scopes, set them here.

You will be prompted to log in, select your HubSpot and authorize access to the connector.

</div>

</section>

<section class="userguide" markdown="1">

## User Guide

<div class="section-content" markdown="1">

### Account Selection

When authenticating the HubSpot Connector and signing into HubSpot, the user is presented with the HubSpot **Choose an Account** screen.

During testing, you should select your main HubSpot account, rather than your developer account.  

You can identify the main account by looking for the one with items shown under the **PRODUCTS** heading as shown below.

In this example, that would be the "Cyclr" account:

![](./images/hubspot-choose-acct.png)

### Connector Parameters 

Useful if accessing this Connector via the API.  Property Names given here are in the same format as they should be passed to the API.

| Property Name   | Description    |
| ----------- | -----------    |
| Scopes      | The scopes of the connector: default values are  `crm.objects.contacts.read`,`crm.objects.deals.read`,`crm.objects.companies.read` |
| OptionalScopes   | The optional scopes of the connector. Default value is **content reports e-commerce forms** |


### Webhook Setup
Hubspot webhooks utilise a single webhook URL, this requires some configuration of your Hubspot application.

Go to Cyclr Console > Connectors > Application Connector Library > Hubspot > Setup

Copy the Webhook URL to your clipboard. e.g. ```https://<yourserivcedomain>/api/partnerwebhook/xxxxxx``` (Note:do not user the webhook url from the builder, but this one under the partner console)

You will now need to setup the Hubspot application to send webhooks. This has three steps:
 1. Enter the URL
 2. Select events to subscribe to
 3. Activate the events

#### Entering the URL

- Go to the Hubspot Developers App [Dashboard](https://app.hubspot.com/developer)
- s=Select the application you use with Cyclr
- Within this application, navigate to **Webhooks**
- Paste the `Webhook URL` from your clipboard, into the **Target URL**
- Click **Save** at the bottom of screen

#### Scopes

Seting up your subscriptions may require you to alter the scopes of the Hubspot application to allow the events to be sent. 

Ensure that your connector is authorised with the right scopes to recieve the webhook events.

#### Selecting events to subscribe to

- Click Create Subscription
- Select the objects and events that you wish to send to Cyclr
- Click Subscribe

#### Activating the events

- Under event subscriptions 
- Click the Hover **View subscriptions** button displayed on hover over the line
- Click the "Activate" button will be shown displayed on hover over the line

Your application is now set up for Webhooks using Cyclr.

### Adding Webhooks to your Cycle or Template

- Drag the Webhook step from the sidebar into the Builder
- Connect the Webhook to another step
- Click Run to start the Cycle

</div>

</section>