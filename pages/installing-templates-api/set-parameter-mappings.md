---
title: Set Step Parameter
sidebar: cyclr_sidebar
permalink: set-step-parameters
tags: [installing]
---

_**Step Parameters are passed as a header or part of the URL (hostname, path, or query string parameters) to the third party API endpoint.**_

For each Missing parameter mapping returned by the step prerequisites request in step 7:

Request:

````http
    GET /v1.0/steps/{Step ID}/parameters/{Parameter ID}
    Authorization Bearer 0000000000000000000000000000000000000000000000000000000000000000
    X-Cyclr-Account: 00000000-0000-0000-0000-000000000000
````

Response:

````json
    {
        "Parameter": {
            "Id": 16017,
            "Name": "List ID",
            "Description": "Select a List.",
            "IsOptional": false,
            "DataType": "Undefined",
            "TriggerName": "Lookup List",
            "Values": [],
            "DisplayOrder": 1,
            "Triggers": [{
                "AccountConnectorId": 36329,
                "MethodId": 36666,
                "Name": "Lookup List",
                "HumanReadableKey": "[lists].name",
                "IdentifierKey": "[lists].id",
                "SubTriggers": [],
                "EntityId": 16017
            }]
        },
        "IsEntityIdentifier": false,
        "MappingType": null,
        "SourceFieldId": null,
        "SourceStepId": null,
        "TriggerValue": null,
        "TriggerValueDisplayName": null,
        "Value": null
    }
````

In the example above, the Triggers array provides directions as to the source of valid values.

In this example the method 36666 of Account Connector 36329 should be called, with the [lists].name values presented to the user for selection and the [lists].id value used as the actual parameter value.

Values can be retrieved from the trigger by calling the identified trigger method like below:

Request:

````http
    GET /v1.0/account/connectors/36329/methods/36666
    Authorization Bearer 2890edffcb964e8aab038cf4efc340ab62a4f604bd5a41369654086f5bd25519
    X-Cyclr-Account: 00000000-0000-0000-0000-000000000000
````

Response:

````json
    {
        "lists": [{
            "id": "a78f86e7d7",
            "web_id": 227621,
            "name": "Newsletter Subscribers",
            "contact": {
                "company": "Acme Inc",
                "address1": "1 Commercial Road",
                "address2": "",
                "city": "Eastbourne",
                "state": "East Sussex",
                "zip": "BN21 3XQ",
                "country": "GB",
                "phone": "+44 (0)330 354 2525"
            },
            "permission_reminder": "You are receiving this email as a subscriber to our regular newsletters. If you unsubscribe you will miss important news and announcements.",
            "use_archive_bar": true,
            "campaign_defaults": {
                "from_name": "Acme Inc",
                "from_email": "news@acmeinc.com",
                "subject": "",
                "language": "en"
            },
            "notify_on_subscribe": "hello@cyclr.com",
            "notify_on_unsubscribe": "hello@cyclr.com",
            "date_created": "2016-08-22T09:46:58+00:00",
            "list_rating": 0,
            "email_type_option": false,
            "subscribe_url_short": "http://eepurl.com/ABC123",
            "subscribe_url_long": "https://cyclr.us5.list-manage.com/subscribe?u=534685638659&id=84378947",
            "beamer_address": "us5-f578sd58f-cb2bd1adc8@inbound.mailchimp.com",
            "visibility": "pub",
            "modules": [],
            "stats": {
                "member_count": 723,
                "unsubscribe_count": 12,
                "cleaned_count": 0,
                "member_count_since_send": 2,
                "unsubscribe_count_since_send": 0,
                "cleaned_count_since_send": 0,
                "campaign_count": 2,
                "campaign_last_sent": "",
                "merge_field_count": 2,
                "avg_sub_rate": 0,
                "avg_unsub_rate": 0,
                "target_sub_rate": 0,
                "open_rate": 100,
                "click_rate": 100,
                "last_sub_date": "2016-08-22T11:36:09+00:00",
                "last_unsub_date": ""
            },
            "_links": []
        }]
    }
````

This response can then be used to present the user with valid options.

In this example there is a single value to present to the user, Newsletter Subscribers, with a corresponding value to pass to Cyclr as the parameter value, a78f86e7d7.

[How to Set Field Mapping](./listing-field-mappings)