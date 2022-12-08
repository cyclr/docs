---
title: Simitive ABC-HE Authentication
sidebar: cyclr_sidebar
permalink: simitive-abc-he-connector
tags: [connector]
---

# Simitive ABC-HE setup

You need the following information to setup the Simitive ABC-HE connector:

1. The API key of your Simitive ABC-HE account.

### Obtain an API key

From within your Simitive ABC-HE account, navigate to the **API Keys** page. Here you can create and view already existing API keys associated with your account. Select **Add API key** to create a new API key. Select **...** to the right of an existing API key and then **Reveal Token** to view an existing API key.

# Cyclr setup

### Account setup

You will be asked for the following values when installing the Simitive ABC-HE connector within an account:

| Value       | Description                                                                                                                                                                                   |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Domain**  | The domain of your Simitive ABC-HE login URL. For example, if you use `http://myuni.simitive.com/` to sign in to your Simitive ABC-HE account, then enter the domain as `myuni.simitive.com`. |
| **API Key** | The API key of your Simitive ABC-HE account.                                                                                                                                                  |

# Additional information

### Custom Object (Period Version)

Use custom objects to set the Simitive ABC-HE period version per group of methods. Multiple custom objects allow multiple period versions to be set per connector installation.

#### Set up a custom object

This will create a new method category. Inside this category, all methods will have the same period version. To set up a custom object:

1. Go to the Simitive ABC-HE connector Settings page:
    - For template connectors: **Cyclr Console** > **Templates** > **Template Connectors** > **Simitive ABC-HE** > **Edit Connector**.
    - For connectors within a cycle: **Cycle Builder** > **Application Connectors** > **Simitive ABC-HE** > **Settings**.
2. Under the **Methods and Fields** heading, expand the **Custom Object (Period Version)** category.
3. Select the red **Copy this Category to create a Custom Object Category** icon.
4. Enter the period version into **Specify object name**.
5. Select **Copy**.

#### Rename a custom object

To change the display name of a custom object method category:

1. Expand the method category by selecting the method category name.
2. Select the **Edit this Custom Object Category** icon.
3. Move the **Object Name** field to the **Object Value** field.
4. Change the **Object Name** field as required. This does not require a specific format.
5. Select **Save**.
