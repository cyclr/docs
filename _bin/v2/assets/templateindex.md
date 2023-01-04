---
title: indextitle
sidebar: cyclr_sidebar
permalink: indexpermalink
tags: [indextags]
layout: page
toc: false
categorylayout: indexcategorylayout
introtitle: indexintrotitle
introtext: indexintrotext
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
{% assign categorydata = site.data.v2.categories.indexpermalink %}
{% include v2/category/{{page.categorylayout}}.html identifier="indexmenuidentifier" intro=hubintro title=hubtitle text=hubtext %}
