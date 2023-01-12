---
title: Rate limits
sidebar: cyclr_sidebar
permalink: connector-rate-limits
tags: [connector-creation]
menus:
    create-a-connector:
        title: Rate limits
        identifier: connector-rate-limits
        toggleonly: menutoggleonly
        weight: 3
---
{::options parse_block_html="true" /}
<section class="card">
## Rate Limits

Cyclr allows you to enter any limitations on the frequency with which API calls will be accepted by an application.  These settings can be made for the connector overall and, if required, different rates can be set for specific methods.

When setting up a connector you can set a rate limit with the scope of 'Account Connector' which is the overall setting.  The rate can be specified in one of two ways:

* Maximum Requests per Second
* Number of Seconds between Requests

If the appropriate values are set then Cyclr will not make calls if the rate would be exceeded, and this will mean that requests are queued.

</section>
