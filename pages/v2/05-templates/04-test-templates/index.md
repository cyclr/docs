---
title: Test templates
sidebar: cyclr_sidebar
permalink: test-templates
tags: [test-templates]
layout: page
toc: false
singlecard: false
menus:
  templates:
    title: Test templates
    identifier: test-templates
    weight: 4
---
{% assign hubintro = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse dolor aliquam convallis leo." %}
{% assign hubtitle = "Test templates" %}
{% assign hubtext = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse dolor aliquam convallis leo." %}
{% include v2/category/{{page.categorylayout}}.html identifier="test-templates" intro=hubintro title=hubtitle text=hubtext %}