---
title: Document360 Connector Guide
sidebar: cyclr_sidebar
permalink: document360-connector
tags: [connector]
---

## Authentication

The following are the steps needed to authorize this connector to access Document360 projects:

### Document360 Console

1. Go to [Document360](https://document360.io/) to either login or create a new account if you don't already have one. You will be directed to the portal dashboard where your projects are displayed.

2. Select a pre-existing project if applicable or create a new one by clicking 'New project' in the top right corner of the page.

    ![connector setup](./images/doc_360_setup_1.png)
    ![connector setup](./images/doc_360_setup_2.png)

3. The API Key can now be accessed. Click the Settings 'cog' icon on the bottom left and then 'API Tokens' from the left hand menu. If a token doesn't already exist, generate one by entering a name and selecting all four 'Allowed Methods': GET, POST, PUT and DELETE.

    ![connector setup](./images/doc_360_setup_8.png)
    ![connector setup](./images/doc_360_setup_4.png)
    ![connector setup](./images/doc_360_setup_5.png)

### Cyclr Console

1. Go to 'My Connectors' from the top right drop down menu.

    ![connector setup](./images/doc_360_setup_9.png)
2. From your connector list 'Edit connector' for Document360

    ![connector setup](./images/doc_360_setup_10.png)
3. From the Edit Connector page click 'Setup'. Enter the API Key and click 'Next'.

    ![connector setup](./images/doc_360_setup_6.png)
    ![connector setup](./images/doc_360_setup_7.png)

The connector is now authenticated and ready to use.
