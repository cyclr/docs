---
title: Test templates
sidebar: cyclr_sidebar
permalink: testing-a-template
tags: [templates]
menus:
    test-templates:
        title: Test templates
        identifier: testing-a-template
        toggleonly: menutoggleonly
        weight: 1
---
{::options parse_block_html="true" /}
<section class="card">

You can test individual authenticated steps in your integration from the template builder. To test a step, select the **Test Step** play icon on the step.

</section>
<section class="card">

## Test steps

### Test a step with test data

You only need to enter test data for fields that don't have hard coded values, such as fields with sources from previous steps:

1. Make sure you map the required fields for the step you want to test.
2. Select the **Test Step** button and enter some test data in the dialogue that opens.
3. Select the **Run** button to see the test output.


### Test a trigger step

You can also test trigger steps to make sure that they can retrieve the right data from the third party application. 

The test output might only return a section of the data, usually the first page. Trigger steps that get new or updated records always return data for you to review, but if there are no new or updated records, Cyclr returns an empty object.

> **Note**: You need to authenticate the application connector to obtain data from the third party application.

</section>
<section class="card">

## Run a Template

To test your template integration before you publish it, select **Run** > **Run Once** in the top bar of the template builder.

</section>
<section class="card">

</section>
<section class="card">

## External Authentication

**Overview**
The external authentication feature needs to be turned on for each individual Partner. 
To do this you will need to navigate to **Admin > Partners > Edit Partner** and turn on the Enable External Authentication of Connectors setting. 

**Using External Authentication**
If you wish to authenticate one or more of your Connectors externally, Cyclr is equipped to handle this. The External Authentication feature allows the authentication credentials of a connector to be set and passed into an individual step, rather than relying on the connector to be authenticated beforehand. This means that different credentials can be used each time the cycle is run. Within the Step Setup of a Connector, there is a setting under Advanced Settings called "Use External Authentication". Enabling this feature will refresh the modal and display any Parameters related to Authentication. The Parameters that appear can then be setup like any other field mapping. These values are normally returned by the third-party provider when authenticating the Connector using Cyclr. However, when using this feature, the values will need to be obtained manually and entered into the newly provided parameters. If you wish to return to using Cyclr for authentication handling, you will need to remove the previous values provided; disabling “Use External Authentication” will not be enough.

**Notes**
1. Turning on “Use External Authentication” within a step will remove the restriction of requiring the connector to be authenticated before the Cycle can be run. However, some other functions within Cyclr, like testing methods outside of the builder, will require the connector to be authenticated.
2. Even if you turn off "Use External Authentication" within a step and leave the mapping of one or more of the authentication parameters, this will still get used when the cycle runs. Any authentication mappings will need to be manually removed/unmapped to use all the authentication values from the installed connector.

</section>
<section class="card">

## Related page

*  [Template versioning](integration-template-versioning)

</section>
