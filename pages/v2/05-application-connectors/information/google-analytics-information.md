---
title: Google Analytics information
sidebar: cyclr_sidebar
permalink: google-analytics-information-user-guide-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## List Metrics Method

This method uses [UA Query Explorer](https://ga-dev-tools.web.app/query-explorer/), which is a tool that lets you interact with the [Core Reporting API](https://developers.google.com/analytics/devguides/reporting/core/v3/) by building queries to get data from your Google Analytics views (profiles). You can use these queries in any of the client libraries to build your own tools.

### Request Fields Setup

There are four required fields:

![Set up request fields](./images/GA_List_Metrics_request_fields.png)

- Profile ID: Select Look Up option.

![Set up request fields](./images/GA_Profile_lookup.png)

Then select the desired Profile ID.

![Profile ID](./images/GA_ProfileID_select.png)

- Start Date: Start date for fetching Analytics data.
- End Date: End date for fetching Analytics data.
- Metrics: A list of comma-separated metrics, for example: `users,sessions`. For a comprehensive list of Metrics option go to [UA Dimensions & Metrics Explorer](https://ga-dev-tools.web.app/dimensions-metrics-explorer/)


</section>
<section class="card">

## Custom Method setup

[UA Query Explorer](https://ga-dev-tools.web.app/query-explorer/) is a tool to produce custom reports, so there isn't a specific method for each type of report. Instead, for each method in the connector, you can add custom fields. Please follow the instructions in the [Adding Custom Fields](https://docs.cyclr.com/adding-custom-fields) documentation to implement this functionality.


</section>
<section class="card">

## Produce a [UA Query Explorer](https://ga-dev-tools.web.app/query-explorer/) Report

For every **Metrics** and **Dimensions** field you use in your report, you need to add a custom field to the method with the format: `[rows].fieldName`, for example: `[rows].users` (add the field name without `ga:`).

For example, you can retrieve a report with the **Users** and **Sessions** metrics, and **UserType** and **SessionCount** dimensions.

![Added Custom Fields](./images/GA_Added_Custom_Fields.png)

Once you add the custom fields to the method, you can use the fields in a cycle to map data from one step to another.

</section>
