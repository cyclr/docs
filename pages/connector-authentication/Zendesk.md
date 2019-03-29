---
title: Zendesk Authentication
sidebar: cyclr_sidebar
permalink: Zendesk-connector
tags: [connector]
---

# Zendesk #



Webhook Implementation - Closed Tickets
---------------------------------------

  - set Trigger conditions to 'Status' is 'Closed' and/or 'Solved' 
  - in 'Actions' set 'Notify Target' to required Target 
  - fields below to be added to Trigger in 'JSON Body'  

```json

{ 
  "TicketId":"{{ticket.id}}", 
  "ExternalId":"{{ticket.external_id}}", 
  "Title":"{{ticket.title}}", 
  "Description":"{{ticket.description}}", 
  "TicketVia":"{{ticket.via}}", 
  "Status":"{{ticket.status}}", 
  "Priority":"{{ticket.priority}}", 
  "Type":"{{ticket.ticket_type}}" 
}
```


For further information please check the official documentation below:

https://support.zendesk.com/hc/en-us/articles/204890268
