---
title: Doc title
sidebar: cyclr_sidebar
permalink: doc-permalink
tags: [doctags]
layout: page
toc: false
categorylayout: category_search
introtitle: Category title
introtext: >-
    Category intro text
menus:
  parentmenuid:
    title: Menu title
    identifier: menuid
    icon: menuicon
    weight: menuweight
---
{% assign categorydata = site.data.categories.doc-permalink %}
{% include v2/category/{{page.categorylayout}}.html identifier="doc-permalink" intro=page.intro title=page.introtitle text=page.introtext %}