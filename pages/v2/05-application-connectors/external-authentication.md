---
title: External Authentication
sidebar: cyclr_sidebar
permalink: external-authentication
tags: [authentication]
layout: page
menus:
  connector-authentication:
    title: External Authentication
    overview: External authentication
    identifier: external-authentication
    weight: 4
---
{::options parse_block_html="true" /}
<section class="card">

## Overview

If you have a need to set connector authentication credentials on individual steps (perhaps for testing an unauthenticated Connector) you can use the **External Authentication** feature.

Please contact Support if you would like this feature to be turned on for your account.

</section>
<section class="card">

## Using External Authentication

With Cyclr's External Authentication feature, you can set connector authentication credentials on individual steps.

You can use different credentials each time the cycle is run, and do not need to authenticate the connector beforehand.

</section>
<section class="card">

## Enable External Authentication

1. Go to the Step Setup
2. Go to Advanced Settings
3. Check the "Use External Authentication" setting
4. The modal refreshes to display any Parameters related to Authentication
5. Setup the Parameters like any other field mapping

Normally the third-party provider returns the values when Cyclr's connector authentication is successful. 

With External Authentication, you obtain the values manually and enter them into the newly provided parameters.

**Note**

External Authentication removes the requirement to authenticate the step's connector before the Cycle runs. Some other functions within Cyclr, such as testing methods outside of the builder, do require the connector to be authenticated.

</section>
<section class="card">

## Disable External Authentication

To return to using Cyclr for authentication handling, you must:

1. Remove the previous values provided
2. Uncheck "Use External Authentication" setting

**Note** 

If you disable "Use External Authentication" but leave any authentication parameter mappings, the cycle continues to use these. Remove all authentication mappings to use all of the installed connector's authentication values.

</section>
