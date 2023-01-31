---
title: Category page title
sidebar: cyclr_sidebar
permalink: category-page-slug
tags: [category-tag]
layout: page
toc: false
introtitle: Page title
introtext: >-
    Page intro text.
menus:
  parentmenuid:
    title: Menu title
    identifier: menuid
    icon: categoryicon
    weight: 1
---
{% assign categorydata = site.data.categories.category-page-slug %}
{% include v2/category/{{page.categorylayout}}.html identifier="category-page-slug" intro=page.intro title=page.introtitle text=page.introtext %}
