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

To view your data retention settings for your overall application, go to **Settings** > **Data Retention** in your Cyclr console. From the **Data Retention** page, you can specify how long you retain data on both successful and errored transactions.

 You can use the toggles to turn data retention on or off. The default data retention time for accounts is 31 days. To set different data retention times for both successful and errored transactions, enter an integer into the first field and select the unit of time from the dropdown options: 
 
 *  **Hours**
 *  **Days**
 *  **Weeks**

</section>
<section class="card">

## Data retention for specific cycles and accounts

Cyclr uses the value you set on this page as the new default data retention time for cycles, however you can alter the value for specific cycles or accounts:

* To change your [data retention settings for a specific cycle](template-settings), select **Settings** and then select the **Data Retention tab**.
* To change your data retention settings for a specific customer account, go to **Accounts** > **Account Management**. Select the **Settings** cog icon, and scroll down to the relevant toggles.
 
</section>