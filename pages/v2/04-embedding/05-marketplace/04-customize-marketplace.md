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

## Customize your Marketplace

In your Cyclr console, go to **Settings** > **Appearance Settings**. From this page, you can use the **Application Custom CSS** field to enter your customizations.

| **Element/Class Name** | **Description** |
|---|---|
| `launch` | Applies styling to the entire section of the web page with the class name launch. |
| `launch a` | Styles the anchor tags inside the launch section. |
| `marketplace-item` | Applies styling to the marketplace item section. |
| `marketplace-item img` | Styles the images inside the marketplace item section. |
| `marketplace-item-title` | Styles the title of the marketplace item section. |
| `marketplace-item-description` | Styles the description of the marketplace item section. |
| `marketplace-item a` | Styles the anchor tags inside the marketplace item section. |
| `#launchMapping h4` | Styles the h4 element inside the launchMapping section. |
| `section-block` | Applies styling to the section blocks of the web page. |
| `section-block-title` | Styles the title of the section blocks. |
| `section-block-title h4` | Styles the h4 element inside the section block titles. |
| `section-block-body` | Styles the body of the section blocks. |
| `form-group` | Styles the form groups in the web page. |
| `form-group label` | Styles the labels inside the form groups. |
| `icon-sm` | Styles the small icons in the web page. |
| `field-status-required` | Styles the required fields in the web page. |
| `alert-info` | Styles the alert messages in the web page. |
| `launch h3` | Styles the h3 element inside the launch section. |

### Example CSS

```
.marketplace-item {
  background-color: #f5f5f5;
  border: 1px solid #3c5064;
}

.marketplace-item img {
  padding-top: 25px;
  padding-bottom: 5px;
}

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

.launch .nav>li>a:hover {
  text-decoration: none;
  background-color: #f5f5f5;
  border-bottom: 0px;
  cursor: pointer;
}

.launch .nav>li>a.active {
  text-decoration: none;
  background-color: #fad5d5;
  border-bottom: 0px;
  cursor: pointer;
}

```

The previous CSS styling results in the following appearance for the Marketplace:

![An example screenshot of a Marketplace with custom styling.](./images/marketplace-styling-example.png)

</section>