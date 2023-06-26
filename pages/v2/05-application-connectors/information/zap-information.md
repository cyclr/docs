---
title: Zap information
sidebar: cyclr_sidebar
permalink: zap-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">

### Enhanced Objects

The Zap connector allows for enhanced objects to be created for the **Submissions** category. This will allow you to create multiple enhanced object categories that each look at the specified Campaign ID. This is a required step if you would like to automatically look up custom fields on the **Create Records** and **Create Submissions** methods.

## Set up an enhanced object

To set up an enhanced object:

1. Go to the **Zap** connector **Settings** page.
2. Under the **Methods and Fields** heading, expand the **Submissions (Enhanced Object)** category.
3. Select the red **Copy this Category to create a Custom Object Category** icon.
4. Select **Select object**. 
5. Select the required Campaign name from the drop down list.
6. Select **Copy**.

A new custom object category will have been created with the specified campaign. All  methods can be run from in here to call them against the campaign without having to specify it on each run. This will now allow custom fields to be looked up automatically in the **Create Records** and **Create Submissions** methods.

</section>
