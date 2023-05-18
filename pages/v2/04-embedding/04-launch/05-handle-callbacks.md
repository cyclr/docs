---
title: Handle LAUNCH callbacks
sidebar: cyclr_sidebar
permalink: handling-callback
tags: [launch]
menus:
    launch:
        title: Handle callbacks
        identifier: handling-callback
        toggleonly: menutoggleonly
        weight: 5
---
{::options parse_block_html="true" /}
<section class="card">

You can fully customize the final page of the LAUNCH flow with HTML and Javascript. To customize the appearance in the Cyclr console, go to **Settings** > **Customize Appearance** > **Launch Complete HTML**.

</section>
<section class="card">

## Example Launch Complete HTML

### Plain HTML message

You can display your own message:

```html
<h1>Congrats - you're connected!</h1>
```

### JavaScript `postMessage`

If you use a popup window, you can display a message with a close button. When your user selects the close button, a JavaScript `postMessage` sends the result object and closes the popup window.

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

A JavaScript result object is available to the window on the final page of the Marketplace flow. You can use the result object for more processes, such as to update newly installed cycles to complete their setup.


<div class="tg-wrap"><table>
<colgroup>
       <col span="1" style="width: 20%;">
       <col span="1" style="width: 20%;">
       <col span="1" style="width: 60%;">
    </colgroup>
<thead>
  <tr>
    <th colspan="2"><strong>Property</strong></th>
    <th><strong>Description</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="2"><code>accountId</code></td>
    <td>The ID of your end user’s account</td>
  </tr>
  <tr>
    <td colspan="2"><code>accountApiId</code></td>
    <td>The API ID of your end user’s account</td>
  </tr>
  <tr>
    <td colspan="2"><code>cycleId</code></td>
    <td>The ID of the newly installed integration within your end user’s account</td>
  </tr>
  <tr>
    <td colspan="2"><code>status</code></td>
    <td>A string indicating the status of the newly installed integration. By design, will always be Active, unless an issue arose during installation, in which case it will be stopped.</td>
  </tr>
  <tr>
    <td colspan="2"><code>userId</code></td>
    <td>The ID of your end user</td>
  </tr>
  <tr>
    <td colspan="2"><code>webhooks</code></td>
    <td>An array of URLs representing the endpoints of the webhooks included within the newly installed integration template. This is important where your application needs to send data to Cyclr to trigger the newly installed integration template. Where the newly installed integration template makes use of more than one webhook, the order of the URLs in this array matches the order of the webhook steps in the template.</td>
  </tr>
  <tr>
    <td colspan="2"><code>errors</code></td>
    <td>An array of error messages when Cyclr activates the newly installed integration template.</td>
  </tr>
  <tr>
    <td colspan="2"><code>completeParameter</code></td>
    <td>The value of the CompleteParameter provided in the LAUNCH API call.</td>
  </tr>
    <tr>
    <td></td>
    <td><code>templateId</code></td>
    <td>The identifier of the template that the integration is installed from.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td><code>templateReleaseId</code></td>
    <td>The identifier of the template that the integration is installed from.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td><code>templateTags</code></td>
    <td>The tags from the template the integration is installed from.</td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>
</div>

</section>
<section class="card">

## Cross domain issue in Internet Explorer

Internet Explorer doesn’t allow you to use `window.opener.postMessage()` from a page that’s on a different domain to the opener. You can avoid this problem in two ways.

### Proxy iFrame

You can create a popup to a page on your domain with the Marketplace URL embedded as an iFrame. If you embed the URL, your JavaScript posts to `window.parent.postMessage()`, which is supported across domains. The proxy page then passes the data back to your application either directly on the backend or with `window.opener.postMessage()`.

### Redirect after LAUNCH Complete page

You can use JavaScript in the LAUNCH complete page to redirect your user to a page on your domain, and pass the data from the LAUNCH flow. The new page handles the details on your backend before it closes the popup.

</section>
