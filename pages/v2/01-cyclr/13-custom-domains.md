---
title: Custom Service Domain
sidebar: cyclr_sidebar
permalink: custom-domains
tags: [installing, embedding, service domain]
menus:
  cylr:
    title: Custom Service Domain
    url: /custom-domains
---

### Using your own domain as a Cyclr Service Domain

To use your own domain as Cyclr Service Domain, follow these steps:

* You must provide us with an SSL certificate and its Private Key for the domain you wish to use with Cyclr, e.g. ```integration.mydomain.com```, which we will install on our web servers.
* You must create a CNAME DNS record pointing ```integration.mydomain.com``` to the Cyclr Instance you're hosted on. If you're on the US Instance for example, that will be `my.cyclr.com`.  Get in touch if you're not sure.
* Contact Cyclr Support once the above tasks have been completed and we'll perform some setup on your Cyclr Console.
* You will need to provide details of a new SSL certificate before the existing one expires (we plan to make this less manual in future).

***IMPORTANT: Changing your Service Domain will require you to update any referenced Webhook or App Callback/Redirect URLs.***


### Reasons to do this

#### Removes "cyclr" from Webhook and Redirect URLs
The domain set as your Cyclr Console's Service Domain is used for Webhook URLs as well as Redirect URLs for Connectors using OAuth authentication.  It may therefore be seen by your own users.  Because of this you may wish to change it to your own domain to remove mentions of Cyclr.

**If you have already created Cycles using Webhooks or setup third party Apps, you will need to update them to use your new Service Domain.**

#### Avoids issues with how some web browsers handle third party cookies
The Safari web browser and Chrome Incognito windows restrict access to third party cookies, causing errors when displaying Cyclr in an iframe to your users.

You can avoid these by using a Service Domain which is a subdomain of the domain hosting your web application.
