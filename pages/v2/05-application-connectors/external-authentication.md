---
title: External Authentication
sidebar: cyclr_sidebar
permalink: external-authentication
tags: [authentication]
layout: page
menus:
  mainmenu:
    title: External Authentication
    overview: External authentication
    identifier: external-authentication
    icon: navconnectors
    weight: 4
---
{::options parse_block_html="true" /}
<section class="card">

## Overview
The external authentication feature needs to be turned on for each individual Partner. 
To do this you will need to speak to the admin to enable External Authentication of Connectors setting. 

## Using External Authentication
If you wish to authenticate one or more of your Connectors externally, Cyclr is equipped to handle this. 
The External Authentication feature allows the authentication credentials of a connector to be set and passed into an individual step, rather than relying on the connector to be authenticated beforehand. This means that different credentials can be used each time the cycle is run. Within the Step Setup of a Connector, there is a setting under Advanced Settings called "Use External Authentication". Enabling this feature will refresh the modal and display any Parameters related to Authentication. The Parameters that appear can then be setup like any other field mapping. These values are normally returned by the third-party provider when authenticating the Connector using Cyclr. However, when using this feature, the values will need to be obtained manually and entered into the newly provided parameters. If you wish to return to using Cyclr for authentication handling, you will need to remove the previous values provided; disabling "Use External Authentication" will not be enough.

**Notes**
1. Turning on "Use External Authentication" within a step will remove the restriction of requiring the connector to be authenticated before the Cycle can be run. However, some other functions within Cyclr, like testing methods outside of the builder, will require the connector to be authenticated.
2. Even if you turn off "Use External Authentication" within a step and leave the mapping of one or more of the authentication parameters, this will still get used when the cycle runs. Any authentication mappings will need to be manually removed/unmapped to use all the authentication values from the installed connector.

</section>
<section class="card">
