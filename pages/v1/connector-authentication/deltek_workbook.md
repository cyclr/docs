---
title: Deltek Workbook Connector Guide
sidebar: cyclr_sidebar
permalink: deltek-workbook-connector
tags: [connector]
---


Permissions In Deltek Workbook
---------------
Get API Access

You must grant the required access rights to your API user's access role for the specific API endpoint you need in Settings » Advanced tools » User access rights of your WorkBook application.

Prerequisite - WorkBook user that can grant access rights to an API user's access role.

**Procedure**

To get access to an API endpoint:

From your WorkBook application, go to Settings » Advanced tools » User access rights.
 * Click the Access role requests tab.
 * On the Access roles pane, select the access role for your API user.
 * On the right pane, search for the request name of the API endpoint you need.
 * Select the Access check box for the required HTTP verb.

Connector Setup
---------------

The Connector now can be installed using the credentials (Username/Password) for the user obtained in the above steps:

Domain - This is the domain used to access your portal. e.g. "mycompany.workbook.net"
