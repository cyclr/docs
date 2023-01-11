---
title: Application connectors
sidebar: cyclr_sidebar
permalink: connector-guides
tags: [connector-guides]
layout: page
toc: false
categorylayout: category_search
introtitle: Application connector guides
introtext: >-
    Search for specific application connectors in order to find their authentication guides and other additional information, or browse the available application connectors on the Cyclr website.
menus:
  mainmenu:
    title: Application connectors
    identifier: connector-authentication
    icon: navconnectors
    weight: 5
---
{% assign categorydata = site.data.v2.categories.connector-guides %}
{% include v2/category/{{page.categorylayout}}.html identifier="connector-authentication" intro=page.intro title=page.introtitle text=page.introtext %}
