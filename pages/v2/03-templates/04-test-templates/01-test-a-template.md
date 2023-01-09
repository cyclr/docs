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

To test an action step, Cyclr will generate a form with the necessary fields. Add some test data and then hit the run button to see the result.

![](./images/test-action-step.gif)

### Test a Get Step

To test a Get step, click its play button. It will then connect to their app and attempt to get some data.

![](./images/test-get-step.gif)

Notes:

*   Cyclr may only return a small part of the data; usually the first “page”
*   Steps that get _new_ or _updated_ records, will in fact always return some data (such that you can review it)


</section>
<section class="card">
## Run a Template

Once correctly setup  you can click the 'run' button for your template to make it live and ready to receive data. Normally when testing it is normal to use the 'run once' option.


</section>
