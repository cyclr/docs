---
title: Template settings
sidebar: cyclr_sidebar
permalink: template-settings
tags: [templates]

menus:
    template-configuration:
        title: Template settings
        identifier: template-settings
        toggleonly: menutoggleonly
        weight: 1
---
{::options parse_block_html="true" /}
<section class="card">

To view and edit a template’s settings, select the **Settings** button from the top bar of the template builder page. This opens a window with several tabs that allow you to configure how this specific template integration works.

</section>
<section class="card">

## Settings Tab

### On Step Error

You can determine what happens when an integration flow encounters an error in an API call. 

| **Option** | **Description** |
|---|---|
| **Ignore** | No special action occurs if the cycle encounters an error. |
| **Retry After a Wait** | If the cycle encounters an error, Cyclr retries the call after a delay. You can set how many times that the cycle retries the call, and each attempt has an increasing delay.For example, the first retry occurs after 5 minutes, the second after a further 35 minutes, the third afters a further 1 hour and 35 minutes, then 4 hours 35 minutes, and the final call after 10 hours and 35 minutes. <br>**Note**: You can only select this option for a step that sends a single request. |
| **Stop The Integration** | If the cycle encounters an error, the entire integration stops. |
| **Stop the Transaction** | If the cycle encounters an error, only the specific transaction that caused the error stops and other transactions continue. |

### Log Step Requests

**Log Step Requests** is the default setting. When active, this setting means that your integration logs both the requests and the responses in the step data.


### Collection Splitting

| **Setting** | **Behavior** |
|---|---|
| **First (Trigger) Step** | Splits a collection of data on the first step in a cycle. |
| **All Steps** | Splits collections of data on all steps. |
| **None** | Doesn’t perform any collection splitting. |

For more information, see the documentation page on [Collection Splitting](collection-splitting).

</section>
<section class="card">

## Variables

You can define variables in the **Variables** tab and then use them in your integration. Once you define a variable, you can map fields with the variable in all the steps in the integration.

</section>
<section class="card">

## Data Retention

In the **Data Retention** tab, you can use the two toggles to set a specific time period to retain data on a step. You can set different time periods for data retention for **Successful Transactions** and **Errored Transactions**.

If you set a specific time in the cycle settings, this value overrides any global settings you have for your Cyclr application. Cyclr displays the current default value under the toggles.

For more information, see the Cyclr documentation on [data retention](https://docs.cyclr.com/console-data-retention-settings).

</section>
<section class="card">

## Audit Log

The **Audit Log** tab displays a log of key events that relate to the template integration. Each event records a **Username**, **Comment**, and **Timestamp** in relation to the event.

</section>
<section class="card">

## Connector Installation

The **Connector Installation** tab displays the connectors that you use in the integration. Each connector has a dropdown where you can select either **Existing Installation** or **Fresh Installation**. When you install the integration into an account, if the account already contains one of the connectors it needs, this setting determines whether the integration uses the existing version of the connector or installs a new version.

The default setting is to use existing connectors when possible.

</section>
