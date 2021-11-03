---
title: Last Successful Run Date
sidebar: cyclr_sidebar
permalink: last-successful-run-date
tags: [lsrd last successful run date]

---

### Last Successful Run Date

If you have a need for a method that only pulls the latest information, you're going to want to use Cyclr's **Last Successful Run Date** functionality.

You may for instance want **List New Contacts** or **List Updated Accounts** methods.

Where a particular endpoint accepts a date as a parameter, you can enter the Last Successful Run Date as a mergefield.

See the example API call below:

* ht<span/>tps://ww<span/>w.api.com/contacts?$filter=createdDateTime ge **2021-11-02T14:32:02Z**

You can add the **Last Successful Run Date** mergefield directly to the endpoint in your connector like so:

* ht<span/>tps://ww<span/>w.api.com/contacts?$filter=createdDateTime ge **\{\{LastSuccessfulRunDate format=yyyy-MM-ddTHH:mm:ssZ\}\}**

Now every time a step uses this method, it will pull all contacts since *the last time this step successfully ran*.

> It's important to note that **Last Successful Run Date** always refers to the last time a particular **Step** successfully ran, not a **Cycle**.

If you want to tell a step to use a particular date, you can use the Date Picker.

This can be found by going into Step Setup > Advanced Settings:

![Date Picker](./images/datepicker.png)

If this is left unchanged, a live run of the Cycle will set this value to the current time, and retrieve nothing.

The next full run of the Cycle will pick up any new data since the *first* run, and so on.

Clicking Step Test will use whatever date is in the picker, so 1970-01-01T00:00:00 if the cycle has never been run, and no value has been given.

#### Accessing Last Successful Run Date in script

Last Successful Run Date can be accessed in ``before_action`` functions by making reference to ``last_successful_run_date``.
