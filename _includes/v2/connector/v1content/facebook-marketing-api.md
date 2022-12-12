
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Facebook Marketing API uses OAuth 2. Register  an application on Facebook to get an OAuth `Client ID` and `Client Secret`.

*Note*: The process of having your app approved by Facebook may be lengthy (approx 5 days).

1. Log into your Facebook account.
2. Create a [Facebook Developer account](https://developers.facebook.com) if you don't have one
3. Go to *My Apps*: [https://developers.facebook.com/apps](https://developers.facebook.com/apps)
4. Click *Create App*, and select Business as the app type
5. Complete the following sections:
    - *App Display Name* : the name your users will see when they grant consent to access their data
    - *App Purpose* set to *Clients*
6. Click *Create App* and enter your password when prompted
7. On the *Add Products to Your App* screen, select *Facebook Login* > *Set Up*
8. In the menu on the left, select *Facebook Login > Settings*
9. Under Valid OAuth Redirect URIs enter `https://Your Service Domain/connector/callback`. Find your service domain in your Cyclr console under *Settings > General Settings > Service Domain* 
10. Click *Save Changes*
11. Under *App Review* on the left, select *Permissions and Features*
12. Set the permissions required when the user sees the consent screen.  The permissions vary according to use case, but advanced access to the user's public profile is required for sign in
13. Search for *public_profile*, click *Get Advanced Access*, and complete the confirmation screen. Advanced Access to public_profile is granted automatically.  Other permissions require more admin.
15. For this example, we'll add the *leads_retrieval* permission, which is required if you are working with Form submissions.
16. Once you have requested Advanced Access on this (and any other permissions), you'll be invited to *Edit App Review Request*. Click this, complete all the required sections, and *Submit for Review*.
17. Under *Settings > Basic* on the left menu, you'll be able to complete any missing sections, and copy your App ID and App Secret.  Once your app has been approved by Facebook, you'll be able to use these to authenticate your App in Cyclr.


## Official Facebook Documentation

See the [Facebook Developer Register](https://developers.facebook.com/docs/apps/register) page for more information.

</div>

</section>

<section class="setup partner" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Go to your Cyclr Console > Connectors > Connector Library > Facebook Marketing API > Setup

*Client ID*: This is the App ID displayed after you create the Facebook app

*Client Secret*: This is the App Secret displayed after you create the Facebook app


Your Facebook Marketing API connector is now set up! You can test it by installing it in one of your user accounts.


</div>

</section>

<section class="userguide" markdown="1">

## User Guide

<div class="section-content" markdown="1">

### Create Ad Set **Promoted Object**

The **Promoted Object** is required for certain campaign objectives. These are the Promoted Object fields based on the Optimization Goal.

| Optimization Goal     | Promoted Object Field |
| :-------------------- | :-------------------- |
| CONVERSIONS           | *Pixel ID* (Conversion pixel ID) |
|            | *Pixel ID* (Facebook pixel ID) and *Custom Event Type* |
|            | *Pixel ID* (Facebook pixel ID), *Pixel Rule* and *Custom Event Type* |
|            | *Event ID* (Facebook event ID) and *Custom Event Type* | 
|            | *Application ID*, *Object Store URL*, and *Custom Event Type* for mobile app events |
|            | *Offline Conversion Data Set ID* (Offline dataset ID) and *Custom Event Type* for offline conversions |
| PAGE_LIKES            | *Page ID* |
| OFFER_CLAIMS          | *Page ID* |
| LINK_CLICKS           | *Application ID* and *Object Store URL* for mobile app or Canvas app engagement link clicks |
| APP_INSTALLS          | *Application ID* and *Object Store URL* |
| OFFSITE_CONVERSIONS   | *Application ID*, *Object Store URL*, and *Custom Event Type* (Standard Events) |
| PRODUCT_CATALOG_SALES | *Product Set ID* |
|                       | *Product Set ID* and *Custom Event Type* |
| LEAD_GENERATION       | *Page ID* |

</div>

</section>
