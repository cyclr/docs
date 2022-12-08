---
title: Twilio Voice
sidebar: cyclr_sidebar
permalink: twiliovoice
tags: [connector]
---

# Twilio Voice #

## Partner Setup ##

This document will explain what is needed to setup access to Twilio Voice and install the connector.

### Credentials Setup ###

1. Go to your Twilio [project settings](https://www.twilio.com/console/project/settings) and retrieve the API credentials (Account SID, Auth Token).

### Connector Setup ###

In the connector setup enter the "Account SID" as the username, and the "Auth Token" as the password.

### Webhook Setup ###

1. Select a phone number from the [incoming phone numbers list](https://www.twilio.com/console/phone-numbers/incoming).
2. Set the "Call Status Changes" to the Cyclr webhook URL.

Cyclr will now recieve any incoming or outgoing calls made to or from this Twilio phone number through the webhook.
