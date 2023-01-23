---
title: Jira Authentication
sidebar: cyclr_sidebar
permalink: jira-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
  
## Jira setup

<a link="get-authentication-details">
  
### Get authentication details

To authenticate your connector, you need to get the authentication details. 

To create an API token for your Jira account, go to the [Manage API tokens for your Atlassian account](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) page of the Atlassian documentation and follow the instructions under the **Create an API token** heading. Use the API token in place of your Jira account password when you setup your Jira account in Cyclr.

</section>

<section class="card">

## Cyclr setup

### Account setup

Cyclr asks you for the below values when you install the Jira connector into an account:

| Value                          | Description                                                  |
| :----------------------------- | :----------------------------------------------------------- |
| **JIRA URL**                   | The URL of your Jira instance. For Atlassian hosted instances, enter `https://mycompany.atlassian.net`. For on-premises hosted instances enter the full URL. For example, `https://my.jira-installation.com`. |
| **On-Premises Installation? ** | If your Jira instance is an on-premises hosted instance. Set to `false` for Atlassian hosted instance or `true` for on-premises hosted instances. Optional and defaults to `false`. |
| **Username**                   | The username of your Jira account.                           |
| **Password**                   | The [API token](#get-authentication-details) of your Jira account. |

> **Note**: You can use different details for different accounts.

</section>

<section class="card">

## Additional information

### Map Issue Properties

You need to add a custom field location to map an issue property field in a cycle. Do this in the following order:

1. [Map Update Issue Property](#map-update-issue-property).
2. [Map Get Issue Properties](#map-get-issue-properties).

<a link="map-update-issue-property">

#### Map Update Issue Property

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

#### Map Get Issue Properties

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
