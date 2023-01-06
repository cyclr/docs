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
{% assign categoryintro = "indexintrotext" %}
{% assign categorytitle = "indexintrotitle" %}
{% assign categorytext = "indexintrotext" %}
{% assign categorydata = site.data.v2.categories.indexpermalink %}
{% include v2/category/{{page.categorylayout}}.html identifier="indexmenuidentifier" intro=categoryintro title=categorytitle text=categorytext %}
