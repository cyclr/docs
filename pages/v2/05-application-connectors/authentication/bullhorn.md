---
title: Bullhorn Authentication
sidebar: cyclr_sidebar
permalink: bullhorn-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
# Bullhorn


</section>
<section class="card">
## Partner Setup

To authenticate the Bullhorn connector you will need a Client ID and Client Secret.  If you do not already have these, you or a listed Account / Support Contact will need to get in touch with Bullhorn Support to have credentials set up.

If asked for a callback URI during this process, give

https://``Your Service Domain``/connector/callback 

Your service domain can be found in your Cyclr console under Settings > General Settings > Service Domain.

Once you have your Client ID and Secret, you will be able to use these details to authenticate the connector.


</section>
<section class="card">
## Apache Tomcat Error

After you are redirected to Bullhorn during the authentication process, sometimes Bullhorn displays an Apache Tomcat error like this:

![Bullhorn Redirect Error](./images/bullhorn-redirect-error.png)

This is a known issue with Bullhorn. The solution is to clear the Bullhorn cookies in your browser, or open Cyclr and authenticate the connector in a private window.


</section>
