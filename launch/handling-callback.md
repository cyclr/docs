---
title: Handling Launch Callback
---

The final window of the LAUNCH flow is completely customizable and influenced by the HTML entered at:

**Console > Settings > Customize Appearance > Launch Complete HTML**

JavaScript is also supported.

Example:
```
    <h1>Congrats - you're connected!</h1>
    <button onclick="closeWindow();">OK</button>
    <script type="text/javascript"> 
        function closeWindow() {
            window.opener.postMessage(JSON.stringify(result), '\*');
            window.close(); 
        }
    </script>
```

In the example above, some simple HTML is displayed to the end user with a button that, when clicked, calls the _closeWindow()_ function, which:

*   Posts result back to the window that opened the LAUNCH flow popup (i.e. the host application); and
*   Closes the LAUNCH flow popup.

The result object has the following properties:

<table>
    <tr>
        <th>Property</th>
        <th>Description</th>
        <th>Example</th>
    </tr>
    <tr>
        <td>cycleId</td>
        <td>The Id of the newly installed integration within your end user’s account</td>
        <td>user@example.com</td>
    </tr>
    <tr>
        <td>status</td>
        <td>A string indicating the status of the newly installation integration cycle.By design, will always be active, unless an issue arose during installation, in which case it will be paused.</td>
        <td>active</td>
    </tr>
    <tr>
        <td>webhooks</td>
        <td>An array of URLs representing the endpoints of the webhooks included within the newly installed integration template.
This is important where your application needs to send data to Cyclr to trigger the newly installed integration template.
Where the newly installed integration template makes use of more than one webhook, the order of the URLs in this array matches the order of the webhook steps in the template.</td>
        <td>["https://webhooks.cyclr.com/Jd78JHd9"]</td>
    </tr>
</table>

### Cross domain issue in IE10

Internet Explorer 10 does not allow window.opener.postMessage() to be used from a page on a different domain to the opener. There are ways around this to enable the result of the LAUNCH flow to be posted back to your application.

#### **Proxy iFrame**

Instead of creating a popup to the LAUNCH URL directly, you should create a popup to a page on your own domain, with the LAUNCH URL embedded as an iFrame. Your JavaScript on the LAUNCH Complete page then posts to window.parent.postMessage() – which is supported across domains in IE – with the proxy page passing the data back to your app, either directly on the backend or using window.opener.postMessage().

#### **Redirect after LAUNCH Complete page**

JavaScript in the LAUNCH Complete page redirects your user to a page on your domain, passing in the result of the LAUNCH flow. That page then handles the details on your backend before closing the popup.