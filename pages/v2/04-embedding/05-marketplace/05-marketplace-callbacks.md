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
Customize Marketplace callback

When you complete the installation of Marketplace integration packages, your user sees the final page of the LAUNCH flow. 
If you don’t redirect your user back to the Marketplace, you can customize this callback.

1. Go to your console and select **Settings** > **Appearance Settings**.
2. In the **Launch Complete HTML** box, define the HTML and JavaScript.

### Message examples

#### Plain HTML message

You can display your own message:

`<h1>Congrats - you're connected!</h1>`

#### Integration package message

If your Marketplace integration package includes an install complete message, you can use the InstallCompleteMessage merge field to display messages for each integration package:

`<h1><span>{{InstallCompleteMessage}}<span\></h1>`

#### JavaScript `postMessage`

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

| **Property** | **Description** |
|:---|:---|
| `accountId` | Identifies the account that you installed the Marketplace integration package into. |
| `accountApiId` | Displays the API ID of the account you installed the Marketplace integration package into. |
| `installCompleteMessage` | Displays the install complete message for the Marketplace integration package. |
| `marketplacePackageId` | Identifies the Marketplace integration package. |
| `userId` | Identifies your end user. |
| `cycles` | Shows the array of cycles you installed as part of the Marketplace integration package. |
| `cycles.cycleId`	 | Identifies the cycle you installed. |
| `cycles.status`	 | Displays the status of the cycle you installed. |
| `cycles.templateId` | Identifies the template you installed the cycle from. |
| `cycles.templateReleaseId` | Identifies the template release you installed the cycle from. |
| `cycles.webhooks` | Displays the array of webhooks the cycle contains. |
| `cycles.webhooks.stepName` | Names the webhook step. |
| `cycles.webhooks.url` | Displays the webhook’s URL. |
| `errors` | Displays the array of error messages when Cyclr activates the newly installed Marketplace Integration Package. |

</section>