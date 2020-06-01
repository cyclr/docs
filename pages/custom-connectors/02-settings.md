---
title: Connector Settings
sidebar: cyclr_sidebar
permalink: connector-settings
tags: [connector-creation]
---

## Custom Conectors

With certain Cyclr price plans it is possible to create custom connectors.  These connectors are private to the Partner Organisation which created them.  

## Connector Basics

A connector may have vanrious releases.  When you add a new connector only certain basic naming details are entered.  The mail details of the specification of the connector are provided at the connector release level.  A connector can have only one 'live' release and there may be previous deprecated versions.

There may also be a draft release which is a pending update or extension to the connector. Pushing the draft release live will cause the current live release to be deprecated.

When a release is pushed live this might be done as a major release which will cause an 'update available' message to appear on all steps on templates and live integartions using the connector.  A major release should generally be used when existing methods need to be updated.  A minor release can be used when there are no changes are being made (or very minor changes are being made) to existing methods but new functionality is being added.

## Connector Settings

| Property | Description | Recommended Standards |
| --- | --- | --- |
| Name | The name of the connector that will be used in the interface. | This should not include the API Version. |
| Description | Description of the product. | Take this from the application's website. |
| API Verion | Version should be same as API version| |
| Icon | The logo that will be used to represent the application. | Logo should be 400x400 .png |

## Release Settings

| Property | Description | Recommended Standards |
| --- | --- | --- |
| Status | Unknown, Approved, Beta, Planned | |
| Comments | A description of the Application.| |
| Post install Property Value Lookup Method | | |
| Post Install Test Auth Method | | |
| Inbound Paging? | Does the API support paging when large amounts of data are requested? | |
| Inbound Page Size | If inbound paging is supported, provide the default page size. | |
| Outbound Page Size | If outbound paging is supported, provide the default page size. | |
| User Singular Partner Webhook URL? | | |
| Icon | The logo that will be used to represent the application. | Logo should be 400x400 .png |

## Related Topics

[Paging](./connector-paging)  

