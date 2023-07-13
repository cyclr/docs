---
title: Custom service domains
sidebar: cyclr_sidebar
permalink: custom-domains
tags: [cyclr-config]
menus:
    cyclr-configuration:
        title: Custom service domains
        identifier: custom-domains
        toggleonly: menutoggleonly
        weight: 8
---
{::options parse_block_html="true" /}
<section class="card">

You can use your own custom domain as your Cyclr Service Domain. To view your current service domain, go to **Settings** > **General Settings** in the Cyclr console and see the **Service Domain** field. 

You can’t edit the custom domain from the settings page. To add a custom service domain, see the section on how to [change your service domain](#change-your-service-domain).

</section>
<section class="card">

## Benefits of a custom service domain

There are several reasons that a custom service domain might benefit you:

### Google verification

Google doesn’t verify third party domains, so you need to set up a custom domain to become a verified Google application.

### Removes Cyclr from visible URLs

Webhook URLs and Redirect URLs for connectors that use OAuth authentication both use the Cyclr service domain. To make sure that your customers won’t see the name Cyclr in these URLs, you can add your own custom service domain to use instead.

> **Note**: If you change your service domain, you need to update your Webhook and Redirect URLs to use the new service domain.

### Third party cookies

The Safari web browser and Chrome Incognito windows both restrict access to third party cookies, which can cause errors when you display Cyclr to your customers in an iframe. To avoid errors, you can use a custom service domain that’s a sub domain of the domain that hosts your application.

</section>
<section class="card">

## Change your service domain

To change your service domain, you need to contact [Cyclr Support](https://support.cyclr.com/hc/en-us):

1. Provide us with an SSL certificate and its Private Key for the domain you want to use, for example, `integration.mydomain.com`. 

    **Note**: Before the existing SSL certificate expires, you need to provide us with the details of the new SSL certificate.

2. Create a **CNAME DNS** record that points the domain, `integration.mydomain.com`, to the [Cyclr instance](cyclr-api-authentication#api-domain) that you use. For example, if you use the US instance, use `my.cyclr.com`.

Once you set up the domain and provide us with the above details, we can set up your Cyclr console to use the new service domain.

> **Note**: If you change your service domain, you need to update your Webhook and Redirect URLs to use the new service domain.

</section>
