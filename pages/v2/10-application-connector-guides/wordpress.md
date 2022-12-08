---
title: Wordpress Authentication
sidebar: cyclr_sidebar
permalink: wordpress-connector.html
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
# Wordpress #

Wordpress Connector Setup
-------------

## Read me ##
Make sure this is the right Wordpress connector you are after. This connector is used for self-hosted Wordpress sites.
For Wordpress hosted sites view the Wordpress guide [here](https://docs.cyclr.com/wordpresscom-connector#wordpress-connector-setup).

## Authentication ##
In order to allow Cyclr to connect to your WordPress site’s API, you must install the <a href="https://wordpress.org/plugins/rest-api-oauth1/" target="_blank">WordPress REST API – OAuth 1.0a Server</a>. This gives your site the ability to securely authenticate API use.

### Register Cyclr as an application ###
Once you have installed the plugin, open WordPress and go to:

Users &gt; Applications &gt; Add New

The values needed to add your app are:
* Name: Cyclr
* Description: this is a free text area
* Callback: {% raw %}https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback{% endraw %}

Your setup should look something like this:
![](/images/wordpress-cyclr-api-authentication.png)

When you add your Consumer, you will be presented with your Client Key and Client Secret.
![](/images/wordpress-oauth-credentials.png)

(Yours will be different to the screenshot).

### Authenticate WordPress in Cyclr ###
With the above correctly setup, install the WordPress connector in Cyclr and provide the Client Key and Client Secret along with your website’s URL.

![](/images/wordpress-auth.png)

Click the Next button and you will be prompted to sign into WordPress. Do this and then authorize Cyclr and you can now begin to use your WordPress site’s API.

</section>
