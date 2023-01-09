---
title: Settings
sidebar: cyclr_sidebar
permalink: connector-settings
tags: [connector-creation]
menus:
    create-a-connector:
        title: Settings
        identifier: connector-settings
        weight: 1
---
{::options parse_block_html="true" /}
<section class="card">
## Custom Connectors

With certain Cyclr price plans, it is possible to create Custom Connectors.  These connectors are private to the Partner Organisation that created them.  


</section>
<section class="card">
## Connector Basics

A connector may have various Releases.  When you add a new connector only certain basic naming details are entered.  The main details of the specification of the connector are provided at the connector release level.  A connector can have only one 'live' release and there may be previous deprecated versions.

There may also be a 'draft' release which is a pending update or extension to the connector. Pushing the draft release live will cause the current live release to become deprecated.

When a release is pushed live this might be done as a Major release which will cause an 'update available' message to appear on all Steps in templates and live integrations using the connector.  A Major release should generally be used when existing methods need to be updated.  A Minor release can be used when there are no changes being made (or only very minor ones) to existing methods, or when new methods are being added.


</section>
<section class="card">
## Connector Settings

| Property | Description | Recommended Standards |
| --- | --- | --- |
| Name | The name of the connector that will be used in the interface. | This should not include the API Version. |
| Description | Description of the product. | Take this from the application's website. |
| API Version | Version should be the same as the API's version.| |
| Icon | The logo that will be used to represent the application. | 400x400 pixel PNG image with a transparent background. |


</section>
<section class="card">
## Release Settings

| Property | Description | Recommended Standards |
| --- | --- | --- |
| Comments | A description of the Application.| |
| Post install Property Value Lookup Method | Choose a method to run immediately after authentication, to get a value. | |
| Post Install Test Auth Method | As above, but a method to check that you have successfully authenticated the connector. | |
| Inbound Paging? | Does the API support paging when large amounts of data are requested? | |
| Inbound Page Size | If inbound paging is supported, provide the default page size. | |
| Outbound Page Size | If outbound paging is supported, provide the default page size. | |
| User Singular Partner Webhook URL? | For specific cases where individual webhook URLs are not appropriate. | Speak to the support team if you would like more information on this setting. |
| Icon | The logo that will be used to represent the application. | 400x400 pixel PNG image with a transparent background. |


</section>
<section class="card">
## Related Topics

[Paging](./connector-paging)  


</section>
