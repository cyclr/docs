---
title: Wordpress.com Authentication
sidebar: cyclr_sidebar
permalink: wordpresscom-connector
tags: [connector]
---

# Wordpress.com #

Wordpress.com Connector Setup
-------------

## ⚠️ Read me ⚠️ ##
Make sure this is the right Wordpress connector you are after. Wordpress.com uses authentication that doesnt require the use of 3rd party plugins and is primarily used for Wordpress hosted sites rather than self-hosted.
For self-hosted sites view the Wordpress guide [here](https://docs.cyclr.com/wordpress-connector.html#wordpress-connector-setup).

## Authentication ##
To set up authentication you will need to make an application within the applications manager located [here](https://developer.wordpress.com/apps/). 
When filling in the fields make sure to put your Cyclr callback URL into the 'Redirect URLs' field.
- Your Cyclr callback URL can be found in your Cyclr console under Settings > General Settings > Service Domain.

Once created you will have access to your Client ID and Secret.

## Cyclr Setup

Setup your Wordpress.com connector within Cyclr:

- Go to your **Cyclr Console**
- Click the **Connectors** menu along the top
- Choose Connector Library
- Select the  **Wordpress.com** Connector
- Click the **Setup** button

### Connector Setup ###
---------------

The Connector now can be installed using the credentials obtained in the above step:

**Client ID**: _Wordpress.com Client ID_

**Secret**: _Wordpress.com Client Secret_

**Domain**:  _Your Wordpress Domain_ 

Your Wordpress.com Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
