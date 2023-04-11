---
title: Errors
sidebar: cyclr_sidebar
permalink: cyclr-errors
tags: [managing-cyclr]

menus:
    about-cyclr:
        title: Errors
        identifier: cyclr-errors
        toggleonly: menutoggleonly
        weight: 5
---
{::options parse_block_html="true" /}
<section class="card">

## 429 "Too Many Requests" Errors

If Cyclr receives a 429 response during a call to a third party API, Cyclr waits `n` seconds before you can make another call. The amount of seconds is determined by the period of time the third party API tells Cyclr to wait in the `Retry-After`. If the third party API doesn't provide a `Retry-After`, Cyclr defaults to a 60 second wait time.

Cyclr logs a warning against any steps that attempt to call the API again before the wait time passes. The warning informs you that the call is blocked and that it can retry later.

If the third party API continues to respond with a 429 error after the wait period, Cyclr increases the wait time by an additional 1 minute, then 3 minutes, 7 minutes, 15 minutes and 30 minutes. Cyclr continues to retry these calls until they are successful.

</section>
