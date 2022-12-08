---
title: Optimizely Authentication
sidebar: cyclr_sidebar
permalink: optimizely-connector
tags: [connector]
---

## Partner Setup

#### Retrieving OAuth2 Details

*   [Login](https://app.optimizely.com/signin) to an Optimizely developer account, or [sign up for an account.](https://www.optimizely.com/rollouts/)
*   Click **Account Settings** in the bottom left area of the navigation tree.
*   Navigate to the **Registered Apps** tab.
*   Click **Register New Application**.
*   Enter an appropriate name for the application, enter your redirect URL (https://**Your Service Domain**/connector/callback), set the Client Type as Confidential and click **Apply**.
*   Copy the generated **Client ID** and **Client Secret** values.

### Cyclr Setup

Setup your Optimizely App within Cyclr:

*   Go to **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Optimizely**
*   Click the **Setup** button

Enter the following values:

**Client ID**:  The **Client ID** that we retrieved from the previous step.
**Client Secret**: The **Client Secret** that we retrieved from the previous step.

Your Optimizely Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
