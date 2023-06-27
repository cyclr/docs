---
title: Zap information
sidebar: cyclr_sidebar
permalink: zap-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">

## Enhanced objects

The Zap connector allow you to create enhanced objects for the **Submissions** category. This allows you to create multiple enhanced object categories that each look at the specified Campaign ID. If you want to automatically look up custom fields on the **Create Records** and **Create Submissions** methods, then you meed to create an enhanced object. 

### Set up an enhanced object

To set up an enhanced object:

1. Find the **Zap** connector in your **Template Connectors** page and select the **Edit Connector** pencil icon.
2. Under the **Methods and Fields** heading, expand the **Submissions (Enhanced Object)** category.
3. Select the red **Copy this Category to create a Custom Object Category** icon.
4. Select **Select object**. 
5. Select the required Campaign name from the drop down list.
6. Select **Copy**.

This creates a new custom object category with the specified campaign. You can run all methods from this category to call them against the campaign without having to specify it on each run. This means that you can look custom fields up automatically in the **Create Records** and **Create Submissions** methods.

</section>
