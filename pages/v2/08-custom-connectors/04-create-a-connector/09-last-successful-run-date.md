---
title: Last successful run date
sidebar: cyclr_sidebar
permalink: last-successful-run-date
tags: [connector-creation]

menus:
    create-a-connector:
        title: Last successful run date
        identifier: last-successful-run-date
        toggleonly: menutoggleonly
        weight: 9
---
{::options parse_block_html="true" /}
<section class="card">

## Last Successful Run Date

If you need a method that only pulls data generated after a specific time/date, you can use Cyclr's **Last Successful Run Date** functionality.

Multiple methods use the **Last Successful Run Date** function, for example, the **List New Contacts** and **List Updated Accounts** methods.

## Add Last Successful Run Date

If a particular endpoint accepts a date as a parameter, you can enter the **Last Successful Run Date** as a mergefield. See the example API call below:

    `ht<span/>tps://ww<span/>w.api.com/contacts?$filter=createdDateTime ge {2021-11-02T14:32:02Z}`

You can add the **Last Successful Run Date** mergefield directly to the endpoint in your connector:

    `ht<span/>tps://ww<span/>w.api.com/contacts?$filter=createdDateTime ge \{\{LastSuccessfulRunDate format=yyyy-MM-ddTHH:mm:ssZ\}\}`

If you add this method to a step, the step pulls all of the contacts that were added after the last time the step successfully ran.

> **Note**: **Last Successful Run Date** refers to the last time a particular **Step** successfully ran, not a **Cycle**.

## Use Last Successful Run Date

### Select a specific date

If you want a step to use a specific date, you can use the Date Picker. To use the date picker, go to **Step Setup** > **Advanced Settings**:

![Date Picker](./images/datepicker.png)

### Test steps

If you select **Test Step**, the step uses the **Last Successful Run Date** value set on the Step, but doesn't update the value afterwards. If you've never run the step before, and haven't given a value, the default date is `1970-01-01T00:00:00Z`.

`1970-01-01T00:00:00Z` (the UNIX Epoch), in Cyclr, indicates that no date/time value is set on a step. 

### Run a cycle

When you run a cycle, Cyclr uses the **Last Successful Run Date** value set on the step. If the value is `1970-01-01T00:00:00Z`, however, Cyclr updates the **Last Successful Run Date** value to the current date/time. This behavior prevents the step from trying to retrieve all existing data on the first run of a cycle.

> **Note**: If you do need to retrieve historical data on the first run of a step, you can use script on the step to have the first run start from a date in the past.

## Access Last Successful Run Date in script

The **Last Successful Run Date** function can be accessed in ``before_action`` functions by making reference to ``last_successful_run_date``.

</section>
