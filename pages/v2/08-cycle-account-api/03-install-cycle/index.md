---
title: Install cycle from template
sidebar: cyclr_sidebar
permalink: install-cycle
tags: [install-cycle]
layout: page
toc: false
intro: indexintro
introtitle: Install cycle from template
introtext: >-
    Get a list of available cycle templates and install a cycle into an account
menus:
  cycle-account-api:
    title: Install cycle from template
    identifier: api-install-cycle
    weight: 3
---
{% assign categorydata = site.data.v2.categories.install-cycle %}
{% include v2/category/{{page.categorylayout}}.html identifier="api-install-cycle" intro=page.intro title=page.introtitle text=page.introtext %}
