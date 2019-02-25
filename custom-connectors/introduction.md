---
title: Custom Connector Introduction
---

What is a custom connector?
---------------------------

A custom connector allows you to integrate apps that aren’t in our [connector library](http://cyclr.com/connectors/). You can even add connectors for your own private apps and websites. Our Connector Manager makes this task quicker and easier to maintain than writing a traditional coded integration.

A connector is a JSON-formatted text file which maps to the methods and fields of an API. Once uploaded, Cyclr takes care of much of the ‘grunge’ of working with APIs:

*   Authentication
*   Paging
*   Rate limiting / throttling
*   Error handling

Your connector file is uploaded to your account (top-right account menu > Developer Tools) as a private Custom Connector.

Below is a basic example that illustrates a method and a single field. You can find more detailed examples [here](./examples).

{% raw %}
        "Methods": [
            {
                "Name": "Your Method Name",
                "Description": "A longer description.",
                "Category": "Contacts",
                "MethodType": "Action",
                "HttpMethod": "Get",
                "DataType": "Json",
                "Endpoint": "https://api.yoururl.com",
                "ResponseFormat": {
                    "Fields": [
                        {
                            "ConnectorField": "[records].Salutation",
                            "SystemField": "Salutation",
                            "DisplayField": "Salutation"
                        },
                  ]
    
             }
          
             ... etc
{% endraw %}

Can you add a new connector for…?
---------------------------------

Firstly, please ask us! We are adding new connectors all the time; we plan to have hundreds.

#### Connector selection criteria

*   Sufficient interest from customers or prospects
*   A customer or prospect is prepared to share the cost of the connector’s development
*   The opportunity for a mutually beneficial marketing partnership with the app we are connecting to

[Create Custom Connector Methods](./methods)