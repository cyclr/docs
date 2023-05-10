---
title: User experience
sidebar: cyclr_sidebar
permalink: launch-user-experience
tags: [launch]
menus:
    launch:
        title: User experience
        identifier: launch-user-experience
        toggleonly: menutoggleonly
        weight: 3
---
{::options parse_block_html="true" /}
<section class="card">

You can use LAUNCH to guide your users through the process to set up an integration between your application and third party applications. This means that your user only has to provide information that you can’t include with the template.

For example, you can use a template for an integration that exports contacts from your application to your user’s email marketing platform. Through LAUNCH, you can allow your user to select the mailing list to add contacts to.

</section>
<section class="card">

## Indicate intent to integrate with a 3rd party app

You can present your users with the option to install an integration. This can be as simple as a button labeled **Connect**, or a link within your application.

</section>
<section class="card">

## Select integration to install

When your user selects the link, LAUNCH opens a browser popup which displays a list of valid integrations that they can install.

![Select Integration](./images/select-integration.png)

If there is only one integration template that applies to the user, the user bypasses this screen.

</section>
<section class="card">

## Authenticate third party connectors

After the user selects an integration to install, LAUNCH takes them through the steps to authenticate each third party connector that the integration template uses. This screen depends on the authentication type that the connectors use.

![Three types of authentication.](./images/auth-launch.png)

If the user has already authenticated a connector, then the user doesn’t need to re-authenticate.

</section>
<section class="card">

## Step setup

LAUNCH presents the user with a screen to allow them to set up each step in the integration template that needs the user to select parameters.

* Your user might need to select from a list of values that are obtained from an authenticated connector in the integration template. For example, they might have to select a **Mailing List **from their email marketing platform.
* Your user might need to select a value from a predetermined list of valid values. For example, an email contact status: **Subscribed **or **Unsubscribed**.
* Your user might need to provide text values for complete flexibility. For example, this could be the source of an email lead.
  
![Field Mapping](./images/launch-field-mapping.png)

</section>
<section class="card">

## Return to host app

When the user completes the setup of their integration, LAUNCH presents the user with a screen that you can customize:
  
![Completed Integration Installation](./images/completed-installation.png)

To customize this screen, you can include your own HTML and JavaScript. You usually then return your user to your application.

LAUNCH provides response values that allow you to update your UI to indicate success, or instigate a backend process to make use of the newly installed Cyclr.

</section>
