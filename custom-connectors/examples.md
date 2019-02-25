---
title: Custom Connector Examples
---

Example 1: standard connector
-----------------------------

The below JSON is taken from a MailChimp connector.

{% raw %}
    {
      "Name": "MailChimp",
      "Description": "This connector provides basic functionalities for connecting to MailChimp.",
      "Version": "v3",
      "AuthType": "OAuth2",
      "OAuth2Type": "AuthorisationCode",
      "Methods": [
        {
          "Parameters": [
            {
              "Values": [
                
              ],
              "Description": "Restrict response to lists created before the set date.",
              "IsOptional": true,
              "TargetType": "QueryString",
              "TargetName": "before_date_created",
              "DisplayName": "Before Date Created"
            },
            {
              "Values": [
                
              ],
              "Description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.",
              "IsOptional": true,
              "TargetType": "QueryString",
              "TargetName": "[fields]",
              "DisplayName": "Fields"
            }
          ],
          "ResponseFormat": {
            "Fields": [
              {
                "Values": [
                  
                ],
                "ConnectorField": "[lists].id",
                "SystemField": "ListId",
                "DisplayField": "List ID"
              },
              {
                "Values": [
                  
                ],
                "ConnectorField": "[lists].name",
                "SystemField": "ListName",
                "DisplayField": "List Name"
              }
            ]
          },
          "Category": "Lists",
          "MethodType": "Action",
          "HttpMethod": "Get",
          "DataType": "Json",
          "EndPoint": "https://{{Dc}}.api.mailchimp.com/3.0/lists",
          "Name": "Get Lists",
          "Description": "Get all lists in the account."
        },
        {
          "Parameters": [
            
          ],
          "RequestFormat": {
            "Fields": [
              {
                "Values": [
                  
                ],
                "ConnectorField": "name",
                "SystemField": "ListName",
                "DisplayField": "List Name",
                "DisplayOrder": 1
              },
              {
                "Values": [
                  
                ],
                "ConnectorField": "contact.company",
                "SystemField": "Company",
                "DisplayField": "Contact Company",
                "DisplayOrder": 2
              },
              {
                "Values": [
                  {
                    "Value": "pub"
                  },
                  {
                    "Value": "prv"
                  }
                ],
                "ConnectorField": "visibility",
                "SystemField": "Visibility",
                "DisplayField": "Visbility",
                "Description": "Whether this list is public (pub) or private (prv).",
                "DisplayOrder": 3
              }
            ]
          },
          "ResponseFormat": {
            "Fields": [
              {
                "Values": [
                  
                ],
                "ConnectorField": "id",
                "SystemField": "listId",
                "DisplayField": "List Id",
                "DisplayOrder": 1
              }
            ]
          },
          "Category": "Lists",
          "MethodType": "Action",
          "HttpMethod": "Post",
          "DataType": "Json",
          "EndPoint": "https://{{Dc}}.api.mailchimp.com/3.0/lists",
          "Name": "Create List",
          "Description": "Create a new list in your MailChimp account."
        }
      ],
      "Parameters": [
        {
          "Values": [
            
          ],
          "TargetType": "MergeField",
          "TargetName": "Dc",
          "DisplayName": "Data Center",
          "IsAccountConnectorProperty": true
        }
      ]
    }
{% endraw %}

Example 2: connector with custom scripting
------------------------------------------

The other example is taken from the ZohoCRM connector. You can see how parameters and scripting are used.

{% raw %}
    {
      "Methods": [
        {
          "Parameters": [
            {
              "Values": [],
              "Hide": true,
              "TargetType": "MergeField",
              "TargetName": "Xml",
              "DisplayName": "xml data"
            },
            {
              "Values": [],
              "Hide": true,
              "TargetType": "MergeField",
              "TargetName": "ApiKey",
              "DisplayName": "ApiKey"
            }
          ],
          "RequestFormat": {
            "Fields": [
              {
                "Values": [],
                "ConnectorField": "Account Name",
                "SystemField": "AccountName",
                "DisplayField": "Account Name",
                "Description": "The company name."
              },
              {
                "Values": [],
                "ConnectorField": "Account Owner",
                "SystemField": "AccountOwner",
                "DisplayField": "Account Owner",
                "IsOptional": true,
                "Description": "The name of the user to whom the account is assigned."
              },
              {
                "Values": [],
                "ConnectorField": "Website",
                "SystemField": "Website",
                "DisplayField": "Website",
                "IsOptional": true,
                "Description": "The URL of the company's website."
              }
            ]
          },
          "Status": "Approved",
          "Category": "Accounts",
          "MethodType": "Action",
          "HttpMethod": "Post",
          "DataType": "Xml",
          "EndPoint": "https://crm.zoho.com/crm/private/xml/Accounts/insertRecords?authtoken={{ApiKey}}&scope=crmapi&xmlData={{Xml}}",
          "Script": "function before_action(){\r\n\tvar xmlData = '<Accounts><row no=\"\"1\"\">';\r\n\r\n\tfor (var p in method_request) {\r\n\t\txmlData += '<FL val=\"\"' + p + '\"\">' + method_request[p] + '</FL>';\r\n\t}\r\n\r\n\txmlData += '</row></Accounts>';\r\n\tmethod_request_parameters.xmlData = xmlData;\r\n\treturn true;\r\n}\r\n",
          "Name": "Create Account",
          "Description": "Create a new account inside Zoho CRM."
        }
      ],
      "Status": "Approved",
      "Version": "1",
      "AuthType": "ApiKey",
      "Name": "Zoho CRM",
      "Description": "Connector for Zoho CRM."
    }
{% endraw %}

[Learn About Custom Connector Fields](./fields)