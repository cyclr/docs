---
title: MYOB AccountRight Live
sidebar: cyclr_sidebar
permalink: myob-accountright-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
Partner Setup
-------------

### Register with MYOB

The first thing to do - unless you already have a my.MYOB account - is to [register for MYOB AccountRight Live API access](https://developer.myob.com/api/accountright/api-overview/getting-started/) by clicking the **Register for API Access** button.  This requires completing a form then waiting on a confirmation email from MYOB.  It shouldn't take more than 24 hours for this to arrive and will enable you to sign in to [my.MYOB](https://my.myob.com.au/Pages/Default.aspx).


### Creating an MYOB App

Once you're in [my.MYOB](https://my.myob.com.au/Pages/Default.aspx), you can create an **App** within the Developer Dashboard to retrieve the neccessary authentication details required to allow Cyclr to access MYOB AccountRight Live's API.

The official MYOB AccountRight Live documentation for creating an **App** can be found [here under the "Access the API via the cloud" heading](https://developer.myob.com/api/accountright/api-overview/getting-started/).

![MYOB Account Right App Setup](./images/myob-accountright-create-an-app.png)

The **Redirect Uri** value should be set to contain the URL hosting your enduser Accounts:

```htmls://[Console Service Domain]/connector/callback```

For example:

```htmls://app-h.cyclr.com/connector/callback```


Once you've created your MYOB App, you'll be able to see its **Key** and **Secret** values which are used as the OAuth Client ID and Client Secret, respectively.

![MYOB Account Right App OAuth details](./images/myob-accountright-app-oauth-details.png)

In your Cyclr Partner Console, go to the Connectors menu then Connector Library, click the green Setup button for the MYOB AccountRight Live Connector and paste those details in there.

Your end users will now be able to install the Connector into their Cyclr Accounts.


### Requirements

For Cyclr to be able to access a user's MYOB Company File, **the default Administrator user must exist with a blank password**.  *If this isn't the case, then Cyclr won't be able to access it.*

</section>
