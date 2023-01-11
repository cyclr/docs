---
title: ServSuite Authentication
sidebar: cyclr_sidebar
permalink: servsuite
tags: [connector]

---

## ServSuite ##

All that is needed to set up this connector are the username and password you normally use to access ServSuite.

### Important Note about Date Ranges ###

The ServSuite API may not be able to complete a call if the date range is too large, so the "List New" methods are set to only check the last 14 days.  If you need to go further back, you can use the "List by range" methods.
