---
title: Connector Paging
sidebar: cyclr_sidebar
permalink: connector-paging
tags: [connector-creation]
---

## Inbound and Outbound Paging

So that Cyclr can retrieve more objects than a remote API may allow in one request (some restrict this to 100 objects, for example), it can take advantage of an API’s paging functionality. This is referred to as **Inbound Paging**. Cyclr will repeatedly request pages of objects until it has retrieved them all.

When a remote API has a limit on the amount of data that can be sent in a single request, Cyclr will also be able to split large amounts of data that need to be sent into several small requests. This is referred to as **Outbound Paging**.

To set a Connector as using Paging, you can use the following Connector-level properties (they default to false – no paging – if not supplied).

| Connector Property | Description |
| --- | --- |
| Inbound Paging | Set to 'true' to activate by default in all appropriate methods. |
| Inbound Page Size |Set to the number of records that the API will return with a single call eg 100, |
| Outbound Page Size |Set to the number of records that the API will allow posted with a single call eg 100, | 

Note that the default for ourbound paging of 'false' at the Connector level.
 
These patrameters can be overriden and adjusted at the method level.

| Method Property | Description |
| --- | --- |
| Inbound Paging | Set to 'true' to activate by default in all appropriate methods. |
| Inbound Page Size |Set to the number of records that the API will return with a single call eg 100, |
| Outbound Paging | Set to 'true' to activate by default in all appropriate methods. |
| Outbound Page Size |Set to the number of records that the API will allow posted with a single call eg 100, | 

If values are not set at the method level they are inherited from those specified for the connector. 


## Inbound Paging Control Variables

It implement inbound paging Cyclr use the following variables.

| Variable | Description |
| --- | --- |
| CYCLR_PAGE_NUMBER | Cyclr will use the current page number it’s requesting here as it iterates through them. Use this with APIs that use page numbers and “number of objects to retrieve” values. The initial value will be one. |
| CYCLR_PAGE_OFFSET | Essentially a “row offset”, starting at 0. Use this with APIs that use offsets and “number of objects to retrieve” values. |
| CYCLR_PAGE_SIZE | The number of objects to be requested per page. This is set by the 'Inbound Page Size' property at the Connector or method level. |
| CYCLR_PAGE_NEXT_URL | The field location in the response that contains the next page URL. |
| CYCLR_PAGE_TOKEN | Page token in the response that is used in subsequent requests. This is sometimes called cursor pagination.
| CYCLR_IGNORE_PARAMETER |Use this when a Connector-level Parameter exists, but is not valid for a particular Method so should be overridden. You must define the Parameter as normal, but provide the CYCLR_IGNORE_PARAMETER variable as the value to have it ignored. |

## Using Paging Variables

### Example 1 - API using page number and page size

In this example the API requires the query sting to include the parameters 'page' and 'limit'.  Other APIs might use different names for these concepts.

| Target Type | Target Name | Disp Name | Desc | Trigger | Optional | Hiden | Value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QueryString| page | NA | NA | NA | NA | true | CYCLR_PAGE_NUMBER |
| QueryString| limit | NA | NA | NA | NA | true | CYCLR_PAGE_SIZE |

### Example 2 - API using page offset and page size

In this example the API requires the query sting to include the parameters 'offset' and 'limit'.  Other APIs might use different names for these concepts.

| Target Type | Target Name | Disp Name | Desc | Trigger | Optional | Hiden | Value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QueryString| page | NA | NA | NA | NA | true | CYCLR_PAGE_OFFSET |
| QueryString| limit | NA | NA | NA | NA | true | CYCLR_PAGE_SIZE |

### Example 3 - API using next page URL

| Target Type | Target Name | Disp Name | Desc | Trigger | Optional | Hiden | Value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ResponseField| result.nextRecordsUrl | NA | NA | NA | NA | true | CYCLR_PAGE_NEXT_URL |
  
### Example 4 - API using page token

This is used when the ID of the last resource returned is in a meta field (in the example meta.cursors.after). This field value needs to be passed in the query string in the next request.

| Target Type | Target Name | Disp Name | Desc | Trigger | Optional | Hiden | Value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ResponseField | meta.cursors.after | NA | NA | NA | NA | true | CYCLR_PAGE_TOKEN |
| QueryString | after | NA | NA | NA | NA | true | CYCLR_PAGE_TOKEN |
  
### Example 5 - API using multiple page tokens

| Target Type | Target Name | Disp Name | Desc | Trigger | Optional | Hiden | Value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ResponseField | meta.cursors.after | NA | NA | NA | NA | true | CYCLR_PAGE_TOKEN |
| QueryString | after | NA | NA | NA | NA | true | CYCLR_PAGE_TOKEN |
| ResponseField | meta.cursors.filter | NA | NA | NA | NA | true | CYCLR_PAGE_FILTER |
| QueryString | after | NA | NA | NA | NA | true | YCLR_PAGE_FILTER |

### Example 5 - API using page token & page number

| Target Type | Target Name | Disp Name | Desc | Trigger | Optional | Hiden | Value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ResponseField | meta.cursors.after | NA | NA | NA | NA | true | CYCLR_PAGE_TOKEN |
| QueryString | queryId | NA | NA | NA | NA | true | CYCLR_PAGE_TOKEN |
| QueryString| page | NA | NA | NA | NA | true | CYCLR_PAGE_NUMBER |
| QueryString| limit | NA | NA | NA | NA | true | CYCLR_PAGE_SIZE |

## Outbound Paging Variables

Outbound paging only requires one variable to locate the array in the request body. Cyclr identifies when it has “too much” data to pass in one request by comparing it to the **PageSizeOutbound** property. If it has more, it chops the data into multiple requests automatically.

### Outbound Array Location

Use the same notation as request/response format connector field. Specify the location of the array and not a field in the array.

### Examples of outbound paging definitions:

    "PagedOutboundLocation": "data.[records]"
