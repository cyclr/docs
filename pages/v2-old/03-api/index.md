---
title: API
sidebar: cyclr_sidebar
permalink: api
tags: [api]
layout: page
toc: false
intro: 
introtitle: API
introtext: >-
    Find information on how to work with the Cyclr API.
menus:
  mainmenu:
    title: API
    identifier: api
    icon: openapi
    weight: 3
---
{% assign categorydata = site.data.v2.categories.api %}
{% include v2/category/{{page.categorylayout}}.html identifier="api" intro=page.intro title=page.introtitle text=page.introtext %}
