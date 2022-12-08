---
title: Performance tips
sidebar: cyclr_sidebar
permalink: performance-tips
tags: [cyclr-config]
menus:
    cyclr-configuration:
        title: Performance tips
        identifier: performance-tips
        weight: 6
---

The following tips may improve the performance of your integrations:

### Disabling Collection Splitting (if not needed)

If you don't have to Split (depends how you want the data to move within the Cycle) then disabling Collection Splitting improves the speed your data is processed.

### Avoiding Delay Steps

Avoid using Delay Steps unless you really wish to stop Transactions from progressing for perhaps an hour or so. Don't use them to try to add a small delay to each Transaction as a way to "space things out" as it'll just block them all as a group, then they'll all advance together as a group.

### Using Step Script instead of Inline Script

Using "Inline Script" on a Field Mapping is a lot slower than using Script in a Step's Advanced Settings area.

### Use Decision steps to avoid unnecessary Cycle runs

Using a decision step to check whether your _trigger_ step has returned data will prevent the rest of the cycle running unnecessarily, and could reduce your task usage.
