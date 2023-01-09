---
title: Marketplaces
sidebar: cyclr_sidebar
permalink: marketplace
tags: [marketplace]
layout: page
toc: false
intro: 
introtitle: Marketplace
introtext: >-
    Embed an integration Marketplace into your application to deliver integrations to your user
menus:
  embedding:
    title: Marketplaces
    identifier: marketplace
    weight: 5
---
{% assign categorydata = site.data.v2.categories.marketplace %}
{% include v2/category/{{page.categorylayout}}.html identifier="marketplace" intro=page.intro title=page.introtitle text=page.introtext %}
