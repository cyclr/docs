---
title: ManageBac Authentication
sidebar: cyclr_sidebar
permalink: managebac-connector
tags: [connector]
---

## Partner Setup

First, login to your existing ManageBac account via your ManageBac front-end.

#### Retrieving an API Key

*   Go to **Settings** > **Develop** > **API Manager**.
*   Click **"Add New Token"** or **copy** an existing API token.
*   If you are going to **create** a new token:
    *   Set an appropriate name for the API token.
    *   Set the appropriate permissions for the token. Giving an API token all permissions is a security breach, so please choose carefully. Each category lets you set permissions for each action, so if you only wanted the API to be able to update students, you should only tick the **"update"** box under the **students** category.
    *   Click **"Add Token"**.
*   Copy the **API Token** supplied.

More information about the API and permissions can be found [here](https://managebac.zendesk.com/hc/en-us/articles/360018226931-Enabling-ManageBac-Public-API-for-Integrations).

### Cyclr Setup

Setup your ManageBac App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **ManageBac**
*   Click the **Setup** button

Enter the following values:

**API Key**:  The API token that we retrieved from the previous step.


Your ManageBac Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
