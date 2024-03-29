---
title: Marketplace settings
sidebar: cyclr_sidebar
permalink: marketplace-settings
tags: [marketplaces,embedding]
menus:
    marketplace:
        title: Deploy Settings
        identifier: marketplace-settings
        toggleonly: menutoggleonly
        weight: 3
---
{::options parse_block_html="true" /}
<section class="card">

You can access your Marketplace settings in two ways:

* From the console, go to **Embedding** > **Marketplaces**, select the `...` icon for the Marketplace you want to view, and select **Settings** from the dropdown.
* From within the Marketplace in the console, select the **Settings** button in the top right corner. 

</section>
<section class="card">

## Marketplace settings

From the **Marketplace Settings** page, you can edit the name and description of your Marketplace. 

The subsequent fields are filled with default values for the terms that your Marketplace displays. You can edit any of these to customize your Marketplace. You can also define the number of columns that you display your cards in. 

The last field is the **Marketplace Notification URL**. This is the URL that Cyclr sends a message to in order to update you on the usage of your Marketplace.

Underneath the fields, there are a series of toggle settings that you can turn on or off:

| **Toggle setting** | **Description** |
|---|---|
| **Integration Package Details View** | Enables you to view installed cycles for a Marketplace package so you can see how your customers use your Marketplace. |
| **Installing Package View Enabled** | Displays a spinner when your user installs a package. |
| **Integration Package Configuration View** | Allows you to see the variables your user enters when they install a package. |
| **Wizard Mappings View Enabled** | Displays field mappings in a wizard instead of a single page when the customer installs a package. |
| **Data Type Mismatch Warnings Enabled** | Indicates if the data type warning should be shown during mapping when a customer installs your Marketplace. |
{: .two-col .col2-75 }

**Note**: Use the breadcrumb navigation at the top of the window to exit the settings page.

</section>
<section class="card">

## Category settings

You can edit the amount of columns in your Marketplace, which determines how many cards you can display on each row. If you set an amount here, it overrides the value set under **Marketplace settings**.

**Note**: These appearance settings apply to your Marketplace as a whole, but you can still set different appearance settings for specific categories if you want to. To access a category’s settings, select **Edit** > **Edit Category** and then select the **Settings** button.


There are two toggle settings you can use to determine how your customer navigates your Marketplace:

* **Auto-Generated Filter**: Generates a filter based on the tags you use in your Marketplace.
* **Search Enabled**: Adds a search bar to the top of your Marketplace so your customers can search for specific cards.

### HTML

You can add **Header** and **Footer** HTML to your Marketplace to customize it. For more information on how to further customize your Marketplace, see the page on how to [style your Marketplace with custom CSS](customize-marketplace).

</section>