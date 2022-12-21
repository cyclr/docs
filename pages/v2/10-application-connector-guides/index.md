---
title: Application connector guides
sidebar: cyclr_sidebar
permalink: connector-guides
tags: [connector-guides]
layout: page
toc: false
singlecard: false
categorylayout: category_search
introtitle: Connector Documentation
introtext: Find all the resources you need to get the most from your connectors
menus:
  mainmenu:
    title: Application connector guides
    identifier: application-connectors
    icon: navsettings
    weight: 10
---
{% assign categorydata = site.data.v2.categories.connector-guides %}
{% assign hubintro = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse dolor aliquam convallis leo." %}
{% assign hubtitle = "Application connector guides" %}
{% assign hubtext = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse dolor aliquam convallis leo." %}
{% include v2/category/{{page.categorylayout}}.html identifier="application-connectors" intro=hubintro title=hubtitle text=hubtext %}
