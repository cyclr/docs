---
title: Script Tester
sidebar: cyclr_sidebar
permalink: script-tester
tags: [connector, script testing]
menus:
  cylr:
    title: Script Tester
    url: /script-tester
---

If you need to test some javascript outside of your cycle, you can do so with the **Script Testing** Tool.

This can be found in your **Console**, under the **Connectors** menu. 

![Script Testing Menu Location](./images/script-testing-menu.png)

You should start with an example object (XML/JSON etc) to run your tests on.

This might be a request from a method you wish to call, or the response from said call.

### Using the Script Testing Tool

1. Click `Global` and paste in the object, ensuring you assign the correct datatype, and give it a useful name.<br>
    ![Global Object Setup](./images/global-object-setup.png)
2. Use the left pane to enter your javascript function(s), and in the text box above, call the method (no brackets required).<br>
    ![Declare Function](./images/declare-function.png)
3. Click **Run**, and if your javascript is valid, you will see its output in the right-hand pane.<br>
    ![Output Pane](./images/output-pane.png)
4. You can now continue to adjust your script until you're happy with the output, pressing **Run** whenever you wish to update the output.<br>
    ![Example Script Test](./images/example-script-test.png)

For more on scripting, see [Connector Scripting](https://docs.cyclr.com/connector-scripting)
