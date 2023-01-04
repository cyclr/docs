---
title: Install cycle from template
sidebar: cyclr_sidebar
permalink: install-cycle
tags: [install-cycle]
layout: page
toc: false
menus:
  cycle-account-api:
    title: Install cycle from template
    identifier: api-install-cycle
    weight: 3
---
{% assign hubintro = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse dolor aliquam convallis leo." %}
{% assign hubtitle = "Install cycle from template" %}
{% assign hubtext = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse dolor aliquam convallis leo." %}
{% assign categorydata = site.data.v2.categories.install-cycle %}
{% include v2/category/{{page.categorylayout}}.html identifier="api-install-cycle" intro=hubintro title=hubtitle text=hubtext %}
