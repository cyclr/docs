---
title: Accessing the Cyclr API
sidebar: cyclr_sidebar
permalink: console-api
tags: [managing-cyclr]

---

## OAuth Client Credentials

### Password Grant Client ID

The Password Grant is no longer the recommended way to authenticate API requests. As such this will be deprecated in the future. However accounts which had Password Grant Client IDs set up will still be able to access and refresh them here.
For more details on why this is no longer recommended please see [OAuth 2.0 Password Grant](https://oauth.net/2/grant-types/password/).
 
### Client Credentials

The Client ID is used to authenticate calls to the Cyclr API. 
Here you're able to generate up to 5 unique pairs of Client IDs and Secrets. Client credentials can also be revoked here.
 
### Access Tokens

The access token represents the authorization of a specific application to access specific parts of a user’s data.
This section lists each time an Access Token has been generated for use with the API along with the Client ID which was used to generate it, the account by which it was generated, the expiry date, and the ability to revoke active access tokens.
 
