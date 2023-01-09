---
title: Test templates
sidebar: cyclr_sidebar
permalink: test-templates
tags: [test-templates]
layout: page
toc: false
introtitle: Test Templates
introtext: >-
    Learn how to manage your integration templates to make sure they are up to date and performing well.
menus:
  cycle-templates:
    title: Test templates
    identifier: test-templates
    weight: 4
---
{% assign categorydata = site.data.v2.categories.test-templates %}
{% include v2/category/{{page.categorylayout}}.html identifier="test-templates" intro=page.intro title=page.introtitle text=page.introtext %}
