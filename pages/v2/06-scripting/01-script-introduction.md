---
title: Script introduction
sidebar: cyclr_sidebar
permalink: script-introduction
tags: [templates]

menus:
    scripting:
        title: Script introduction
        identifier: script-introduction
        toggleonly: menutoggleonly
        weight: 1
---
{::options parse_block_html="true" /}
<section class="card">

Cyclr uses Javascript, which you can use to interact with the data that you send and receive to external applications. This means that you can ensure that you send and receive valid data.

</section>
<section class="card">

## Inline script

You can use inline scripts to make changes to data directly in a mapping field.

For inline script, you need to prefix the script with `=` (an equals sign). To prevent carriage returns or broken scripts, you can use <code>`</code> (backticks) characters around string values that you merge in.

For example:

`=(100 * 2)` <br> or <br> <code>=`[Mergefield]` === '' ? 'no value' : `[Mergefield]`;</code>

> **Note**: The `[Mergefield]` in the example represents the value that Cyclr uses when you map a field with the **Type a Value** option and select from the dropdown box.

For more complex scripts, or scripts that apply to multiple fields, you can use [Step script](#step-script) instead.

</section>
<section class="card">

## Step script

You can use step scripts to make complex changes to data. Step scripts can be easier to read than multiple inline scripts and there may be a performance advantage to using one set of Step Script instead of multiple inline scripts.

You can add step scripts from the builder:

1. Select **Step Setup** on a step in your cycle.
2. Select **Advanced Settings** to expand the section.
3. Enter script or additional functions to interact with Cyclr events.

</section>
<section class="card">

## Connector script

When you build a custom connector, you can add script directly to the Connector’s definition.

To add the script, go to the **Scripting** tab of the Connector builder, or add the script within individual methods.

</section>
<section class="card">

## Event Handlers

Cycles trigger events at certain points when the cycle runs, which means that you can modify data with Javascript functions called **event handlers**.

There are three ways that you can add event handlers when you work on a custom connector:

* If you add the event handler to a connector release, Cyclr calls the event handler for each method.
* If you add the event handler to a method in a connector, Cyclr only calls the event handler for that specific method.
* If you add the event handler through a step’s **Step Setup** window, Cyclr only calls the event handler for that specific step.<br>       **Note**: To add an event handler to a specific step, open the **Step Setup** window and select **Advanced Settings** to expand that section.

### Example

```js

function before_action() {

    /* Handle event here */

    return true;

}

```

Sometimes, when you pass a value from a `before_action` handler to an `after_action` handler, you can’t put the value in the `method_request` object as part of the request as the API you call may interpret it as invalid data. Instead, you can use the `method_request_mergefields` object as it persists  across the two events. The `script_parameters`  object, for example, is doesn’t persist across any events.<br>


### Event Handler order

If you add an event handler to more than one level for the same event, such as at connector level and method level, Cyclr calls all of the event handlers.

Cyclr calls event handlers in a specific order:



* Events beginning with `before`, such as `before_action`.

	**Method** > **Connector** > **Builder step**



* All other events, such as `after_action`:

    **Connector** > **Method** > **Builder step**

</section>
<section class="card">

## Limitations

### Execution time

The execution time for scripts is 60 seconds to avoid delays.


### External HTTP requests

For security, Cyclr uses the same authentication method as the connector and the same authentication value as when the connector was authenticated by the user. You can’t use script to access or modify the authentication values.


### `cycle_variables` object

The `cycle_variables` object is only available through the **Advanced Settings** of a step, and not through an inline script. Any changes you make to the `cycle_variables` object are not persisted.
