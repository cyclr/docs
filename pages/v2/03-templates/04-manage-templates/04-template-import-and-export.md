---
title: Import or export templates
sidebar: cyclr_sidebar
permalink: template-export-import
tags: [templates]
keywords: template management, integration management, template export, template import

menus:
    manage-templates:
        title: Import or export templates
        identifier: template-export-import
        toggleonly: menutoggleonly
        weight: 4
---
{::options parse_block_html="true" /}
<section class="card">
You can export templates from one Cyclr instance and import them to another. This allows you to keep templates in sync if you have Cyclr instances in multiple regions. For example, if you build a template on the UK instance and want to use the exact same template on the US instance, you can use the template export import feature.

To ensure that template you import are identical to the exported template, the generated file includes the details of the connector releases that the template uses.

> **Note**: Cyclr doesn't support account connector properties and webhook key mappings for the export/import functionality.

</section>
<section class="card">

## Export Template

You can export template releases from your Cyclr console. To export the template as a JSON file to download, find the template in the **Template Library**, select **Releases** and then select the **Export** button.

The screenshot below shows where you can find the export and import buttons on the **Template Releases** page:

![A screenshot of the template release screen with the import and export buttons highlighted.](./images/template-export.png)

</section>
<section class="card">

## Import Templates

You can import a template release JSON file as a new template, or into an existing template as a new release as in the screenshot above. 

To import a new template from a JSON file, go to **Templates** > **Template Library** in the console and select the **Import Template** button.

Cyclr displays an error message if there are any compatibility issues, for example, if the method can't be found on the current instance.

</section>
<section class="card">

## Related page

*  [Template versioning](integration-template-versioning)

</section>
