---
title: About Cyclr
sidebar: cyclr_sidebar
permalink: about-cyclr
tags: [about-cyclr]
layout: page
toc: false
introtitle: About Cyclr
introtext: >-
    Find all the information and resources that you need in order to use Cyclr.
menus:
  mainmenu:
    title: About Cyclr
    identifier: about-cyclr
    icon: navdocs
    weight: 1
---
{% assign categorydata = site.data.categories.about-cyclr %}
{% include v2/category/{{page.categorylayout}}.html identifier="about-cyclr" intro=page.intro title=page.introtitle text=page.introtext %}
