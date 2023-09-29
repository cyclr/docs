---
title: Template versioning
sidebar: cyclr_sidebar
permalink: integration-template-versioning
tags: [templates]
keywords: versioning, locked, template management, deprecated, integration management, template version

menus:
    test-templates:
        title: Integration template versioning
        identifier: integration-template-versioning
        toggleonly: menutoggleonly
        weight: 2
---
{::options parse_block_html="true" /}
<section class="card">
To help you and your team organize and iterate your integrations we have introduced integration template versioning to the Cyclr Console.

The new feature allows you to create Draft "releases" of an integration so you can build it out and test new additions, before locking it as a Live release. 

While Live releases cannot be edited, you can copy them to create an iterative new release. Once this has been built out as required, it can be set as the new Live version of the integration.

Combining this with our audit trail features, your whole team are able to build and work on integration templates, with their account details being assigned to a release for traceability.  

</section>
<section class="card">

## Template Releases Orientation 

![Annotated screenshot of the template release screen.](./images/Template-Release-Screen.png)

1.  Status of the template release
2.  Release notes for template release (click on text to add/edit)
3.  Audit trail (see who created the release and when)
4.  The icons of the connectors used in the template release
5.  Promote Draft release to Live
6.  Edit template release in the workflow builder
7.  Run or Pause the template release
8.  View template release Report
9. Copy template release (you can then choose whether to create a new Draft within the template, copy it to another template, or create a completely new template)
10. Export the release
11. Delete template release
12. View template release in the workflow builder (Live and Deprecated releases are readonly) 

</section>
<section class="card">

## Published Templates

One of the main advantages of using the versioning feature is for updating your published Templates without having to take them down.

Published templates will always provide the Live version to your users when they choose to install one so you are able to create a Draft version, make any necessary updates and promote to Live to make it accessible to new user installations - without any downtime.

</section>
<section class="card">

## Copying Templates

As a Live Template Release is automatically locked for editing, you can quickly create a new identical, editable version by copying it.

Clicking the Copy Release button next to a Release allows you to select where you want the new release to be copied to.

The default destination is the current Template, however, you are also able to:
* create a new Template from your Release.
* copy your Release into another existing Template.
* create a new Template in another Cyclr Console if you have access to more than one.

This allows you to quickly create new releases for similar integrations, e.g if you are creating CRM integrations with your application and have created one, you can copy it to a new template, and swap out the CRM steps for the equivalent steps of another CRM connector.

</section>
<section class="card">

## Promoting Releases

Once you have promoted your release, the previous Live release will be marked as Deprecated and locked for editing.

This allows you to keep a trail of your integration development progress so you can see what you we previously doing, while also being able to go back by creating a copy of a Deprecated release and promoting it to Live.

</section>
