---
title: IP Restrictions
sidebar: cyclr_sidebar
permalink: ip-restrictions
tags: [cyclr-config]
menus:
    cyclr-configuration:
        title: IP Restrictions
        identifier: ip-restrictions
        toggleonly: menutoggleonly
        weight: 7
---
{::options parse_block_html="true" /}
<section class="card">

You can use IP restrictions to further secure your Cyclr console and any calls that you make with the Cyclr API

</section>
<section class="card">

## API and Console

 By default, Cyclr doesn’t restrict access by IP address. 

To restrict who can access both your API calls and your partner console, you can add approved IP addresses. If you add IP restriction to either the API or console, only those IP addresses have access.

To add an approved IP address:

1. Select the red **+** button on the relevant card. 
2. Enter the IP address or CIDR. <br>**Note**: This dialogue shows your current IP address.
3. Select **Add**.

</section>
<section class="card">

## API - Call Non-Native Connector Methods

Cyclr blocks APIs that call non-native connector methods by default. To edit access for these APIs, make a request with [Cyclr’s support team](https://support.cyclr.com/hc/en-us).

</section>