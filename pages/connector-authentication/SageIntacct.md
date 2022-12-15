---
title: Sage Intacct Authentication
sidebar: cyclr_sidebar
permalink: sage-intacct-connector
tags: [connector]

---

## Sage Intacct setup
To authenticate this connector you will need a variety of credentials:

| Credential | Description |
| ----------- | ----------- |
| `Web Services ID` and `Web Services Password`  |  Web Services credentials consist of a sender ID and password. These are provisioned by Sage Intacct for customers/partners with an active Web Services developer license. These credentials are not necessarily tied to a particular Sage Intacct company/user. A Marketplace Partner can use a sender ID for any Sage Intacct company that has authorized that sender ID for Web Services.     |
|`Company Login ID` and `Company Login Password` | Provide a user ID and password to log in to a standalone company. This is the same information you use when you log into the Sage Intacct UI.   |
| `Company ID` | The ID of the company the above username and password will be used to authenticate against.       |
| `Location ID` (optional) | Add a location ID to log into a multi-entity shared company. Entities are typically different locations of a single company.  |

A `Client ID` can be used to log into a distributed child company. The `Company Login ID` and `Company Login Password` in this scenario are for access to the console, not the target client company itself. To provide this, fill in the Company ID field with the following format: `myConsoleId|clientCompanyId|entityId`.

## Cyclr setup

To set up the Sage Intacct connector in Cyclr:

1. Go to your **Cyclr Console**.

2. Select **Connectors** > **Application Connector Library** at the top of the page.

3. Use the search box to find the **Sage Intacct** connector.

4. Select the **Setup Required** icon.

5. Enter the your `Web Services ID`, `Web Services Password`, `Company Login ID`, `Company Login Password` and `Company ID`. 

6. Optionally, enter your `Location ID` if you are logging into a multi-entity shared company. 

7. Select **Save Changes**.
