---
title: Template Export Import
sidebar: cyclr_sidebar
permalink: template-export-import
tags: [templates]
keywords: template management, integration management, template export, template import
menus:
  templates:
    title: Template Export Import
    url: /template-export-import
    weight: 9
---

You can export templates from one Cyclr instance and import them to another. This allows you to keep templates in sync if you have Cyclr instances in multiple regions.

For example, you build a template on the UK instance and want to use exactly the same template on the US instance. This can now be achieved using the template export import feature.

Export Template
---------------

Template releases can be exported within your Cyclr Console. Once you select Export, the template will be exported to a JSON file for downloading. Be aware of the limitations in the popup. See screenshot below for how to find the export button in Cyclr.

![](./images/templates/template-export.png)


Import Templates
----------------

A template release JSON file can be imported as a new template (see screenshot below), or into an existing template as a new release (see screenshot above). You will see an error message if there are any compatibility issues, e.g. method not found on the current instance.

![](./images/templates/template-import.png)
