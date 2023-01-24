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

