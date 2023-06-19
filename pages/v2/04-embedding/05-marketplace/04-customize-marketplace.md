---
title: Style your Marketplace with custom CSS
sidebar: cyclr_sidebar
permalink: customize-marketplace
tags: [marketplaces,embedding]
menus:
    marketplace:
        title: Style your Marketplace with custom CSS
        identifier: customize-marketplace
        toggleonly: menutoggleonly
        weight: 4
---
{::options parse_block_html="true" /}
<section class="card">

## Style your Marketplace with custom CSS

In your Cyclr console, go to **Settings** > **Appearance Settings**. From this page, you can use the **Application Custom CSS** field to enter your customizations.

| **Elements/Classes** | **Description** |
|---|---|
| `.launch` | Applies styling to the entire section of the web page with the class name launch. |
| `.launch a` | Allows you to apply styling to the anchor tags inside the launch section. |
| `.marketplace-item` | Applies styling to the marketplace item section. |
| `.marketplace-item img` </br> `.marketplace-item-image img` | Allows you to apply styling to the images inside the marketplace item section. |
| `.marketplace-item-title` | Allows you to apply styling to the title of the marketplace item section. |
| `.marketplace-item-description` | Allows you to apply styling to the description of the marketplace item section. |
| `.marketplace-item a` | Allows you to apply styling to the anchor tags inside the marketplace item section. |
| `.marketplace-search` | Allows you to apply styling to the marketplace search input section. |
| `.marketplace-tags` | Allows you to apply styling to the marketplace item tags section. |
| `.marketplace-tag` | Allows you to apply styling to the individual item tags within the marketplace tags section. |
| `.marketplace-items` | Allows you to apply styling to the section containing the marketplace items. |
| `.marketplace-item-rich-text` | Allows you to apply styling to the individual rich text marketplace items. |
| `.marketplace-item-images` | Allows you to apply styling to the images section within a marketplace item. |
| `.marketplace-item-image` | Allows you to apply styling to the individual images within a marketplace item. |
| `.marketplace-item-footer` | Allows you to apply styling to the section at the bottom of a marketplace item. |
| `.marketplace-item-status` | Allows you to apply styling to the status section of a marketplace item. |
| `.label-status` | Allows you to apply styling to the individual status of a marketplace item. |
| `.marketplace-item-buttons` | Allows you to apply styling to the buttons section within a marketplace item. |
| `.marketplace-item-buttons` </br> `.btn` | Allows you to apply styling to the individual buttons with a marketplace item. |
| `.marketplace-item-buttons` </br> `.dropdown-menu` </br> `.dropdown-item` | Allows you to apply styling to the dropdown items within a marketplace item. |
| `#launchMapping h4` | Allows you to apply styling to the h4 element inside the launchMapping section. |
| `.section-block` | Applies styling to the section blocks of the web page. |
| `.section-block-title` | Allows you to apply styling to the title of the section blocks. |
| `.section-block-title h4` | Allows you to apply styling to the h4 element inside the section block titles. |
| `.section-block-body`| Allows you to apply styling to the body of the section blocks. |
| `.form-group` | Allows you to apply styling to the form groups in the web page. |
| `.form-group label` | Allows you to apply styling to the labels inside the form groups. |
| `.icon-sm` | Allows you to apply styling to the small icons in the web page. |
| `.field-status-required` | Allows you to apply styling to the required fields in the web page. |
| `.alert-info` | Allows you to apply styling to the alert messages in the web page. |
| `.launch h3` | Allows you to apply styling to the h3 element inside the launch section. |
{: .two-col .col2-75 }

</section>
<section class="card">

## Example CSS

```css
.marketplace-item-title {
  color: #3c5064;
  font-weight: normal !important;
  font-size: 16pt;
  padding-bottom: 5px;
}

.marketplace-item-description {
  color: #0096a5;
  font-weight: normal !important;
  text-align: left !important;
  padding-left: 10px;
  padding-right: 10px;
  line-height: 1.4em;
  margin-bottom: 2em;
  font-size: 14px !important;
}

.marketplace-item a {
  border: 1px solid #0096a5;
  background: #ffffff;
  color: #3c5064;
  border-radius: 25px;
}
```

</section>
<section class="card">

## LESS Variables

To view and edit the LESS variables that are available in Cyclr, go to **Settings** > **Appearance Settings** in the console and view the **Application LESS Variables** field.

Below is a list of all of the LESS variables that relate to Marketplaces:

```LESS
@marketplace-item-gutter-x: 12px;
@marketplace-item-gutter-y: 12px;

@marketplace-item-rich-text-h1-font-family: 'Inter', sans-serif;
@marketplace-item-rich-text-h1-font-size: 36px;
@marketplace-item-rich-text-h1-font-weight: 500;
@marketplace-item-rich-text-h1-margin: 0px 0px 6px 0px;

@marketplace-item-rich-text-h2-font-family: 'Inter', sans-serif;
@marketplace-item-rich-text-h2-font-size: 30px;
@marketplace-item-rich-text-h2-font-weight: 600;
@marketplace-item-rich-text-h2-margin: 0px 0px 6px 0px;

@marketplace-item-rich-text-h3-font-family: 'Inter', sans-serif;
@marketplace-item-rich-text-h3-font-size: 24px;
@marketplace-item-rich-text-h3-font-weight: 400;
@marketplace-item-rich-text-h3-margin: 0px 0px 6px 0px;

@marketplace-item-rich-text-h4-font-family: 'Inter', sans-serif;
@marketplace-item-rich-text-h4-font-size: 20px;
@marketplace-item-rich-text-h4-font-weight: 500;
@marketplace-item-rich-text-h4-margin: 0px 0px 6px 0px;

@marketplace-item-rich-text-h5-font-family: 'Inter', sans-serif;
@marketplace-item-rich-text-h5-font-size: 14px;
@marketplace-item-rich-text-h5-font-weight: 500;
@marketplace-item-rich-text-h5-margin: 0px 0px 6px 0px;

@marketplace-item-rich-text-p-font-family: 'Inter', sans-serif;
@marketplace-item-rich-text-p-font-size: 12px;
@marketplace-item-rich-text-p-font-weight: 500;
@marketplace-item-rich-text-p-margin: 0px 0px 12px 0px;

@marketplace-item-background-color: #FFFFFF;
@marketplace-item-border-color: #DBDCE0;
@marketplace-item-font: 'Inter', sans-serif;

@marketplace-item-title-font-color: #37474F;
@marketplace-item-title-font-size: 18px;

@marketplace-item-description-font-color: #777777;
@marketplace-item-description-font-size: 12px;

@marketplace-item-button-border-color: #DBDCE0;
@marketplace-item-button-font-color: #00A1E0;
@marketplace-item-button-font-size: 14px;
@marketplace-item-button-background-color: #FFFFFF;

@marketplace-item-dropdown-menu-background-color: #FFFFFF;
@marketplace-item-dropdown-menu-border-color: #DBDCE0;
@marketplace-item-dropdown-item-font-size: 12px;
@marketplace-item-dropdown-item-font-color: #37474F;

@marketplace-item-status-running-font-color: #FFFFFF;
@marketplace-item-status-running-background-color: #74B665;
@marketplace-item-status-paused-font-color: #FFFFFF;
@marketplace-item-status-paused-background-color: #E79950;
```

</section>