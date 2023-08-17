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

## Related page

*  [Template versioning](integration-template-versioning)

</section>
