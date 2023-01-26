---
title: Jira information
sidebar: cyclr_sidebar
permalink: jira-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Map issue properties

To map an issue property field in a cycle, you need to add a custom field location:

1. [Map the Update Issue Property](#map-update-issue-property).
2. [Map the Get Issue Properties](#map-get-issue-properties).

<a link="map-update-issue-property">

### Map Update Issue Property

To add a custom request field location for the **Issues** > **Issue Properties** > **Update Issue Property** method:

1. Go to the **Edit Connector** page of your Jira connector.
2. Under the **Methods & Fields** heading, select **Issues > Properties > Update Issue Property**.
3. Under the **Request Fields** heading, select the pink **+** button to add a method field.
4. Enter the following:
   | Value              | Description                                                  |
   | ------------------ | ------------------------------------------------------------ |
   | **Field Location** | The property key of the issue property.                      |
   | **Display Name**   | The display name of the issue property in the Cyclr UI. Optional. |
   | **Description**    | The description of the issue property in the Cyclr UI. Optional. |
   | **Data Type**      | The data type of the issue property.                         |
5. Select **Create**.

<a link="map-get-issue-properties">

### Map Get Issue Properties

To add a custom response field location for the `Issues > Issue Properties > Get Issue Properties` method:

1. Go to the **Edit Connector** page of your Jira connector.
2. Under the **Methods & Fields** heading, select **Issues > Properties > Get Issue Properties**.
3. Under the **Response Fields** heading, select the pink **+** button to add a method field.
4. Enter the following:
   | Value              | Description                                                  |
   | ------------------ | ------------------------------------------------------------ |
   | **Field Location** | The property key of the issue property.                      |
   | **Display Name**   | The display name of the issue property in the Cyclr UI. Optional. |
   | **Description**    | The description of the issue property in the Cyclr UI. Optional. |
   | **Data Type**      | The data type of the issue property. This should match the data type used when creating the issue property. |
5. Select **Create**.

</section>
