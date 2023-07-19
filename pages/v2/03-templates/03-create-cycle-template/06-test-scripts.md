---
title: Test scripts
sidebar: cyclr_sidebar
permalink: script-tester
tags: [templates]
menus:
    create-cycle-templates:
        title: Template scripts
        identifier: script-tester
        toggleonly: menutoggleonly
        weight: 6
---
{::options parse_block_html="true" /}
<section class="card">

You can add Javascript to steps within your cyclr to change how you process data. You can do this through the field mapping, or you can add step script through the **Advanced Settings** section of the **Step Setup** window. For more information on scripting in Cyclr and to view the script reference pages, see the section on [scripting](scripting).

</section>
<section class="card">

## Script Testing

If you need to test some javascript outside of your cycle, you can do so with the **Script Testing** Tool.

In your console, go to **Connectors** > **Script Testing**.

You can start with an example object (XML/JSON etc) to run your tests on. This might be a request from a method you wish to call, or the response from said call.

### Use the Script Testing tool

1. Select the **Global** button and paste in the object. Ensure that you assign the correct datatype, and give it a useful name.

<img src="./images/global-object-setup.png" alt="Global Object Setup." width="400px">

2. Use the left pane to enter your javascript function(s), and in the text box above, call the method (no brackets required).
3. Select the green **Run** button, and if your javascript is valid, you will see its output in the left side pane.
4. You can now continue to adjust your script. Select **Run** when you want to update the output.
    ![Example Script Test](./images/example-script-test.png)

</section>
