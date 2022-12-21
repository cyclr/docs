---
title: indextitle
sidebar: cyclr_sidebar
permalink: indexpermalink
tags: [indextags]
layout: page
toc: false
singlecard: false
categorylayout: [categorylayout]
introtitle: [introtitle]
introtext: [introtext]
menus:
  indexmenuname:
    title: indexmenutitle
    identifier: indexmenuidentifier
    icon: indexmenuicon
    toggleonly: indexmenutoggleonly
    weight: indexmenuweight
---
{% assign hubintro = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse dolor aliquam convallis leo." %}
{% assign hubtitle = "indextitle" %}
{% assign hubtext = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse dolor aliquam convallis leo." %}
{% assign categorydata = site.data.v2.category.{{page.permalink}} %}
{% include v2/category/{{page.categorylayout}}.html identifier="indexmenuidentifier" intro=hubintro title=hubtitle text=hubtext %}
