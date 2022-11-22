---
title: Contact Form 7 Plugin
sidebar: cyclr_sidebar
permalink: contact-form-7-plugin
tags: [plugins]
---

Contact Form 7, a plugin for WordPress - does not include webhook functionality. This makes getting the data from form submissions difficult.

We have created our Contact Form 7 plugin to allow for easy integration with any of the [apps or services that Cyclr connects](https://cyclr.com/connectors).

#### Prerequisites

*   WordPress with admin access
*   [Contact Form 7](https://contactform7.com/) installed
*   [Contact Form 7 Modules](https://en-gb.wordpress.org/plugins/contact-form-7-modules/) installed (required for hidden fields)
*   Cyclr account

#### Plugin installation

If you have completed the prerequisites:

*   [Download our Contact Form 7 plugin](http://files.cyclr.com/cyclr-plugins/cyclr-webhooks.zip)
*   In WordPress, click Plugins and then Add New
*   On the Add Plugins page, click Upload Plugin
*   Locate the zip file for the plugin on your computer and upload it

Once those steps are complete, you are ready to set up the plugin.

Once you have [installed our Contact Form 7](https://intercom.help/cyclr/contact-form-7-plugin/installation) plugin, you are ready to set up webhooks on your forms.

#### Get your webhook’s URL from Cyclr

*   Create a cycle and install the Contact Form 7 Plugin connector
*   Click/drag the Form Entry step into the builder
*   Click the cog icon on the step and copy the webhook’s URL to your clipboard.

#### Set up Contact Form 7

*   In Contact Form 7, open your form for editing
*   Add a new hidden field named url to your form
*   In the window that creates your new field, set the value for this new field to be [https://yourcyclrwebhook](https://yourcyclrwebhook/)

#### Set up custom fields in Cyclr

Cyclr will not know about the fields you’ve added to your form by default. You will need to add these.

*   In the builder, open the connector in the sidebar and click the Settings button
*   Under Methods & Fields, pop open the Entries category and then the Form Entry webhook
*   On the Fields tab, click the plus button to add a new field
*   Set the Location field to the the name of the field in Contact Form 7, e.g. name, email, company, etc
*   Set the Display Name to be anything you like; this is shown in Cyclr when you are mapping fields
*   The Description field is optional
