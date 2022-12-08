---
title: FMX Authentication
sidebar: cyclr_sidebar
permalink: fmx-connector
tags: [connector]
---

<a name="fmx-set-up"></a>

# FMX set up

You need the following information to set up the FMX connector:

1. The **FMX Subdomain** of the account. For example, an account under https://cyclrtesting.gofmx.com/ has an FMX subdomain of `cyclrtesting`.
2. The **Username** and **Password** of the account.

These are given/set on FMX account creation. Clients should ask their FMX account manager if they require help obtaining these.

# Cyclr set up

To set up the FMX connector within Cyclr:

1. Go to your **Cyclr Console**.
2. Select the **Connectors** dropdown menu at the top of the page.
3. Select **Application Connector Library**.
4. Use the search bar to find the FMX connector.
5. Select the **Setup Required** button.
6. Enter the following values from the previous section:
    - **FMX Subdomain**: The FMX subdomain.
    - **Username**: The FMX username.
    - **Password**: The FMX password.
7. Select **Next**.

The FMX connector is now set up! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

# FMX custom objects

The FMX connector uses Cyclr custom objects to make methods dynamic based on module names. Each custom object name requires:

-   [The module name](#find-the-module-name) that work requests are taken from.
-   [The request type ID](#find-the-request-type-id) of the request type that custom fields are taken from.
    Note: Module names and request type IDs can be different for each client account.

<a name="find-the-module-name"></a>

## Find the module name

You need a module name to set up a custom object. To find a specific module name:

1. Log into your FMX account.
2. In the left-hand navigation menu, locate the requests module that you want to use as a custom object.
3. The URL to the page of this module contains the module name required to set up a custom object in the form `/<module name>-requests`. For example, the URL of **Maintenance Requests** is `https://cyclrtesting.gofmx.com/maintenance-requests` and the module name is `maintenance`.

<a name="find-the-request-type-id"></a>

## Find the request type ID

You need a request type ID to set up a custom object. Before you can find the request type ID:

-   [Install and authenticate the FMX connector](#fmx-set-up).
-   [Find the module name](#find-the-module-name).

To find a specific request type ID:

1. Go to the FMX connector **Settings** page:
    - For template connectors: **Cyclr Console** > **Templates** > **Template Connectors** > **FMX** > **Edit Connector**.
    - For connectors within a cycle: **Cycle Builder** > **Application Connectors** > **FMX** > **Settings**.
2. Run the **List Request Types** method under **Methods and Fields** > **Utilities** to return a list of request types and request type IDs. For example, the `Appliance` request type has a request type ID of `363065`.

## Set up a custom object

When you set up a custom object it creates a new method category with the parameters you enter. To set up a custom object:

1. Go to the FMX connector **Settings** page:
    - For template connectors: **Cyclr Console** > **Templates** > **Template Connectors** > **FMX** > **Edit Connector**.
    - For connectors within a cycle: **Cycle Builder** > **Application Connectors** > **FMX** > **Settings**.
2. Under the **Methods and Fields** heading, expand the **Work Requests (Custom Object)** category.
3. Select the red **Copy this Category to create a Custom Object Category** icon.
4. Enter the module name, followed by a dot, and then the request type ID into **Specify object name**. For example, for the `maintenance` module and request type ID `363065`, enter `maintenance.363065`.
5. Select **Copy**.

### Change a custom object display name

To change the display name of a custom object method category:

1. Expand the method category by selecting the method category name.
2. Select the **Edit this Custom Object Category** icon.
3. Move the **Object Name** field to the **Object Value** field.
4. Change the **Object Name** field as required. This does not require a specific format.
5. Select **Save**.
