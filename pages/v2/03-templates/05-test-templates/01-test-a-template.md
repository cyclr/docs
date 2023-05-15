---
title: Test a template
sidebar: cyclr_sidebar
permalink: testing-a-template
tags: [templates]
menus:
    test-templates:
        title: Test a template
        identifier: testing-a-template
        toggleonly: menutoggleonly
        weight: 1
---
{::options parse_block_html="true" /}
<section class="card">
## Testing Steps

You can test the steps in your template, by clicking their “play” button.

### Test an Action Step

To test a step, you need to map it's required fields and then select the **Test Step** icon. This opens a window where you can enter some test data. Select **Run** in order to see the test output.

![A screenshot of the step testing window. ](./images/test-action-step.png)

### Test a Get Step

To test a trigger step, map the required fields and select the **Test Step** icon to test whether the step can retrieve the right data from the application.

Notes:

*   Cyclr may only return a small part of the data; usually the first “page”
*   Steps that get _new_ or _updated_ records, will in fact always return some data (such that you can review it)


</section>
<section class="card">
## Run a Template

Once correctly setup  you can click the 'run' button for your template to make it live and ready to receive data. Normally when testing it is normal to use the 'run once' option.


</section>
