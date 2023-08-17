---
title: Template Library
sidebar: cyclr_sidebar
permalink: template-library
tags: [templates]

menus:
    manage-templates:
        title: Template Library
        identifier: template-library
        toggleonly: menutoggleonly
        weight: 1
---
{::options parse_block_html="true" /}
<section class="card">

From the **Template Library** page, you can see all of your template integrations. The table shows any tags you add to each template, and any connectors that they use. Each template also has the following options that you can use to manage and configure your integrations:

| **Option** | **Action** |
|---|---|
| **Edit Most Recent Draft** | Opens the most recent draft of the integration template in the template builder so that you can edit it. |
| **Releases** | Opens the **Template Releases** page where you can version your template integrations. For more information, see the page on [template versioning](integration-template-versioning). |
| **Move Template** | Opens a dropdown box of your folders so that you can select one to move the template integration to. |
| **Upgrade Installed Integrations** | Upgrades all of the existing integrations to the latest live version of the template. The integrations retain **User Configurable** variables and mapping variables, but this overwrites any other values. |
| **Delete Template** | Removes the template from your **Template Library**. This doesn’t remove instances of the template from your customer accounts. |
| **Published/Unpublished** toggle | Determines whether a template is published and available for your customers to install, or whether it’s unpublished and not ready for publication. |

</section>
<section class="card">

## Tag templates

Under the name of the template, there is a **Tag Template** icon. When you provide your templates to your customers through one of Cyclr’s [embedding](embed-cycles) options, you can use these tags to filter the templates. 
For example, you can configure the LAUNCH API call to only present templates that you tag in a particular way.

</section>