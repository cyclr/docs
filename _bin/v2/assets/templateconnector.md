---
title: connectortitle
sidebar: cyclr_sidebar
permalink: connectorname-connector
tags: [connector]
icon: connectoricon
default_header: false
category: connectorcategory
categories: connectorcategories
showv1content: connectorcontentv1
---
{% assign connectordata = site.data.v2.connectors.connector-connectorname %}
{% assign v1content = "connectorname.md" %}
{% include v2/connector/connector.html %}	