---
title: Marketplaces
sidebar: cyclr_sidebar
permalink: marketplace
tags: [marketplace]
layout: page
toc: false
menus:
  embedding:
    title: Marketplaces
    identifier: marketplace
    weight: 5
---
{% assign hubintro = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse dolor aliquam convallis leo." %}
{% assign hubtitle = "Marketplaces" %}
{% assign hubtext = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse dolor aliquam convallis leo." %}
{% assign categorydata = site.data.v2.categories.marketplace %}
{% include v2/category/{{page.categorylayout}}.html identifier="marketplace" intro=hubintro title=hubtitle text=hubtext %}
