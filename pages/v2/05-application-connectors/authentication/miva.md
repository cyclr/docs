---
title: Miva authentication
sidebar: cyclr_sidebar
permalink: miva-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

## Miva setup

To set up the Miva connector, you need to authenticate with the following details.

<a link="get-store-domain"></a>

### Get store domain

You can find the domain of your store in your store URL. For example, if your store URL is `https://mydomain.mivamerchantdev.com/` then the store domain is `mydomain.mivamerchantdev.com`.

<a link="get-store-folder"></a>

### Get store folder

You can find your store folder in the admin URL of your store. For example, if the admin URL of your store is `https://mydomain.mivamerchantdev.com/mm5/admin.mvc` then the store folder is `mm5`. For more information, see [Miva's documentation on API Endpoints](https://docs.miva.com/json-api/#api-endpoint).

<a link="get-store-code"></a>

### Get store code

You can find your store code in your store URL. For example, if your store URL is `https://mydomain.mivamerchantdev.com/` then the store code is `mydomain`.

<a link="generate-signature"></a>

### Generate signature

You can generate a signature from the Miva admin page of your store under **Users > API tokens**. For mroe information, see [Miva's documentation on Authentication](https://docs.miva.com/json-api/#authentication).

<a link="generate-access-token"></a>

### Generate access token

You can generate an access token from the Miva admin page of your store under **Users > API tokens**. For more information, see [Miva's documentation on Authentication](https://docs.miva.com/json-api/#authentication).

</section>
<section class="card">
  
## Cyclr setup

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
