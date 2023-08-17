---
title: Template versioning
sidebar: cyclr_sidebar
permalink: integration-template-versioning
tags: [templates]

menus:
    test-templates:
        title: Integration template versioning
        identifier: integration-template-versioning
        toggleonly: menutoggleonly
        weight: 3
---
{::options parse_block_html="true" /}
<section class="card">

You can use template versioning to organize and iterate your integrations. 

Cyclr locks live releases of a template to avoid errors, but you can copy them as **Draft** releases to build on your integrations and test new additions.

</section>
<section class="card">

## Template Releases Orientation 

To access the **Template Releases** page:

1. Go to **Templates** > **Template Library**.
2. Select the **View Folder** icon on the template you want to view.
3. Select the **Releases** clock icon.

![Annotated screenshot of the template release screen.](./images/Template-Release-Screen.png)

1. View the status of the template release.
2. View and edit the release notes for the template release.
3. View the audit trail of who created the release, when they created it, and when it was last run.
4. View the icons of the connectors that the release uses.
5. Promote a [draft release](#template-drafts) to live. 
6. Edit the template release in the workflow builder.
7. Run or pause the template release.
8. View the template release report.
9. [Copy](#copy-templates) the template release.
10. Export the release.
11. Delete the template release.
12. View the template release in the workflow builder (Live and [Deprecated](#deprecated-releases) releases are read only).

</section>
<section class="card">

## Template drafts

A published template provides the **Live** version of the integration template to your customers. To make sure that you don’t have to take down a published template, you can select the **Copy Release** button to create a **Draft** version to make any necessary updates. 

To make the updates accessible to new user installations, promote the draft version to live.

</section>
<section class="card">

## Deprecated releases

When you promote a draft release to a live release, Cyclr marks the previous live release as **Deprecated**. Deprecated releases allow you to track your development progress. A deprecated release is locked so you can’t edit it, but you can still create a copy and promote it to revert changes.

</section>
<section class="card">

## Copy templates

When you copy a template release you can create a draft version, but you can also do the following:

* Create a new template from your template release.
* Copy your template release into another template.
* Use the template release to create a new template in another Cyclr console if you have access to multiple consoles.

You can copy template releases to quickly create new releases for similar integrations.

</section>
<section class="card">

## Related pages

* [Import or export templates](template-export-import).
* [Copy cycles as templates](copy-account-cycle).

</section>
