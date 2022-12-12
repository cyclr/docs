---
title: Embedding introduction
sidebar: cyclr_sidebar
permalink: embedding-overview
tags: [embedding]
menus:
    embedding:
        title: Embedding introduction
        identifier: embedding-overview
        weight: 1
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
This article provides a broad overview of how Cyclr works with your app:

1.  Connect your API
2.  Create integrations
3.  User interface
4.  Hosted or self hosted

### 1. Connect your API

Our connectivity framework makes it very easy to add a platform connector for your app to Cyclr. With your API connected, you have instantly unlocked [100+ other integrations](http://cyclr.com/connectors).

Importing an API can be done automatically (if your API docs are hosted by Swagger, Apiary, etc) or semi-manually by using simple JSON to map to your API's methods. Once you have a Cyclr account, you can access tools to import your API.

### 2. Create integrations

Integrations are pre-made connections between your app and another app, which are then accessed by your users. For example, you may need to connect your app to MailChimp to sync contacts.  Integrations take the form of templates which can be made available either to all users or published for a specific user only.

In either case, these integrations are created by your team (or us, if you wish) using our [design tools](http://cyclr.com/design-tools). Having created and tested this integration in Cyclr's drag and drop builder, you then publish it to your app.

### 3. User interface

Cyclr is used by SaaS and app vendors in various ways, with users never seeing the integrations right up to a full integration marketplace with tools built on our API and served up in your app's UI.

The table below outlines some scenarios that are possible.

<table>
    <tr>
        <th>Deployment</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>Invisible</td>
        <td>Cyclr has no footprint in the host UI, instead integrations are setup by your team on behalf of users. This the fastest solution to deploy and is often popular for a first release to address immediate integration needs.</td>
    </tr>
    <tr>
        <td>Simple</td>
        <td>As with the Invisible deployment, except users activate their own authentication for the apps they want to connect. This is done using Cyclr's authentication framework. Upon connecting an app, integrations can optionally be automatically deployed and activated. This gives users an experience of simply activating integrations, with zero effort required on their part.</td>
    </tr>
    <tr>
        <td>User Self Serve</td>
        <td>Using Cyclr's API, the host app can build any interface to allow users to activate and customise integrations. The interface could be as simple as a button to start/stop a pre-made integration or a full step-based interface exposing users to the full integration with the ability to change behaviour, field mappings, decisions, etc.</td>
    </tr>
</table>

### 4. Hosted or self hosted

Cyclr provides hosting for your integrations, allowing you to get started quickly and have us take care of scaling, maintenance, and security.

In addition, Cyclr can also be deployed to your own infrastructure.

</section>
