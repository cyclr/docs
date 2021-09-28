---
title: Handling Launch Callback
sidebar: cyclr_sidebar
permalink: handling-callback
tags: [launch]
---

The final page of the LAUNCH flow is completely customizable and defined by the HTML &amp; JavaScript entered at:

**Console > Settings > Customize Appearance > Launch Complete HTML**

### Example Launch Complete HTML

#### Plain HTML Message

The most basic example is to simply display a completed message.

````html
<h1>Congrats - you're connected!</h1>
````

#### JavaScript postMessage

If LAUNCH was opened in a popup you can use javascript to send the result of the LAUNCH back to your application. This example displays a message to the user with a close button, when the user closes the button the result is sent using JavaScript postMessage and the popup window is closed.

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

A JavaScript **result** object is made avalible to the window on the final page of the LAUNCH flow, it has the following properties.

| Property | Description | Example |
| --- | --- | --- |
| accountId | The ID of your end user's account | xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx |
| accountApiId | The API ID of your end user's account | CYCLR_ACCOUNT_API_ID |
| cycleId | The ID of the newly installed integration within your end user's account | xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx |
| status | A string indicating the status of the newly installation integration cycle.By design, will always be Active, unless an issue arose during installation, in which case it will be stopped. | Active or Stopped |
| userId | The ID of your end user | xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx |
| webhooks | An array of URLs representing the endpoints of the webhooks included within the newly installed integration template. This is important where your application needs to send data to Cyclr to trigger the newly installed integration template. Where the newly installed integration template makes use of more than one webhook, the order of the URLs in this array matches the order of the webhook steps in the template. | ["https://webhooks.cyclr.com/Jd78JHd9"] |
| errors | An array of error messages when Cyclr activates the newly installed integration template. | ["Please set up all the steps correctly before starting the cycle."] |
| completeParameter | The value of the CompleteParameter provided in the LAUNCH API call. | |

### Cross domain issue in IE10

Internet Explorer 10 does not allow window.opener.postMessage() to be used from a page on a different domain to the opener. There are ways around this to enable the result of the LAUNCH flow to be posted back to your application.

#### Proxy iFrame

Instead of creating a popup to the LAUNCH URL directly, you should create a popup to a page on your own domain, with the LAUNCH URL embedded as an iFrame. Your JavaScript on the LAUNCH Complete page then posts to window.parent.postMessage() – which is supported across domains in IE – with the proxy page passing the data back to your app, either directly on the backend or using window.opener.postMessage().

#### Redirect after LAUNCH Complete page

JavaScript in the LAUNCH Complete page redirects your user to a page on your domain, passing in the result of the LAUNCH flow. That page then handles the details on your backend before closing the popup.
