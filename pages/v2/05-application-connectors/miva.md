---
title: Miva Authentication
sidebar: cyclr_sidebar
permalink: miva-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

## Miva setup

### Get authentication details

To authenticate your connector, get the following details:

<a link="get-store-domain"></a>

#### Get store domain

The domain of your store is included in your store URL. For example, if your store URL is `https://mydomain.mivamerchantdev.com/` then the store domain is `mydomain.mivamerchantdev.com` .

<a link="get-store-folder"></a>

#### Get store folder

The folder of your store is included in the admin URL of your store. For example, if the admin URL of your store is `https://mydomain.mivamerchantdev.com/mm5/admin.mvc` then the store folder is `mm5`. See [Miva's documentation on API Endpoints](https://docs.miva.com/json-api/#api-endpoint) for more information.

<a link="get-store-code"></a>

#### Get store code

The store code of your store is included in your store URL. For example, if your store URL is `https://mydomain.mivamerchantdev.com/` then the store code is `mydomain`.

<a link="generate-signature"></a>

#### Generate signature

You can generate a signature from the Miva admin page of your store under **Users > API tokens**. See [Miva's documentation on Authentication](https://docs.miva.com/json-api/#authentication) for more information.

<a link="generate-access-token"></a>

#### Generate access token

You can generate an access token from the Miva admin page of your store under **Users > API tokens**. See [Miva's documentation on Authentication](https://docs.miva.com/json-api/#authentication) for more information.

</section>
<section class="card">
  
## Cyclr setup

### Account setup

Cyclr asks you for the below values when you install the Miva connector into an account:

| Value            | Description                                                  |
| :--------------- | :----------------------------------------------------------- |
| **Domain**      | The [domain](#get-store-domain) of the store to access.      |
| **Folder**       | The [folder](#get-store-folder) of the store to access.      |
| **Store Code**   | The [store code](#get-store-code) of the store to access.    |
| **Signature**    | The [HMAC-SHA256 signature](#generate-signature) to use for authentication. |
| **Access Token** | The [access token](#generate-access-token) to use for authentication. |

> Note: You can use different details for different accounts.

</section>
<section class="card">
  
## Additional information

### Generate HMAC when using a step script

All Miva API requests require a HMAC signature to be sent with every request. The connector automatically generates an HMAC signature before every request and uses the request body as part of the encoding when generating this.

If step script is used with a `before_action` function to modify the body of a request, this causes a mismatch between the generated HMAC signature and the request body. You need to manually regenerate the HMAC signature in this case by inserting a `RegenerateHmacSignature()` call before the final `return true`. For example:

```javascript
function before_action() {
    if (method_request != null && method_request.fields == null) {
	method_request.fields = ['id', 'first_name', 'last_name'];
    }
	
    RegenerateHmacSignature(); /* Regenerate HMAC signature. */
    return true;
}
```

</section>
