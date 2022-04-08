---
title: BigChange JobWatch
sidebar: cyclr_sidebar
permalink: bigchange-jobwatch
tags: [connector]
---

# Partner setup

## Getting your BigChange JobWatch API key

You will need to obtain your BigChange JobWatch API key to give Cyclr access to the BigChange JobWatch API. Contact your customer service representative to get this.

# Cyclr setup

## Connector installation

To set up the BigChange JobWatch connector within Cyclr:

1. Go to your **Cyclr Console**.
2. Click the **Connectors** dropdown menu at the top of the page.
3. Click **Application Connector Library**.
4. Use the search bar to find the BigChange JobWatch connector.
5. Click the **Setup Required** button.
6. Enter the following values:
    - **API Key**: Your BigChange JobWatch API key you obtained in the previous section.
    - **Username**: Your BigChange JobWatch username.
    - **Password**: Your BigChange JobWatch password.
7. Click **Next**.

Your BigChange JobWatch connector is now set up! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

## Custom fields

You can add custom fields to contacts, contact notes, and jobs in the following methods:

-   Create Contact
-   Update Contact
-   Update Contact Note
-   Create Job
-   Update Job

You can view custom fields for contacts, contact notes, and jobs in the following methods:

-   Get Contact
-   Get Contact Note
-   Get Job
-   List Contact Notes
-   List Contacts
-   List Group Jobs
-   List Jobs
-   List Jobs by Contact
-   Search Contacts
-   Search Contacts By Email
-   Search Contacts By Email, ID, Or Reference
-   Search Contacts By Phone Number
-   Search Contacts By Postcode

You can add custom fields to the above methods in the following way:

1. Go to the **Edit Connector** page for the BigChange JobWatch connector.
2. Under the **Methods & Fields** heading, locate the required method by expanding out the categories and method name.
3. Click the pink **+** button to add a method field.
4. Enter the following, repeating this for each BigChange JobWatch custom field you want to add:
    - **Field Location**: The custom field location, which must have the format "cust\_&lt;field name&gt;".
    - **Display Name**: The custom field display name.
    - **Description**: The custom field description.
    - **Data Type**: Text.
5. Click **Create**.

You must ensure the **Field Location** matches exactly for this to function. You can confirm that the custom fields are enabled by dragging the required method(s) into a cycle and viewing the **Step Settings**. You can find the custom fields at the bottom of the **Mappings** list.
