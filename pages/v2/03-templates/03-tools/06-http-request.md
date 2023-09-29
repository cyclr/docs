---
title: HTTP Request
sidebar: cyclr_sidebar
permalink: http-request
menus:
    template-tools:
        title: HTTP Request
        identifier: http-request
        toggleonly: menutoggleonly
        weight: 6
---
{::options parse_block_html="true" /}
<section class="card">

The HTTP Request step allows you to make a HTTP request to a specified host. This means that, instead of requesting a method from the Cyclr Support team, you can create a custom method yourself. You can use a HTTP Request for individual cases, such as to create a custom method for a single use, to go to a single endpoint, or to retrieve a specific set of data.

If you want a connector with more customization options, or for more extensive use, see the documentation on how to [Create a custom connector](custom-connectors).

</section>
<section class="card">

## Set up the HTTP Request step

The HTTP Request step has four different tabs in the **Step setup** window to configure the method. You can use the red **Previous** and **Next** buttons at the bottom of the window to switch between the tabs.

### Setup

You can use the following fields to set up and configure your custom method.

| **Field** | **Description** |
|---|---|
| Name | Name the method to help you identify it. |
| Description | You can write a description of the method. |
| Method Type | Select a type of method you want to create from the dropdown menu. |
| Endpoint | Enter the endpoint for the method call. |
| Authentication Type | Select the type of authentication you want to use from the dropdown menu. |
| Authentication values | Depending on the **Authentication Type** that you select, Cyclr might display fields for you to select which authentication values the connector requires to authenticate. For more information on authenticating with the Cyclr API, see the page on [API authentication](cyclr-api-authentication). |

### Add Method

You can paste JSON data into the **JSON Request** box. Cyclr uses this data to generate fields for the method. To respond to a webhook, you need to add fields to the step.

Cyclr returns the response as either JSON, XML, or as form encoded data. You can use the `Accept` HTTP header in the request to specify which format the response is in.

### Authenticate/Finish

The **Authenticate/Finish** tab provides fields for you to enter your authentication values and authenticate the step. These fields change dependent on the **Authentication Type** and **Authentication Values** that you select on the [Setup](#setup) tab.

> **Note**: For more information on authenticating connectors, you can view the [Authentication](account-connector-authentication) section of the Cyclr documentation.

Select the **Create** button on this tab to save any changes that you’ve made to the HTTP Request step. Cyclr displays a spinner with the message **Creating Quick Connector**. When the creation of the step completes, Cyclr directs you to the **Field Mapping** tab.

### Field Mapping

The **Field Mapping **tab is only visible after you add a method and select **Next** on that tab. When you configure your **HTTP Request** step, you can map the fields in the same way as a standard method step.

For more information, see the Cyclr documentation on how to [map fields](field-mapping).

**Note**: To use the created fields to map subsequent steps, you can select **HTTP Request** as the Source.

</section>
<section class="card">

## Limitations

Since your user’s template builder isn’t upgraded to 2.0 yet, your users can’t edit cycles with this step. This means you can only use the **HTTP Request ** step if you have access to the console. 

If they don’t have access, the application redirects them to the list of cycles. While cycles including these steps are visible, the **Edit** and **Copy** buttons are disabled.

</section>