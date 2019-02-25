---
title: Custom Connector Properties
---

Name
----

Provides a name for the connector to be shown in the Cyclr UI.

CreatedOnUtc
------------

The date and time when the Connector file was created (in GMT timezone). Will be used to identify when a Connector should be updated in Cyclr. Format: “2015-12-14T11:20:00.000Z”. Leave the seconds and milliseconds as zeros (not that precise).

Description
-----------

Provides a description for the connector to be shown in the Cyclr UI. This should describe, in a sentence, what the app does.

Version
-------

This is the version of the product’s API and doesn’t necessarily match the version of the product itself.

AuthType
--------

This specifies what type of authentication is used by the remote endpoint.

*   **ApiKey **– the user should provide an API key as the HTTP header for the connector. Requires: _AuthScheme _(HTTP header field name).
*   **Basic **– the API uses HTTP basic authentication.
*   **OAuth1 **– the API uses OAuth 1.0a authentication. Requires: _ClientId _(also known as ConsumerKey), _ClientSecret _(also known as ConsumerSecret), _RequestTokenUrl_, _AuthorizeUrl_, _AccessTokenUrl_.
*   **OAuth2 **– the API uses OAuth 2 authentication. Requires: _ClientId_, _ClientSecret_, _AuthoriseUrl_, _AccessTokenUrl_.
*   **None **– no authentication required.
*   **AuthFields **– the API needs to inject authentication fields into the POST message. Requires: _Name_, _Key_, _Type_.

OAuth2Type
----------

This field will only be used if the **AuthType **is **OAuth2**.

*   **AuthorisationCode (Default)** – the client will redirect the user to the authorization server, the user will then be asked to login to the authorization server and approve the client.
*   **ClientCredentials** – client will get the access token from the authorization server without user challenge.
*   **PasswordCredentials** – client will get the access token from the authorization server using username & password.

Icon
----

Your connector needs an icon.

*   Minimum: square @ 256px / 256px
*   24-bit PNG on a transparent background

[Learn About Custom Connector Parameters & Triggers ](./parameters-and-triggers)