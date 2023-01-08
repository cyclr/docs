---
title: indextitle
sidebar: cyclr_sidebar
permalink: indexpermalink
tags: [indextags]
layout: page
toc: false
categorylayout: indexcategorylayout
intro: indexintro
introtitle: indexintrotitle
introtext: >-
    indexintrotext
menus:
  indexmenuname:
    title: indexmenutitle
    identifier: indexmenuidentifier
    icon: indexmenuicon
    toggleonly: indexmenutoggleonly
    weight: indexmenuweight
---
{% assign categorydata = site.data.v2.categories.indexpermalink %}
{% include v2/category/{{page.categorylayout}}.html identifier="indexmenuidentifier" intro=page.intro title=page.introtitle text=page.introtext %}
