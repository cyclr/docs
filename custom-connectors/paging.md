---
title: Custom Connectors Paging
---

Inbound and Outbound Paging
---------------------------

So that Cyclr can retrieve more objects than a remote API may allow in one request (some restrict this to 100 objects, for example), it can take advantage of an API’s paging functionality. This is referred to as **Inbound Paging**. Cyclr will repeatedly request pages of objects until it has retrieved them all.

When a remote API has a limit on the amount of data that can be sent in a single request, Cyclr will also be able to split large amounts of data that need to be sent into several small requests. This is referred to as **Outbound Paging**.

To set a Connector as using Paging, you can use the following Connector-level properties (they default to false – no paging – if not supplied):

    "PagedInbound": true,
    "PagedOutbound": true,

At the Connector level, **PageSizeInbound **and **PageSizeOutbound **are numeric properties can be defined to set the size of the inbound and outbound pages. e.g.

    "PageSizeInbound": 100, 
    "PageSizeOutbound": 20,

For inbound paging, **Parameters **can then be created to describe how Cyclr should work with the remote API to perform paging. You can use** Inbound Paging Variables **listed below as **Values **for paging **Parameters**.

Note that paging parameters will be shown to users unless the “Hide” property is set to be true for them, i.e.

    "Hide": true

#### Inbound Paging Variables

The following Cyclr variables are available as part of Inbound Paging:

#### CYCLR_PAGE_NUMBER

Cyclr will use the current page number it’s requesting here as it iterates through them. Use this with APIs that use page numbers and “number of objects to retrieve” values.

In this example from Magento, it would be “page”:

    You can define the limit of items returned in the response by passing the limit parameter. By default, 10 items are returned and the maximum number is 100 items. You can also define the page number by passing the page parameter. Example:
    http://magentohost/api/rest/products?page=2&limit=20

#### CYCLR_PAGE_OFFSET

Essentially a “row offset”, starting at 0. Use this with APIs that use offsets and “number of objects to retrieve” values .

In the below example from MailChimp it would be “offset”:

    Paginate your API requests to limit response results and make them easier to work with. We use offset and count in the URL query string to paginate because it provides greater control over how you view your data.
    
    Offset defaults to 0, so if you use offset=1, you’ll miss the first element in the dataset. Count defaults to 10. For example, this URL includes query string parameters for pagination:
    
    https://usX.api.mailchimp.com/3.0/campaigns?offset=0&count=10

Cyclr will compute this value using the current page being requested and the **PageSizeInbound **property, e.g. to get all objects from a system containing 23 objects using a PageSizeInbound of 10, this would be the process in pseudo code:

    CYCLR_PAGE_SIZE = PageSizeInbound // e.g. 10.  
    CYCLR_PAGE_NUMBER = 1 // start with the first page.  
    
    WHILE (objects exist to return)  
    {  
        CYCLR_PAGE_OFFSET = ((CYCLR_PAGE_NUMBER - 1) * CYCLR_PAGE_SIZE)  
        Get CYCLR_PAGE_SIZE number of objects, starting at CYCLR_PAGE_OFFSET  
        CYCLR_PAGE_NUMBER = CYCLR_PAGE_NUMBER + 1 // move to the next page.
    }

#### CYCLR_PAGE_SIZE

The number of objects to be requested per page. This is set by the **PageSizeInbound **property at the Connector level.

#### CYCLR_PAGE_NEXT_URL

The field location in the response that contains the next page URL.

#### CYCLR_PAGE_TOKEN

Page token in the response that is used in subsequent requests. This is sometimes called cursor pagination.

In the example of GoCardless, the ID of the last resource returned is in a meta field. This field value needs to be passed in the query string in the next request.

If the API requires multiple page tokens, you can use CYCLR_PAGE_TOKEN**_{% raw %}{NAME}{% endraw %}** to retrieve them.

#### CYCLR_IGNORE_PARAMETER

Use this when a Connector-level Parameter exists, but is not valid for a particular Method so should be overridden. You must define the Parameter as normal, but provide the CYCLR_IGNORE_PARAMETER variable as the value to have it ignored.

#### Examples of inbound paging definitions:

API 1 with page number and page size

{% raw %}
    "Parameters": [  
        {  
           "TargetType":"QueryString",  
           "TargetName":"page",  
           "Values":["CYCLR_PAGE_NUMBER"],  
           "Hide": true  
       },  
       {
           "TargetType":"QueryString",
           "TargetName":"limit",
           "Values":["CYCLR_PAGE_SIZE"],
           "Hide": true
       }
     ]
{% endraw %}

API 2 with page offset and page size

{% raw %}
    "Parameters": [  
        {
            "TargetType": "QueryString",
             "TargetName": "offset",
             "Values": ["CYCLR_PAGE_OFFSET"],
             "Hide": true
         },
         {
             "TargetType": "QueryString",
             "TargetName": "count",
             "Values": ["CYCLR_PAGE_SIZE"],
             "Hide": true
         }
     ]
{% endraw %}

API 3 with next page URL

{% raw %}
    "Parameters": [
    {
    "TargetType": "ResponseField",
    "TargetName": "result.nextRecordsUrl"
    "Values": ["CYCLR_PAGE_NEXT_URL"]
    "Hide": true
    }
    ]
{% endraw %}
  

API 4 with page token

{% raw %}
    "Parameters": [
    {
    "TargetType": "ResponseField",
    "TargetName": "meta.cursors.after"
    "Values": ["CYCLR_PAGE_TOKEN"]
    "Hide": true
    },
    {
    "TargetType": "QueryString",
    "TargetName": "after"
    "Values": ["CYCLR_PAGE_TOKEN"]
    "Hide": true
    }
    ]
{% endraw %}

API 5 with multiple page tokens

{% raw %}
    "Parameters": [
    {
    "TargetType": "ResponseField",
    "TargetName": "meta.cursors.after"
    "Values": ["CYCLR_PAGE_TOKEN"]
    "Hide": true
    },
    {
    "TargetType": "QueryString",
    "TargetName": "after"
    "Values": ["CYCLR_PAGE_TOKEN"]
    "Hide": true
    },
    {
    "TargetType": "ResponseField",
    "TargetName": "meta.cursors.filter"
    "Values": ["CYCLR_PAGE_TOKEN_FILTER"]
    "Hide": true
    },
    {
    "TargetType": "QueryString",
    "TargetName": "after"
    "Values": ["CYCLR_PAGE_TOKEN_FILTER"]
    "Hide": true
    }
    ]
{% endraw %}

#### Outbound Paging Variables

Outbound paging only requires one variable to locate the array in the request body. Cyclr identifies when it has “too much” data to pass in one request by comparing it to the **PageSizeOutbound** property. If it has more, it chops the data into multiple requests automatically.

#### Outbound Array Location

Use the same notation as request/response format connector field. Specify the location of the array and not a field in the array.

#### Examples of outbound paging definitions:

    "PagedOutboundLocation": "data.[records]"