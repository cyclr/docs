---
title: Exceptions
sidebar: cyclr_sidebar
permalink: exceptions
tags: [templates]

menus:
    scripting:
        title: Exceptions
        identifier: exceptions
        toggleonly: menutoggleonly
        weight: 5                                                                                   
---
{::options parse_block_html="true" /}
<section class="card">

Exceptions are errors that prevent your script from performing as you expect. You can use these exception functions for to deal with authentication errors with your custom connector.

</section>
<section class="card">

## <code>AuthRefreshException</code>

**Connector builder only**.

You can use this exception to force refresh the OAuth 2 authentication token. If the OAuth 2 endpoint doesn’t return a definite token expiry time, the `AuthRefreshException` exception can be useful.

When Cyclr receives the exception, Cyclr calls the OAuth 2 Access Token URL to get a new access token.

### <code>AuthRefreshException</code> examples

For example, an API returns the code 200 with an error code in the response when the token becomes invalid:

```js
function after_action() {
    if (method_response != null && method_response.error != null && typeof method_response.error !== 'undefined' && method_response.error === 'invalid_grant') {
        throw new AuthRefreshException();
    }
   
    return true;
}
```

If an API returns a non-2xx HTTP status code when the auth token becomes invalid, you can throw `AuthRefreshException` in `after_error`:

```js
function after_error() {
    if (method_error != null && method_error.error != null && method_error.statusCode.toString() === '403') {
        throw new AuthRefreshException();
    }


    return true;
}
```

</section>
<section class="card">

## <code>AuthSessionException</code>

**Connector builder only**.

You can use this exception to force refresh the authentication session.

When Cyclr receives this exception, Cyclr calls the Post Install Property Value Lookup Method to start a new session.

### <code>AuthSessionException</code> examples
For example, an API returns 200 with an error code in the response when the session expires:

```js

function after_action() {
    if (method_response != null && method_response.error_code != null && typeof method_response.error_code !== 'undefined' && method_response.error_code === 'You are not logged on.') {
        throw new AuthSessionException();
    }


    return true;
}
```
If an API returns a non-2xx HTTP status code when the auth session expires, you can throw `AuthSessionException` in `after_error`:

```js
function after_error() {
    if (method_error != null && method_error.statusCode != null && method_error.statusCode.toString() === '403') {
        throw new AuthSessionException();
    }
   
    return true;
}
```
</section>
