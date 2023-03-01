---
title: Podio information
sidebar: cyclr_sidebar
permalink: podio-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Obtain the App ID

The connector includes a method 'List Apps' which you can use to find the ID of the App you wish to interact with. If the App in question is not listed, you can find the ID manually in the following way:

1. Locate the App in the Podio interface.
2. select the wrench button at the top right of the sidebar.
3. Select **Developer**.

   ![podio interface](./images/podio_screenshot_1.png)

4. Copy the **App ID for (App Name)** value from the next page.

</section>
<section class="card">

## Rate limits

For most of the actions in this connector, Podio imposes a rate limit of 250 calls per hour. As a result, calls (including each page request) are staggered at 15 second intervals.

The maximum page size that Podio supports is 500 objects. If the response to your request contains less than 500 objects, the response isn't delayed.

</section>
