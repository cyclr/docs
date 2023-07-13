---
title: Data Retention
sidebar: cyclr_sidebar
permalink: console-data-retention-settings
tags: [cyclr-config]

menus:
    cyclr-configuration:
        title: Data Retention
        identifier: console-data-retention-settings
        toggleonly: menutoggleonly
        weight: 4
---
{::options parse_block_html="true" /}
<section class="card">

To view your data retention settings for your overall application, go to **Settings** > **Data Retention** in your Cyclr console. From the **Data Retention** page, you can specify how long you retain data on both **Successful Transactions** and **Errored Transactions**.

The default data retention time for accounts is 31 days, but you can use the toggles to turn data retention on or off, and you can set different data retention times for both successful and errored transactions. To set the time, enter an integer into the first field and select the unit of time from the dropdown options: **Hours**, **Days**, and **Weeks**.

</section>
<section class="card">

## Data retention for specific cycles and accounts

Cyclr uses the value you set on this page as the new default data retention time for cycles, however you can alter the value for specific cycles or accounts:

* To change your [data retention settings for a specific cycle](template-settings), select **Settings** and then select the **Data Retention tab**.
* To change your data retention settings for a specific customer account, go to **Accounts** > **Account Management**, select the **Settings** cog icon, and scroll down to the relevant toggles.
 
</section>