---
title: Building Integration Templates
---

Integration Templates available in the LAUNCH flow are designed using the Cyclr drag-and-drop builder.

Integration Name
----------------

The name given to an Integration Template is presented to your end user on the integration selection screen during the LAUNCH flow.

  
![Template Name](./images/template_name.png)

  
Consider keeping integration template names concise, descriptive, and unique such that it is clear to your end user which selection is the most appropriate for their use case.

Integration Description
-----------------------

The Integration Description will be presented to your end users in future releases of the LAUNCH flow.

  
![Integration Description](./images/integration_description.png)

  
Use a description that helps your end user understand what the impact of installing this integration will be.

Integration publishing status
-----------------------------

The “_Integration Published_” toggle controls whether or not the integration is available for selection by our end user during the LAUNCH flow.

  
![Integration Published](./images/integration_published.png)

  
Before publishing an Integration for inclusion in the LAUNCH flow, consider tagging the integration appropriately so that it appears to your end users within the right context.

Step setup
----------

Various values entered in the step setup modal within the Integration Builder are presented to your end users during the LAUNCH flow.

  
![LAUNCH Step Setup](./images/step_setup.png)

 

Step element

Launch flow element

Usage

Step name

Field mapping screen title

The title could be used as a high level instruction to your end user.  
  
For example:  
  
“Select the spreadsheet you wish to export data to”

Step description

Field mapping screen description

The description should extend the title.  
  
For example:  
  
“Data will be exported to the spreadsheet you select below. The data will be appended to any existing data that spreadsheet contains.”

“Launch Visible” toggle

n/a

Controls whether or not that field is presented to your end user during the field mapping screen for this step.  
  
Where a value is selected, that will be presented to your end user as the default value or mapping. Your end user will be able to amend as required.  
  
Where no value is selected, your user will be responsible for specifying a value or mapping before they can proceed.  
  
Where “Launch Visible” is not selected, the value or mapping specified in the template will be used. Your end user will not be able to amend.

Cycle-level Parameters
----------------------

If the same request parameters is required in a number of steps within your template, Cycle-level Parameters can be used as a way to ensure your end user is only asked to specify the value once during the LAUNCH flow.

Make sure any Cycle-level parameters that your user should specify are marked as “_Launch Visible_” before publishing your template.

Template tagging
----------------

Within the context of the LAUNCH flow, template tags help display to your end users only integration templates that are relevant to intent of context within your app.

For example, tagging could be based on the type of application that is integrated to (e.g. CRM, email marketing, accounting, etc…), or a specific brand of application (e.g. Salesforce, Oracle, Facebook, etc…).

[Deploying LAUNCH in your App](./launch-deployment)