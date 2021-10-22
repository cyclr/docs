---
title: Google Analytics Connector User Guide
sidebar: cyclr_sidebar
permalink: google-analytics-connector-user-guide
tags: [connector]
---

## Authentication

Follow the instructions in our guide [Google Authentication](https://docs.cyclr.com/google-authentication)

## List Metrics method

This method uses [UA Query Explorer](https://ga-dev-tools.web.app/query-explorer/), which is a tool that lets you interact with the [Core Reporting API](https://developers.google.com/analytics/devguides/reporting/core/v3/), by building queries to get data from your Google Analytics views (profiles). You can use these queries in any of the client libraries to build your own tools.

# Set up request fields

There are four required fields:

![Set up request fields](./images/GA_List_Metrics_request_fields)

- Profile ID: Select Look Up option.

![Set up request fields](./images/GA_Profile_lookup)

Then select the desired Profile ID.

![Profile ID](./images/GA_ProfileID_select.png)

- Start Date: Start date for fetching Analytics data.
- End Date: End date for fetching Analytics data..
- Metrics: A list of comma-separated metrics, ie. users,sessions. For a comprehensive list of Metrics option go to [UA Dimensions & Metrics Explorer](https://ga-dev-tools.web.app/dimensions-metrics-explorer/)

## Custom Method set up

[UA Query Explorer](https://ga-dev-tools.web.app/query-explorer/) is a tool to produce custom reports, because of this, a method that would fit every single report would not be feasible to implement. Cyclr connector allows its user to add custom fileds to a method.
Follow the instructions in our guide [Adding Custom Fields](https://docs.cyclr.com/adding-custom-fields) to have a better understanding of how this functionality works and could be applied to fullfill the user need.

# Producing a [UA Query Explorer](https://ga-dev-tools.web.app/query-explorer/) report

The fields we are focusing on this section are "Metrics" and "Dimensions". For every "Metrics" and "Dimensions" field we use in our report, a custom field must be added to the method with this form [rows].fieldName, ie. [rows].users (add the field name without "ga:").

As an example, we are going to retrieve a report using "Users" and "Sessions" metrics, and "UserType" and "SessionCount" dimensions.

![Added Custom Fields](./images/GA_Added_Custom_Fields.png)

Once the Custom Fields are added to the method, they can be used in a Cyclr cycle as current fields.
