---
title: Connector information
sidebar: cyclr_sidebar
permalink: additional-information
tags: [connector-guides]
layout: page
toc: false
categorylayout: category_search
searchtext: connector_information_search
introtitle: Additional information
introtext: >-
    Search for a specific application connector to find any information we have on how you can use the connector. For information on how to set up and authenticate the connector, see [Application connector authentication](connector-guides).
menus:
  connector-authentication:
    title: Additional information
    identifier: additional-information
    weight: 2
---
{% assign categorydata = site.data.categories.connector-guides %}
{% include v2/category/{{page.categorylayout}}.html identifier="connector-authentication" intro=page.intro title=page.introtitle text=page.introtext %}