---
title: Cross Updating Preventor
sidebar: cyclr_sidebar
permalink: cross-updating-preventor
tags: [utility-connector]
---

## Purpose

Many integrations are triggered when details of an updated record in one applicaiton is sent to a second application so as to keep the data in synch. There are occacions when this process needs to be bi-directional and this can result in an infinite cross-updating loop where A updates B then B updates A and so on.

The Cyclr Cross Updating Preventor is designed to stop this.  It can be used to make sure that an inbournd update to an application does not result in a return outbound update.
