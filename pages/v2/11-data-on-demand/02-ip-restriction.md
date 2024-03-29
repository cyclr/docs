---
title: IP restriction
sidebar: cyclr_sidebar
permalink: ip-restriction
tags: [data-on-demand]

menus:
    data-on-demand:
        title: IP restriction
        identifier: ip-restriction
        toggleonly: menutoggleonly
        weight: 2
---
{::options parse_block_html="true" /}
<section class="card">
## Native connectors

You can call native connectors with the `IsPartnerIntegrationConnector` flag set to `true` from any IP address.


</section>
<section class="card">
## Third party connectors
Cyclr restricts IP access to Cyclr APIs used for passing requests to external applications. The IP restricted APIs are:

*  `GET /v1.0/account/connectors/{id}/methods/{methodId}` 
*  `POST /v1.0/account/connectors/{id}/methods/{methodId}`
*  `GET /v1.0/account/connectors/{id}/test/{methodId}`
*  `POST /v1.0/account/connectors/{id}/test/{methodId}`

To use Cyclr APIs to call standard connectors, such as third party connectors, you can only make the Cyclr API request from an IP address approved by Cyclr. 

To get your IP address approved, you can contact the Cyclr support team through the **Help** button in the documentation sidebar or in the Cyclr console. If you can’t access the **Help** button, you can email help@cyclr.com instead.


</section>
<section class="card">
## Related page

*  [API authentication](cyclr-api-authentication)

</section>
