---
title: MYOB AccountRight Live
sidebar: cyclr_sidebar
permalink: myob-accountright-connector
tags: [connector]
---

# MYOB AccountRight Live #

Partner Setup
-------------

The first thing to do - unless you already have a my.MYOB account - is to [register for API access with MYOB](https://developer.myob.com/contact/register-for-myobapi-access/).  This requires completing a form then waiting on a confirmation email from MYOB.  It shouldn't take more than 24 hours for this to arrive and will enable you to sign in to [my.MYOB](https://my.myob.com.au/Pages/Default.aspx).

One you're in [my.MYOB](https://my.myob.com.au/Pages/Default.aspx), you can create an **App** within the Developer Dashboard to retrieve the neccessary authentication details required to allow Cyclr to access MYOB AccountRight Live's API.

The official MYOB AccountRight Live documentation for creating an **App** can be found [here under the "Access the API via the cloud" heading](https://developer.myob.com/api/accountright/api-overview/getting-started/).

[screenshot of Register App form]

The **Redirect Uri** value should be set to contain both the URL of your Cyclr console and the URL hosting your enduser Accounts, separated by a comma:

```https://my.cyclr.[com/uk]/connector/callback,https://[Console Service Domain]/connector/callback```

For example:

```https://my.cyclr.com/connector/callback,https://app-h.cyclr.com/connector/callback```


Once you've created your MYOB App, you'll be able to see its **Key** and **Secret** values.  Copy and paste these back into your Cyclr Console's Connector Library as the Client ID and Client Secret values of the MYOB AccountRight Live Connector.

Your end users will now be able to install the Connector into their Cyclr Accounts.


For Cyclr to be able to access a user's MYOB Company File, the default Administrator user must exist with a blank password.  If this isn't the case, then Cyclr won't be able to access it.

Once installed, the Company File can then be selected through Step Setup in the Builder.

ALternatively, when creating a Template for integrating with MYOB that you wish to make available to your users, you can use a Cycle Variable in your Template and reference that in each MYOB Step's , giving yourself a single location


MYOB AccountRight Live requires a Company File to be chosen for each Step in the Cycle Builder so that the Request is sent to the correct location when it's run.
