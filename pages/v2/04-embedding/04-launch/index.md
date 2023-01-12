---
title: LAUNCH
sidebar: cyclr_sidebar
permalink: launch
tags: [launch]
layout: page
toc: false
introtitle: LAUNCH
introtext: >-
    Embed LAUNCH into your application to deliver integrations to your users.
menus:
  embedding:
    title: LAUNCH
    identifier: launch
    weight: 4
---
{% assign categorydata = site.data.categories.launch %}
{% include v2/category/{{page.categorylayout}}.html identifier="launch" intro=page.intro title=page.introtitle text=page.introtext %}
