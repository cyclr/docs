---
title: indextitle
sidebar: cyclr_sidebar
permalink: indexpermalink
tags: [indextags]
layout: page
toc: false
categorylayout: indexcategorylayout
introtitle: indexintrotitle
introtext: >-
    indexintrotext
menus:
  indexmenuname:
    title: indexmenutitle
    identifier: indexmenuidentifier
    icon: indexmenuicon
    weight: indexmenuweight
---
{% assign categorydata = site.data.categories.indexpermalink %}
{% include v2/category/{{page.categorylayout}}.html identifier="indexmenuidentifier" intro=page.intro title=page.introtitle text=page.introtext %}
