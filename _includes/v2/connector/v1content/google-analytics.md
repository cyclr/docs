
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

See the [Google Authentication](https://docs.cyclr.com/google-authentication) documentation for more information.


</div>

</section>

<section class="userguide" markdown="1">

## User Guide

<div class="section-content" markdown="1">

### List Metrics Method

This method uses [UA Query Explorer](https://ga-dev-tools.web.app/query-explorer/).

Use this to interact with the [Core Reporting API](https://developers.google.com/analytics/devguides/reporting/core/v3/). Build queries to get data from your Google Analytics views (profiles). 

Use these queries in any client libraries to build your own tools.

### Request Fields Setup

There are four required fields.

![Set up request fields](./images/GA_List_Metrics_request_fields.png)

- Profile ID: Select Look Up option.

![Set up request fields](./images/GA_Profile_lookup.png)

Then select the desired Profile ID.

![Profile ID](./images/GA_ProfileID_select.png)

- Start Date: Start date for fetching Analytics data.
- End Date: End date for fetching Analytics data..
- Metrics: A list of comma-separated metrics, ie. users,sessions. For a comprehensive list of Metrics option see [UA Dimensions & Metrics Explorer](https://ga-dev-tools.web.app/dimensions-metrics-explorer/)

### Custom Method Setup

[UA Query Explorer](https://ga-dev-tools.web.app/query-explorer/) is a tool to produce custom reports.

It is not feasible to implement a single method which fits every type of report. 

Add custom fields to the connector methods to access the required data. See the instructions in our guide [Adding Custom Fields](https://docs.cyclr.com/adding-custom-fields) to implement this functionality.

### Producing a [UA Query Explorer](https://ga-dev-tools.web.app/query-explorer/) Report

For every "Metrics" and "Dimensions" field in a report, add a custom field with the format: [rows].fieldName, e.g. `[rows].users`. Add the field name without `ga:`.

For example, to retrieve a report using `Users` and `Sessions` metrics, and `UserType` and `SessionCount`dimensions.

![Added Custom Fields](./images/GA_Added_Custom_Fields.png)

Once the Custom Fields are added to the method  they can be used in a cycle, to map data from one step to another.
