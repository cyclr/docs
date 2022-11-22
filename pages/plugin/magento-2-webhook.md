---
title: Magento 2 Webhook Extension
sidebar: cyclr_sidebar
permalink: magento-2-webhook-extension
tags: [plugins]
---

Magento 2 does not include webhook functionality.

We have created our Magento 2 extension to allow for easy integration with any of the [apps or services that Cyclr connects](https://cyclr.com/connectors).

#### Prerequisites

*   Magento with admin access

*   Cyclr account

#### Extension installation

If you have completed the prerequisites:

*   [Download our Magento 2 Webhook extension](https://github.com/cyclr/cyclr-magento-2/releases)

*   Copy the extension to your Magento instance, e.g.
```
cp -r ./ /var/www/html/app/code/Cyclr/Webhook/
```

*   Update database schema
```
php bin/magento setup:upgrade
```

*   Clean cache (Optional)
```
php bin/magento cache:clean
```

Once those steps are complete, you are ready to install the Magento 2 Webhook connector in Cyclr. The Magento 2 Webhook connector will automatically create / delete webhooks in your Magento instance when you start / stop a cycle.

#### Extension setup

*   The webhooks will be processed once per minute. If you wish to change this setting, you can visit *System -> System Settings -> Cron (Scheduled Tasks) -> webhooks*
