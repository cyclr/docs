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

![Profile ID](./images\GA_ProfileID_select.png)

- Start Date: Start date for fetching Analytics data.
- End Date: End date for fetching Analytics data..
- Metrics: A list of comma-separated metrics, ie. users,sessions. For a comprehensive list of Metrics option go to [UA Dimensions & Metrics Explorer](https://ga-dev-tools.web.app/dimensions-metrics-explorer/)
