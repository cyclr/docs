---
title: Appearance Settings
sidebar: cyclr_sidebar
permalink: settings-appearance
tags: [settings]
---

Theses settings allow you to change the appearance of Cyclr when in accounts, using LAUNCH or Marketplace.

*Due to caching in Cyclr it will take a minute until the changes take effect.*

### Application LESS Variables

The simplist way to alter the appearance of Cyclr is to change the values of LESS variables.

For example if the *body-background* is set to *#ccc* then the background of Cyclr will change to grey

```` less
@body-background: #ccc;
````

![](/images/settings-appearance-less.png)

### Application Custom CSS

If changing the LESS variables is insufficient to provide the customization that you require you can also include you own custom CSS block, this will be included alongside the Application LESS so you can use both as required.

For example to change the rounded buttons to squares you could use

```` css
.btn-rounded {
    border-radius: 0;
}
````

![](/images/settings-appearance-css.png)

### Header HTML

Header HTML allows HTML & JavaScript to be injected into the header of the page.

```` html
<h1>This is a header</h1>
````

![](/images/settings-appearance-header-html.png)

### Footer HTML

Footer HTML allows HTML & JavaScript to be injected into the footer of the page.

```` html
<h1>This is a footer</h1>
````

![](/images/settings-appearance-footer-html.png)

### Launch Complete HTML

Launch Complete HTML allows for the changing of HTML & JavaScript that is displayed at the end of the install process for LAUNCH and Marketplace for more information See [Handling Launch Callback](/handling-callback)
