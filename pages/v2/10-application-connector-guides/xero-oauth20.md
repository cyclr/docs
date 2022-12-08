---
title: Xero OAuth2.0 Authentication
sidebar: cyclr_sidebar
permalink: xero-oauth2
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
# Xero (OAuth2.0)

## Partner Setup

In order to install a **Xero (OAuth2.0)** Connector, you must first create a Xero OAuth 2.0 **App** in Xero's Developer portal.

### Preparation 

When creating your Xero App, you will need to provide your Cyclr Partner **Service Domain** so it's best to have that information to hand before you begin.

This is specific to your instance of Cyclr and can be found in your Cyclr Partner Console under **Settings > General Settings > Service Domain**.

Your Cyclr Partner may have been setup with a default Service Domain, but this can be changed if you would prefer to remove mentions of 'cyclr' from it.  Contact Support for more.

### Creating a Xero App

Go to [https://developer.xero.com/myapps](https://developer.xero.com/myapps) to create a Xero OAuth 2.0 App in Xero.

Click the **New app** button in the top right to see a form similar to this:

![](./images/xero_oauth20_newapp.png)

Give the App a name (this will be presented to your users when they consent, so you may choose not to mention Cyclr).

Leave the **Integration type** as **Web App** and complete the rest of the fields.

Under **Company or application URL**, enter the domain of the site where your integration will be hosted.

For **Redirect URI**, enter your Cyclr Service Domain in this format:

```
https://[Your Cyclr Service Domain]/connector/callback
```

Read and agree to the Xero Developer Platform Terms and Conditions, and click **Create App**

### Finding your Client ID and Client Secret

You should now be faced with an App details screen - select **Configuration** from the menu on the left.

Make a note of your Client ID.

Generate a Secret, and make a note of that too.

You should now take your Client ID and Client Secret values and store them in your Cyclr Console against the Xero (OAuth2.0) entry.

### Cyclr Setup

From your Cyclr Console, click the **Connectors** option along the top then **Application Connector Library**, find **Xero (OAuth2.0)** - you may need to use the Search box to locate it - then click the Padlock button and paste and save your values there.

If you are a Xero Partner, you can also provide your **User-Agent** string, othewise leave it blank.

You should now be able to successfully install a **Xero (OAuth2.0)** Connector.

At this point it would be a good idea to install a Connector and run a test against one of the Methods, just to make sure the authentication process has been completed successfully.

### Payroll Sections
Xero has separate APIs for the Australian, UK and New Zealand markets so we have different payroll Methods within the connector to support them. You need to ensure that the client only uses the payroll section related to their login.  All other sections are common.
i.e. If the users system payroll is Australia they should only use the payroll methods under the Payroll - AU Section.

</section>
