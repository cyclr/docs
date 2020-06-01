---
title: Integration Template Versioning
sidebar: cyclr_sidebar
permalink: integration-template-versioning
tags: [integration-cycles]
keywords: versioning, locked, template management, deprecated, integration management, template version
---

To help you and your team organise and iterate your integrations we have introduced integration template versioning to the Cyclr Console.

The new feature allows you to create Draft "releases" of an integration so you can build it out and test new additions, before locking it as a Live release. 

![](./images/live-template-workflow.png)

While Live releases cannot be edited, you can copy them to create an iterative new release. Once this has been built out as required, it can be set as the new Live version of the integration.

Combining this with our audit trail features, your whole team are able to build and work on integration templates, with their account details being assigned to a release for traceability.  



Template Releases Orientation 
-------------------

![](./images/Template-Release-Screen.png)

1.  Title of the template you are working on
2.  Status of the template release
3.  Release notes for template release (click on text to add/edit)
4.  Audit trail (see who created the release and when)
5.  The Connectors used in the template release
6.  Promote Draft release to Live
7.  Edit template release in the workflow builder
8.  Run or Pause the template release
9.  View template release Report
10. Copy template release (you can then choose whether to create a new Draft within the template, copy it to another template, or create a completely new template)
11. Delete template release
12. View template release in the workflow builder (Live and Deprecated releases are readonly) 



Published Templates
---------------

One of the main advantages of using the versioning feature is for updating your published Templates without having to take them down.

Published templates will always provide the Live version to your users when they choose to install one so you are able to create a Draft version, make any necessary updates and promote to Live to make it accessible to new user installations - without any downtime.

![](./images/Integration-Template-Releases.png)


Copying Templates
---------------

As a Live template release is automatically locked for editing, you can quickly create a new identical, editable version by copying it.

![](./images/live-template-workflow.png)

Clicking the copy button on a release also allows you to select where you want the new release to be copied to.

The default destination is the current template, however, you are also able to select other templates to copy your Draft release into as well as a creating a new template. This allows you to quickly create new releases for similar integrations, e.g if you are creating CRM integrations with your application and have created one, you can copy it to a new template, and swap out the CRM steps for the equivalent steps of another CRM connector.


Promoting Releases

Once you have promoted your release, the previous Live release will be marked as Deprecated and locked for editing.

![](./images/Integration-Template-Releases.png)

This allows you to keep a trail of your integration development progress so you can see what you we previously doing, while also being able to go back by creating a copy of a Deprecated release and promoting it to Live.
