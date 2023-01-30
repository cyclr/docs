---
title: Selligent Authentication
sidebar: cyclr_sidebar
permalink: selligent
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
# Selligent


</section>
<section class="card">
## Partner Setup

To use the Selligent connector, you will need 

1. The server of your Selligent account, for example: **yourcompany.slgnt.eu** (without the https://)
2. Your Username
3. A Secret Key (aka Password).

### Username & Password

To be able to use the REST API a dedicated API user has to be created.

![connector setup](./images/APIUserCreate.png)

A name and login needs to be entered for the API user. 

The user's password is generated automatically and is used for hashing. The refresh button to the right of the field allows regenerating the password.

The API user must assign specific rights, indicating what operations can be performed through the API by that user and what operations can't.

![connector setup](./images/APIUserRights.png)

Once this is done, the Server, Username and Password (Key) can be entered when installing the connector.

</section>
