---
title: Set up a Marketplace
sidebar: cyclr_sidebar
permalink: marketplace-setup
tags: [marketplaces,embedding]
menus:
    marketplace:
        title: Set up a Marketplace
        identifier: marketplace-setup
        toggleonly: menutoggleonly
        weight: 2
---
{::options parse_block_html="true" /}
<section class="card">

## Create a Marketplace

To create a Marketplace, go to your Cyclr console:

1. Go to **Embedding** > **Marketplace**.
2. Select the **Create Marketplace** button.
3. Enter a name for your Marketplace, and you have the option to enter a description.
4. Select **Add**.

To add integrations and action links to your Marketplace, select the **Edit** button for that Marketplace. Once you add these elements, they display within the **Edit Marketplace** page, and you can use the black arrow icons to change the order that they appear in. 

</section>
<section class="card">

## Add a category

You can create categories to differentiate between elements of your Marketplace:

1. Select the **Add Category** button.
2. Enter a name for the category. You also have the option to enter a description.
3. Select the **Upload** button to upload an icon to display with the category, or select **Or pick an Icon from our library** to choose from Cyclr’s available icons.
4. Select **Add** to create and open the category.

</section>
<section class="card">

## Add an integration package

You can use an integration package to to select one or more cycle templates. IF multiple templates are needed, your user can save time and install all of the templates together.

1. Select the **Add Integration Package** button.
2. Enter a name for the category. You also have the option to enter a description.
3. Select the **Upload** button to upload an icon to display with the category, or select **Or pick an Icon from our library** to choose from Cyclr’s available icons.
4. Select **Add** to set up your integration package.
5. From the **Integration Package** page, select the template you want to add from the dropdown, and select the **Add Template** button.
6. Repeat step 5 until you’ve added all the templates you want to include in the package.

### Integration package settings

To view and change the settings of your integration package, switch to the **Package Details** tab. From this tab, you can edit the name, description, and the icon, and set a custom **Installed Message** that displays when the package successfully installs.

There are three toggle settings for integration packages that you can use.

| **Setting** | **Description** |
|:---|:---|
| **Single Installation** | This toggle means your user can only install the integration package once. For integration packages with multiple templates, if the user has at least one of the included templates installed, they can’t install the package. |
| **Redirect Back to Marketplace on Install Complete** | This toggle means that your user is redirected back to your Marketplace when they complete the install. |
| **Auto Start on Install Complete** | This toggle means that the integration package starts to run automatically when the package successfully installs. |

> **Note**: If you don’t enable **Redirect Back to Marketplace**, then the LAUNCH Complete HTML displays when the package successfully installs. You can customize the LAUNCH Complete HTML with the `{{InstallCompleteMessage}}` mergefield.


</section>
<section class="card">

## Add an action link

You can add custom links to your Marketplace that direct your user to a specific URL. 

1. Select the **Add Action Link** button.
2. Enter a name for the category. You also have the option to enter a description.
3. Enter the text that you want to display to your user in the **Link Text** field.
4. Enter the URL to direct your user to in the **Link URL** field.
5. Select the **Upload** button to upload an icon to display with the category, or select **Or pick an Icon from our library** to choose from Cyclr’s available icons.
6. Select **Add** to create and open the action link.

</section>



