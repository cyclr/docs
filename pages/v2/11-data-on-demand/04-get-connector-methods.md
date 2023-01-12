---
title: Get connector methods
sidebar: cyclr_sidebar
permalink: get-connector-methods
tags: [data-on-demand]

menus:
    data-on-demand:
        title: Get connector methods
        identifier: get-connector-methods
        toggleonly: menutoggleonly
        weight: 4
---
{::options parse_block_html="true" /}
<section class="card">
Each authenticated connector in an account has multiple available connector methods you can use. To call a connector method, you need the  MethodUniqueIdentifier.
You can use the [`/v1.0/connectors/{name}/methods`](https://api.cyclr.uk/docs/index#!/Connectors/Connectors_Methods_GET_0) request to retrieve a list of available methods, and their identifiers, for a connector.


</section>
<section class="card">
## Request

 `GET https://yourCyclrDomain/v1.0/connectors/{name}/methods`

For connectors with a version, use:

 `GET https://{yourCyclrDomain}/v1.0/connectors/{name}/{version}/methods`

### Request parameters

| **Parameter**         | **Description**                                                                   |
|:----------------------|-----------------------------------------------------------------------------------|
| `{yourCyclrDomain}`   | Replace with the API domain of your version of Cyclr. For example, api.cyclr.com. |
| `{name}`              | Replace with the [connector name](get-account-connectors).                                                  |
| `{version}`           | Replace with the connector version.                                               |


</section>
<section class="card">
## Example response 

```
[
	{
		"Id": 116,
		"Name": "Update Ticket",
		"Description": "Updates a ticket.",
		"EndPoint": "https://api.example/updateTicket",
		"MethodUniqueIdentifier": "8f8df8ef-3007-11e7-a033-06abe76375dd"
	},
	{
		"Id": 117,
		"Name": "Delete Ticket",
		"Description": "Deletes a ticket.",
		"EndPoint": "https://api.example/deleteTicket",
		"MethodUniqueIdentifier": "56d8a7ef-3457-af37-a3fd-0645386a75bd"
	}
]
```
### Response parameters

| **Parameter**            | **Description**               |
|:-------------------------|-------------------------------|
| `Id`                     | The method ID.                |
| `Name`                   | The method name.              |
| `Description`            | The method description.       |
| `EndPoint`               | The API endpoint.             |
| `MethodUniqueIdentifier` | The unique method identifier. |


</section>
<section class="card">
## Related pages

*  [Get account connectors](get-account-connectors)
*  [Call a connector method](call-a-connector-method)

</section>
