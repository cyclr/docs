---
title: Customize appearance
sidebar: cyclr_sidebar
permalink: customising-launch
tags: [launch]
menus:
    launch:
        title: Customize appearance
        identifier: customising-launch
        toggleonly: menutoggleonly
        weight: 6
---
{::options parse_block_html="true" /}
<section class="card">

To preview an instance of LAUNCH in the Cyclr console, go to **Embedding** > **LAUNCH** and select the **Try LAUNCH** button.


This shows a pop up with any published integration templates that you have.

</section>
<section class="card">

## Customize LAUNCH

You can customize the appearance of your LAUNCH flow with CSS and HTML styling.

To edit the appearance of LAUNCH in the console, go to **Settings **> **Appearance Settings**. 

Application Custom CSS

To restyle your LAUNCH layout, you can add CSS to the **Application Custom CSS **field. You can use the following elements and classes to customize appearance:

| **Element** | **CSS Class** | **Explanation** |
|---|---|---|
| Create/Active Button | `.btn-success` | The button that the user uses to select an integration template. |
| LAUNCH Background | `body.launch` | The background and color settings of your instance of LAUNCH. |
| Application Icons | `.icon-sm` | The way in which LAUNCH displays application logos. |
| Integration Template Description | `.template-description` | The font format for integration descriptions. |

### Example styling

```css
    .btn-success {
        background-color: #d27;
        border-color: #d27;
        color: #fff;
    }

    body.launch {
        background-color: #f6f27f;
        padding: 20px 20px 20px 20px;
    }
```

</section>
<section class="card">

## Header HTML and Footer HTML

You can also use HTML to create your own custom header and footer for your version of LAUNCH.

On the **Appearance Settings** page, there are fields for both the **Header** and the **Footer**. You can use both of these fields to add custom messages or images that you want to display for your users.

### Example header

```html
<div class="header"> 

<h2>Test Heading</h2>

<p>This is a test message to show your users. You can add instructions for how to set up integrations here.</p>

</div>
```

If you want to add specific styling to a message, you can wrap the message in a custom `div`. This means you can add the styling to the **Application Custom CSS** field, like below:

```css
    .header {
        padding: 20px 0 20px 0;
    }
```

</section>
<section class="card">

## LAUNCH Complete HTML

You can use the **LAUNCH Complete HTML** field to customize the window that the user sees once they successfully install an integration through LAUNCH. You can add the HTML to this field, and add any CSS definitions into the **Application Custom CSS** field.

For more information on how to edit the LAUNCH Complete page, see the documentation on how to [handle LAUNCH callback](handling-callback).

</section>
