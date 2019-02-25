---
title: Customising The Appearance of Launch
---

To view an instance of LAUNCH from within the Cyclr Console, go to:

Click “**Guide**” > Click the “**Show**” button under Integrate with your App > Click the “**Try LAUNCH**” button for an instance to appear as a pop up with any integration templates you’ve published.

As standard, the layout and colour scheme are pretty bland, however you can reskin your version of LAUNCH using CSS and HTML.

In the Console, click **Settings** and then **Appearance Settings**.

This screen will present you with several areas where you can paste code.

### Available CSS Classes

To restyle the LAUNCH layout add CSS to “**Application Custom CSS**”

Here are some of the available elements within LAUNCH you may want to customise.

<table>
    <tr>
        <th>Element</th>
        <th>CSS Class</th>
        <th>Explanation</th>
    </tr>
    <tr>
        <td>Create/Active Button</td>
        <td>.btn-success</td>
        <td>This button is used by the user to select an integration template to setup and activate.</td>
    </tr>
    <tr>
        <td>LAUNCH Background</td>
        <td>body.launch</td>
        <td>Using this allows you to edit the background and colour settings of your instance of LAUNCH.</td>
    </tr>
    <tr>
        <td>Application Icons</td>
        <td>.icon-sm</td>
        <td>Allows you to alter how the application logos are displayed.</td>
    </tr>
    <tr>
        <td>Integration Template Description</td>
        <td>.template-description</td>
        <td>Update the font format for integration descriptions.</td>
    </tr>
</table>

**Example**

    .btn-success {
        background-color: #d27;
        border-color: #d27;
        color: #fff;
    }

    body.launch {
        background-color: #f6f27f;
        padding: 20px 20px 20px 20px;
    }

Adding a Custom Header and Footer to LAUNCH
-------------------------------------------

You can further customise your LAUNCH instance by creating your own custom header and footer using HTML.

There are separate blocks in the Appearance Settings page for both Header and Footer.

Use both of these sections to add any custom messages or images you need to display to your users.

**Example**

<div class="header"> 

<h2>Test Heading</h2>

<p>This is a test message to show your users. You can add instructions for how to set up integrations here.</p>

</div>

By wrapping your message in a custom Div you can add stylings to the “**Application Custom CSS**” code block to further customise your message. In this case, this was added:

    .header {
        padding: 20px 0 20px 0;
    }

LAUNCH Complete HTML
--------------------

This section allows you to display a message to your user once they have successfully installed an integration template.

Design your message and HTML and paste it in this box (in “**Appearance Settings**”), making sure you add any CSS definitions in the **Application Custom CSS** code block.