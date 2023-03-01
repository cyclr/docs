---
title: Eventbrite information
sidebar: cyclr_sidebar
permalink: eventbrite-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">

## Event custom objects

The Eventbrite connector uses Cyclr custom objects to make methods dynamic based on an event ID. Each event custom object requires its corresponding event ID to function. This enables  Cyclr to automatically map custom fields for each event custom object you create.

### Find the event ID

You need an event ID to set up a custom object. To find a specific event ID:

1. Log into your Eventbrite account.
2. In the top navigation bar, mouse over the account name and select **Manage my events**.
3. Select the event you want to create a custom object for.
4. The URL to the page of this event contains the event ID required to set up a custom object in the form `?eid=<event ID>`. For example, if the URL of an event is `https://www.eventbrite.co.uk/myevent?eid=328737431507` then the module name is `328737431507`.

### Set up a custom object

When you set up a custom object it creates a new method category with the parameters you enter. To set up a custom object:

1. Go to the Eventbrite connector **Settings** page:
    - For template connectors: **Cyclr Console** > **Templates** > **Template Connectors** > **Eventbrite** > **Edit Connector**.
    - For connectors within a cycle: **Cycle Builder** > **Application Connectors** > **Eventbrite** > **Settings**.
2. Under the **Methods and Fields** heading, expand the **Events (custom object)** category.
3. Select the red **Copy this Category to create a Custom Object Category** icon.
4. Enter the event ID into **Specify object name**.
5. Select **Copy**.

### Change the custom object display name

To change the display name of a custom object method category:

1. Expand the method category by selecting the method category name.
2. Select the **Edit this Custom Object Category** icon.
3. Move the **Object Name** field to the **Object Value** field.
4. Change the **Object Name** field as required. This does not require a specific format.
5. Select **Save**.

</section>
