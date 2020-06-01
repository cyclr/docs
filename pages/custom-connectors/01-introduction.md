---
title: Connector Introduction
sidebar: cyclr_sidebar
permalink: connector-introduction
tags: [connector-creation]
---

## What is a Cyclr Custom Connector?

A custom connector allows you to integrate apps that aren’t in our [connector library](http://cyclr.com/connectors/). You can even add connectors for your own private apps and websites. Our Connector Manager makes this task quicker and easier to maintain than writing a traditional coded integration.  Note that not all price plans include access to the Custom Connector builder or that access is subject to an additional fee

A connector a standardised definition in a propriatory Cyclr format of the methods and fields of an API. Once created Cyclr takes care of everthing that is needed to work with an API including:

| Property | Description | 
| --- | --- |
| Description | Name, description version etc. of the Application's API |
| Authentication Method | How the connector should connect to the target API (e.g. OAuth, API key, login, etc). |
| Rate limiting & Throttling | How frequetly it is allowed to make calls to the API. |
| Methods / Endpoints | The endpoints for the API. |

If available in your console, access to Custom Connectors is available in the Console under 'Connectors'.

## Manual Connector Creation

Custom Connectors can be created manually by a process of specification.  This means that you are not 'coding' the connector but rather filling out series of forms that collect information about the specification of each aspect of the connector.

## Importing an API

Our powerful OpenAPI discovery tool lets you import an existing API specification into Cyclr. Currently, we support OpenAPI Version 2.0 in JSON and YAML.

If you are using another version, please convert it to an OpenAPI 2.0 file using third-party tools.
You can choose Create Connector to start with an empty connector if you don’t have an OpenAPI specification.

After importing the connector it is generally required to go through a 'tidy up' excercice to bring it up to standard.
