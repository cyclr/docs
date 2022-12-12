
## Partner Setup ##

This document explains how to setup access to Zoho and to install the Zoho CRM Connector.

### OAuth Setup ###

You'll need to register your Cyclr Partner with Zoho by creating a "Client" in your [Zoho API Console](https://accounts.zoho.com/developerconsole).

[Zoho's own documentation on this can be found here](https://www.zoho.com/accounts/protocol/oauth-setup.html)


* When asked which **Client Type** you wish to create, choose "Server-based Application".

![](./images/Zoho_ClientType.png)

<br/>

* Enter an **Authorized Redirect URI** using this format:

{% raw %}`https://{{Your Cyclr Service Domain}}/connector/callback`{% endraw %}

e.g. ```https://app-h.cyclr.com/connector/callback```

You can find your **Service Domain** within your Cyclr Console from the **Settings** menu then **General Settings**.

### Connector Setup ###

Once you have your Client ID and Client Secret from Zoho, go to your Cyclr Console then Connectors > Application Connector Library, search for **Zoho CRM**, click the Padlock button next to it and set them so they're used when installing the Connector.

## Scopes
The scopes are defaulted to "ZohoCRM.modules.ALL,ZohoCRM.users.ALL,ZohoCRM.org.ALL,ZohoCRM.settings.roles.ALL", however you can enter your own scopes if you wish to restrict the connectors access further.

See Zoho's documentation [here](https://www.zoho.com/crm/developer/docs/api/v2/scopes.html) on available scopes.
