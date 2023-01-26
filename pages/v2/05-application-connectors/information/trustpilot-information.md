---
title: Trustpilot information
sidebar: cyclr_sidebar
permalink: trustpilot-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Authorization

You need a **Business Unit ID** for most requests with the Trustpilot connector. Without the **Business Unit ID**, Trustpilot sends a `403 - Forbidden` response. You can find the **Business Unit ID** with the **Search For Business Units** method, or use the **Search For Business Units** method as the first step in your cycles.

> **Note**: Some endpoints are classified as **Private** by Trustpilot. This means that the logged in user needs permissions to access that Business Unit ID's data. If the logged in user doesn't have those permissions, the response is `403 - Forbidden`.

</section>
