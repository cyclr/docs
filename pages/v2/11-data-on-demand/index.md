---
title: Data on demand
sidebar: cyclr_sidebar
permalink: data-on-demand
tags: [data-on-demand]
layout: page
toc: false
introtitle: Data on demand
introtext: >-
    Use Cyclr as a proxy server to interact with external applications, call connector methods, and process data.
menus:
  mainmenu:
    title: Data on demand
    identifier: data-on-demand
    icon: report
    weight: 11
---
{% assign categorydata = site.data.v2.categories.data-on-demand %}
{% include v2/category/{{page.categorylayout}}.html identifier="data-on-demand" intro=page.intro title=page.introtitle text=page.introtext %}
