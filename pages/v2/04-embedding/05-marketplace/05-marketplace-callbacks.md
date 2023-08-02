---
title: Marketplace callback
sidebar: cyclr_sidebar
permalink: marketplace-callback
tags: [marketplaces]
menus:
    marketplace:
        title: Marketplace callback
        identifier: marketplace-callback
        toggleonly: menutoggleonly
        weight: 5
---
{::options parse_block_html="true" /}
<section class="card">

When your user installs an integration package from the Marketplace, this process either redirects your user back to the Marketplace, or displays a completion message.

</section>
<section class="card">

## Customize Marketplace callback

When you complete the installation of Marketplace integration packages, your user sees the final page of the LAUNCH flow. 
If you don’t redirect your user back to the Marketplace, you can customize this callback.

1. Go to your console and select **Settings** > **Appearance Settings**.
2. In the **Launch Complete HTML** box, define the HTML and JavaScript.

</section>
<section class="card">

## Message examples

### Plain HTML message

You can display your own message:

`<h1>Congrats - you're connected!</h1>`
<br>

### Integration package message

If your Marketplace integration package includes an install complete message, you can use the InstallCompleteMessage merge field to display messages for each integration package:

`<h1><span>{{InstallCompleteMessage}}<span\></h1>`
<br>

### JavaScript `postMessage`

If you use a popup window, you can display a message with a close button. When your user selects the close button, a JavaScript `postMessage` sends the result object and closes the popup window.

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
</section>
<section class="card">

## JavaScript result object

A JavaScript result object is available to the window on the final page of the Marketplace flow. You can use the result object for more processes, such as to update newly installed Cycles to complete their setup.

### Properties

<table width="100%">
	<col style="width:25%">
	<col style="width:25%">
	<col style="width:50%">
<thead>
  <tr>
    <th colspan="2">Property</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="2"><code>accountId</code></td>
    <td>Identifies the account that you installed the Marketplace integration package into.</td>
  </tr>
  <tr>
    <td colspan="2"><code>accountApiId</code></td>
    <td>Displays the API ID of the account you installed the Marketplace integration package into.</td>
  </tr>
  <tr>
    <td colspan="2"><code>installCompleteMessage</code></td>
    <td>Displays the install complete message for the Marketplace integration package.</td>
  </tr>
  <tr>
    <td colspan="2"><code>marketplacePackageId</code></td>
    <td>Identifies the Marketplace integration package.</td>
  </tr>
  <tr>
    <td colspan="2"><code>userId</code></td>
    <td>Identifies your end user.</td>
  </tr>
  <tr>
    <td colspan="2"><code>cycles</code></td>
    <td>Shows the array of cycles you installed as part of the Marketplace integration package.</td>
  </tr>
  <tr>
    <td></td>
    <td><code>cycleId</code></td>
    <td>Identifies the cycle you installed.</td>
  </tr>
  <tr>
    <td></td>
    <td><code>status</code></td>
    <td>Displays the status of the cycle you installed.</td>
  </tr>
  <tr>
    <td></td>
    <td><code>templateId</code></td>
    <td>Identifies the template you installed the cycle from.</td>
  </tr>
  <tr>
    <td></td>
    <td><code>templateReleaseId</code></td>
    <td>Identifies the template release you installed the cycle from.</td>
  </tr>
  <tr>
    <td></td>
    <td><code>webhooks</code></td>
    <td>Displays the array of webhooks the cycle contains.</td>
  </tr>
  <tr>
    <td></td>
    <td><code>webhooks.stepName</code></td>
    <td>Names the webhook step.</td>
  </tr>
  <tr>
    <td></td>
    <td><code>webhooks.url</code></td>
    <td>Displays the webhook’s URL.</td>
  </tr>
  <tr>
    <td colspan="2"><code>errors</code></td>
    <td>Displays the array of error messages when Cyclr activates the newly installed Marketplace Integration Package.</td>
  </tr>
</tbody>
</table>


</section>
<section class="card">

## Cross domain issue in Internet Explorer
Internet Explorer  doesn’t allow you to use `window.opener.postMessage()` from a page that’s on a different domain to the opener. You can avoid this problem in two ways.

### Proxy iFrame

You can create a popup to a page on your domain with the Marketplace URL embedded as an iFrame. If you embed the URL, your JavaScript posts to `window.parent.postMessage()`, which is supported across domains. The proxy page then passes the data back to your application either directly on the backend or with `window.opener.postMessage()`. 

### Redirect after LAUNCH complete
You can use JavaScript in the LAUNCH complete page to redirect your user to a page on your domain, and pass the data from the LAUNCH flow. The new page handles the details on your backend before it closes the popup.

</section>