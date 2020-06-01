---
title: Connector Rate Limits
sidebar: cyclr_sidebar
permalink: connector-rate-limits
tags: [connector-creation]
---

## Rate Limits

Cycle allows you to enter any limitations on the frequency with which API calls will be accepted by an applicaiton.  These settings can be made for the connector overall and, if required, differnt rates can be set for specific methods.

When setting up a connected you can set a rate limit with the scope of 'Account Connector' which is the overall setting.  THe rate can be specified in one of two ways:

* Maximum Requests per Second
* Number of Seconds between Requests

If the appropriate vales are set then Cyclr will not make calls if the rate would be exceeded, and this will mean that requests are queued.
