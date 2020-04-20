---
title: OpenAPI
sidebar: cyclr_sidebar
permalink: openapi
tags: [connector-creation]
---

## Introduction ##

In this guide, you will learn how to create your own custom connectors in Cyclr.
Importing an API

Our powerful OpenAPI discovery tool lets you import your existing API specification into Cyclr.
After signing into the Console, select Connectors > My Connectors > Generate From OpenAPI Specification.


![](./images/import-api-1.gif)

* We currently support OpenAPI Version 2.0 in JSON and YAML.
* If you are using another version, please convert it to an OpenAPI 2.0 file using third-party tools.
* You can choose Create Connector to start with an empty connector if you don’t have an OpenAPI specification.

## Connector Setup ##

There are a few things you may want to set up manually after importing your API:

* Authentication: if your API uses OAuth (1.0a or 2.0), you need to enter the Client ID, Client Secret, Authorise URL, Access Token URL and Request URL (only for OAuth 1.0a).
* Pagination: this is very handy if your connector is dealing with large data sets and requires paging parameters to be included in the request. Just set them up as parameters and turn on the Inbound Paging flag.
* Rate Limit: you can set a rate limit for your connector, e.g., 2 requests per second or 1 second between each request.

## Promote Connector Release ##

Cyclr uses release versioning to track connector history. Promote your draft release to a live release when you are happy with the connector setup.

![](./images/promote-connector.gif)

## Connector Testing ##

* Go to ``Templates -> Template Library`` and select ``Design New Template``.
* When you are in the builder, find ``Add Application`` from the sidebar.
* If you don’t see your connector in the list, check if you have promoted the draft release.
* Once your connector is installed, you will be taken back to the builder. You can then drag and drop methods onto the builder and test them.

There are a few ways to test a method:

* Use Step Testing and provide some mock values to test the endpoint. Make sure you have mapped all the required fields in Step Setup. Otherwise you won’t see the Step Testing button.
* Design an end-to-end integration and run it.

## Publishing Connectors ##

After you have tested your new connector, the last step you may want to do is to publish it into your user accounts.

* Go to Account Management under the Accounts dropdown in the Console.
* Sign in to the account that you wish to publish the connector in.
* Same as how you test a connector, open the builder and use Add Connector to install the connector in the user account.
