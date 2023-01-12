---
title: Marketplace
sidebar: cyclr_sidebar
permalink: marketplace
tags: [marketplace]
layout: page
toc: false
introtitle: Marketplace
introtext: >-
    Embed an integration Marketplace into your application to deliver integrations to your users.
menus:
  embedding:
    title: Marketplace
    identifier: marketplace
    weight: 5
---
{% assign categorydata = site.data.categories.marketplace %}
{% include v2/category/{{page.categorylayout}}.html identifier="marketplace" intro=page.intro title=page.introtitle text=page.introtext %}
