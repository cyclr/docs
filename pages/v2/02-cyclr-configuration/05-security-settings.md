---
title: OAuth Client Credentials
sidebar: cyclr_sidebar
permalink: console-security
tags: [cyclr-config]

menus:
    cyclr-configuration:
        title: Security settings
        identifier: console-security
        toggleonly: menutoggleonly
        weight: 5
---
{::options parse_block_html="true" /}
<section class="card">

The Cyclr API validates requests against OAuth client credentials.

## Password Grant Client ID

> **Warning**: Cyclr doesn’t support Password Grant any more. Password Grant still functions but may stop, so migrate to client credentials to avoid errors.

This section displays the Password Grant client ID. To refresh this client ID and invalidate existing Password Grant tokens, select the **Refresh** button.

</section>
<section class="card">

## Client Credentials

You need client credentials to authenticate with the Cyclr API. This section displays any existing client ID’s, when they were created, and a description. To view the associated client secret, select the **View Client Secret** eye icon. 

You can also select the **Delete Client Credentials** bin icon to delete a set. When you delete credentials, any access tokens associated with those credentials no longer work to authenticate.

To generate a new set of client credentials:

1. Select the **Generate Client Credentials** button.
2. Type in a description to help you identify the credential set.
3. Select **Create**.

**Note**: You can only have 5 sets of unique credentials at a time.

</section>
<section class="card">

## Access Tokens

The OAuth page also displays your access tokens. The list details the scope and whether the access token is for a specific account, as well as the expiry date. 

To delete an access token, select the **Revoke Access** bin icon.

</section>
