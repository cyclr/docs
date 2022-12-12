
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content required" markdown="1">

### API user ##

Setup an API user with the required access rights. 

See the [Adestra user setup documentation](https://app.adestra.com/doc/page/current/index/admin/users/users).

The account, username and password will be required to authenticate the connector.

## Authenticating the connector
*Username:* Prefix with the lower-case account name and a dot, e.g. my_account.username.

*Password:* password of the API user

## Notes


### Table methods

Some Adestra method calls require a table ID. 

These table methods include the table ID in the response body:
- List Core
- List Data

### Contact methods 

Contact methods have the Default ID and Email specified.

Add custom fields as specified on the method for the required table. 

Download table definitions from the Adestra portal or via the connector table methods.
