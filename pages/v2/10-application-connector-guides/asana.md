---
title: Asana
sidebar: cyclr_sidebar
permalink: asana
tags: [connector]
---

## Partner Setup

### oAuth Application Creation

You will need to provide your Cyclr Partner ‘Service Domain’ as part of the process of setting up access so best to have that information to hand before starting. This is specific to your instance of Cyclr and it can be found from the Cyclr Partner Console under: Settings > General Settings > Service Domain.

In Asana Register an oAuth Application

You must first register your application with Asana to receive a client ID and client secret. 

Visit your Account Settings dialog, click the Apps tab, and "Add New Application".

You must supply your new application with:

 * App Name - A name for your application. 
 * App URL - This is url of your company
 * Redirect URL - https://[Your Cyclr Service Domain]/connector/callback

Once you have created an app, the details view will include a Client ID, needed to uniquely identify your app to the Asana API, as well as a Client Secret.

Note Your Client Secret is a secret, it should never be shared with anyone or checked into source code that others could gain access to.

### Cyclr Setup

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Find the **Asana** Connector
*   Click the **Setup** button

Enter the following values:

 * **Client ID**: Client ID obtained from registering an application

 * **Client Secret**: The client secret obtained from registering an application.

Your Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
