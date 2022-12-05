---
title: Handling Marketplace Callback
sidebar: cyclr_sidebar
permalink: marketplace-handling-callback
tags: [marketplaces]
menus:
  embedded-marketplace:
    title: Handling Marketplace Callback
    url: marketplace-handling-callback
---

Marketplace Integration Packages are installed using the LAUNCH flow.  After installation is complete, LAUNCH will either redirect the user back to the Marketplace or display the LAUNCH complete page. If the Marketplace Integration Package is not set to redirect the user back to the Marketplace, then the final page of the LAUNCH flow can be customized by defining the HTML &amp; JavaScript at:

**Console > Settings > Customize Appearance > Launch Complete HTML**

### Example Launch Complete HTML

#### Plain HTML Message

The most basic example is to simply display a completed message.

````html
<h1>Congrats - you're connected!</h1>
````

#### Integration Package Message

If the Marketplace Integration Package includes an install complete message, you can display custom messages for each Integration Package by using the InstallCompleteMessage mergefield.

````html
<h1>{% raw %}{{InstallCompleteMessage}}{% endraw %}</h1>
````

#### JavaScript postMessage

If the Marketplace was opened in a popup, you can use JavaScript to send the "result" of the installation back to your application.  If a popup wasn't used, then the **result** object is available straightaway.  The example below displays a message to the user with a close button.  When the user clicks the button, the **result** object is sent using a JavaScript **postMessage** and the popup window is closed.

```html
    <h1>Congrats - you're connected!</h1>
    <button onclick="closeWindow();">OK</button>
    <script type="text/javascript"> 
        function closeWindow() {
            window.opener.postMessage(JSON.stringify(result), '\*');
            window.close(); 
        }
    </script>
```

### JavaScript result object

A JavaScript **result** object is made available to the window on the final page of the Marketplace/LAUNCH flow.  It has the following properties and can be used to perform further processing such as updating newly installed Cycles to complete their setup:

| Property | Description | Example |
| --- | --- | --- |
| accountId | The ID of the Account that the Marketplace Integration Package was installed into | xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx |
| accountApiId | The API ID of Account that the Marketplace Integration Package was installed into | CYCLR_ACCOUNT_API_ID |
| installCompleteMessage | The install complete message for the Marketplace Integration Package | Integration is now active |
| marketplacePackageId | The ID of the Marketplace Integration Package | 1 |
| userId | The ID of your end user | xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx |
| cycles | Array of cycles that where installed as part of the Marketplace Integration Package |  |
| cycles.cycleId | ID of the installed cycle | xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx |
| cycles.status | Status of the installed cycle | Active or Stopped |
| cycles.templateId | ID of the template that the cycle was installed from | xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx |
| cycles.templateReleaseId | ID of the template release that the cycle was installed from | xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx |
| cycles.webhooks | Array of webhooks that a cycle contains |  |
| cycles.webhooks.stepName | Name of the step the webhook is for | Webhook |
| cycles.webhooks.url | URL of the webhook | https://my.cyclr.com/api/webhook/abcdefg123 |
| errors | An array of error messages when Cyclr activates the newly installed Marketplace Integration Package. | ["Please set up all the steps correctly before starting the cycle."] |

### Cross domain issue in IE10

Internet Explorer 10 does not allow window.opener.postMessage() to be used from a page on a different domain to the opener. There are ways around this to enable the result of the Marketplace LAUNCH flow to be posted back to your application.

#### Proxy iFrame

Instead of creating a popup to the Marketplace URL directly, you should create a popup to a page on your own domain, with the Marketplace URL embedded as an iFrame. Your JavaScript on the LAUNCH Complete page then posts to window.parent.postMessage() – which is supported across domains in IE – with the proxy page passing the data back to your app, either directly on the backend or using window.opener.postMessage().

#### Redirect after LAUNCH Complete page

JavaScript in the LAUNCH Complete page redirects your user to a page on your domain, passing in the result of the LAUNCH flow. That page then handles the details on your backend before closing the popup.
