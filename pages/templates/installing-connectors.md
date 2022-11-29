---
title: Connectors
sidebar: cyclr_sidebar
permalink: installing-connectors
tags: [templates]

---
## Basics

In order to build a Cyclr Template you first need to install connectors. You can do this from the builder.  If this is your first Template, you will be directed to the connector store in order to get started.

![](./images/add-connector.gif)

If you need further connectors these can be added from the right sidebar of the builder.  There are two types of connector available.  Application connectors work with many popular SaaS applications.  Utility connectors are provided to help in the construction of your integrations.

If you want to test a Template, you will need to authenticate the connectors that have been used in order to allow Cyclr to connect and transfer data. If you are just experimenting, you can skip the authentication step and install with the connector without authentication.  However, we strongly recommend that you thoroughly test your Templates before they are published.  

## Authenticating a Connector

There are different types of authentication. Depending on the connector you wish to use, the application may require any of the following:

*   OAuth – login using your account and give permissions
*   An API key
*   Username and password
*   No authentication, e.g. for webhooks

If the application uses OAuth authentication, then you will need to get a Client ID and Client Secret.  The way in which this is done differs application by application, and there is documentation provided about what needs to be done.  Although you can add the Client ID and Client Secret when the connector is authenticated in the builder, the recommendation is that they are added to the connector by going to the Application Connector page and clicking on the 'pad lock' symbol.

For the second part of the OAuth process you will be handed off to the application to which you are connecting to complete the process by entering your Username and Password.

For the other authentication methods, the connector installer will take you through the steps required in order to complete the authentication.

Once you have authenticated your connectors, you will be returned to the builder. Your new connectors will be installed in the sidebar ready to use.

## Related Topics

[How to Build a Template](./building-a-template)
