---
title: Briostack Connector
sidebar: cyclr_sidebar
permalink: briostack-connector
tags: [connector]
---

Briostack Setup
---------------
In order to authenticate the connector, you will simply need your username, password and account name.

Your account name can be found in the address of your website, for example if your site is __johnsmithltd.briostack.com__, your account name would be __johnsmithltd__.


Important Note
---------------
The Briostack API requires a separate account for each installation of the connector.  If you try to run two connectors authenticated with the same details, you may receive the following error -

``"Congratulations! It looks like your team is growing and you need more Brio Sales licenses. Reach out to Briostack at 801-623-5200 or support@briostack.com to add more."``

Sales Methods
---------------
Within the Sales methods, you can select a category, to return only those sales which fall within it, or return all sales by leaving the field blank.

Customers
---------------
It is not currently possible to filter the customers by business sector, so for most use cases, "List Customers" would not be a practical method.  As a result, Get Customer has been provided for returning individual customer records.
