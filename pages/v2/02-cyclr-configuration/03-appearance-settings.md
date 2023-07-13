---
title: Appearance settings
sidebar: cyclr_sidebar
permalink: console-appearance-settings
tags: [cyclr-config]

menus:
    cyclr-configuration:
        title: Appearance settings
        identifier: console-appearance-settings
        toggleonly: menutoggleonly
        weight: 3
---
{::options parse_block_html="true" /}
<section class="card">

To view the **Appearance Settings** page, go to **Settings** > **Appearance Settings** in your Cyclr console. 

From this page, you can customize how Cyclr appears when viewed from a customer account with [LAUNCH](launch) or [Marketplaces](marketplaces).

> **Note**: Due to caching in Cyclr, changes may take up to a minute to take effect.

</section>
<section class="card">

## Application LESS Variables

The first block on the page shows the LESS variables that you can use within Cyclr. You can edit any of these variables to alter the appearance of your application. 

### Example

For example, if you set `@body-background` to `#ccc` then application’s background changes to grey:

```css
@body-background: #ccc;
```

![A screenshot of Cyclr with a gray background.](/images/settings-appearance-less.png)

</section>
<section class="card">

## Application Custom CSS

If you want to customize your application further, you can add your own custom CSS in the **Application Custom CSS** block. The CSS works alongside the **Application LESS Variables** so you can use both methods together if you need to.

### Example

For example, you can add CSS to the application to change the shape of buttons to square:

``` css
.btn-rounded {
    border-radius: 0;
}
```

![A screenshot of Cyclr with square buttons.](/images/settings-appearance-css.png)

</section>
<section class="card">

## Header HTML

You can use the **Header HTML** block to inject both HTML and JavaScript into the header of your application. 

### Example

You can add a simple text header with HTML tags:

```html
<h1>This is a header</h1>
```

![A screenshot of the example header text.](/images/settings-appearance-header-html.png)

</section>
<section class="card">

## Footer HTML

You can use the **Footer HTML** block to inject both HTML and JavaScript into the footer of your application. 

### Example

You can add a simple text footer with HTML tags:

``` html
<h1>This is a footer</h1>
```

![A screenshot of the example footer text.](/images/settings-appearance-footer-html.png)

</section>
<section class="card">

## Launch Complete HTML

You can use the **Launch Complete HTML** block to add HTML and JavaScript to determine the appearance of the page that displays to your customers at the end of the install process through LAUNCH or Marketplaces. For more information, see the page on [Handling Launch Callback](handling-callback).

</section>
<section class="card">

## Connector Callback Error HTML

You can use the **Connector Callback Error HTML** block to add HTML that determines what the application displays when someone encounters an error when authenticating a connector.

You can use merge fields to include the specific error and description that returns from the third party application in your callback HTML:

* `{{error}}`
* `{{error_description}}`

For example:

```html
<p>The following error has occurred: {{error}} - {{error_description}}</p>
```

</section>
