---
title: Tools
sidebar: cyclr_sidebar
permalink: tools
tags: [templates]
layout: page
toc: false
introtitle: Tools
introtext: >-
    Use Cyclr's logic tools in your integration templates to further control how you process data.
menus:
  build-a-template:
    title: Tools
    identifier: tools
    weight: 4
---
{% assign categorydata = site.data.categories.build-a-template %}
{% include v2/category/{{page.categorylayout}}.html identifier="tools" intro=page.intro title=page.introtitle text=page.introtext %}
