---
title: Snowflake Authentication
sidebar: cyclr_sidebar
permalink: snowflake-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">
    
<a name="snowflake-setup"></a>
## Snowflake setup

You need the following information to set up the Snowflake connector in Cyclr:

-   The [client ID and client](#getting-the-client-id-and-client-secret) secret obtained by [creating a security integration](#creating-a-secutiry-integration) in Snowflake.
-   The [account identifier](#getting-the-account-identifier) associated with your Snowflake account.

<a name="creating-a-secutiry-integration"></a>
### Create a security integration

You need to create a security integration in Snowflake to [get the client ID and client secret](#get-the-client-id-and-client-secret). For more information., see Snowflake's guide on how to [create a security integration](https://docs.snowflake.com/en/sql-reference/sql/create-security-integration.html#snowflake-oauth) in the Snowflake console. The following example creates a security integration called `cyclr_oauth` that issues a refresh token once every 90 days:

```sql
create or replace security integration
    cyclr_oauth
    TYPE = OAUTH
    ENABLED = TRUE
    OAUTH_CLIENT = CUSTOM
    OAUTH_CLIENT_TYPE = CONFIDENTIAL
    OAUTH_REDIRECT_URI = 'https://example.cyclr.com/connector/callback'
    OAUTH_ISSUE_REFRESH_TOKENS = TRUE
    OAUTH_REFRESH_TOKEN_VALIDITY = 7776000;
```

> **Warning**: Snowflake does not allow you to refresh tokens with the API. The user needs to log in again once the refresh token expires. To extend the duration of the refresh token, you can contact your Snowflake account administrator. For more information, see Snowflakes documentation on [OAuth](https://community.snowflake.com/s/article/FAQs-Snowflake-OAuth).

> **Note**: The `OAUTH_REDIRECT_URI` field needs to point to the OAuth redirect URL of your Cyclr account. The URL has the format: `https://{Your Cyclr service domain e.g. app-h.cyclr.com}/connector/callback`.

<a name="getting-the-client-id-and-client-secret"></a>
### Get the client ID and client secret

You need a client ID and client secret to authenticate the Snowflake connector in Cyclr. Before you can get these credentials, you need to [create a security integration](#creating-a-secutiry-integration). For more information on how to get the client ID and client secret, see the [Snowflake documentation](https://docs.snowflake.com/en/sql-reference/functions/system_show_oauth_client_secrets.html). The following example gets the client ID and client secret for the security integration created in the previous section:

```sql
select system$show_oauth_client_secrets('CYCLR_OAUTH');
```

**Note**: The integration name `cyclr_oauth` is converted to upper case and you need to enter `CYCLR_OAUTH` instead for this request.

<a name="getting-the-account-identifier"></a>
### Getting the account identifier

You need your account identifier to authenticate the Snowflake connector in Cyclr. Your account identifier is the subdomain in your Snowflake account URL provided on account creation. This is the same URL that you use to log in to Snowflake. For example, the account URL `https://AB12345.europe-west1.gcp.snowflakecomputing.com` has the account identifier `AB12345.europe-west1.gcp`.

</section>

<section class="card">
    
<a name="cyclr-setup"></a>
## Cyclr setup

To set up your Snowflake connector within your Cyclr console:

1. Go to your **Cyclr Console**.
2. Select **Connectors** > **Application Connector Library** at the top of the page.
3. Use the search box to find the **Snowflake** connector.
4. Select the **Setup Required** icon.
5. Enter the below values, omitting this step will allow you to use different settings for each account on installation:
    | Value             | Description                                                  |
    | ----------------- | ------------------------------------------------------------ |
    | **Client ID**     | The [client ID](#getting-the-client-id-and-client-secret) of your Snowflake account. |
    | **Client Secret** | The [client secret](#getting-the-client-id-and-client-secret) of your Snowflake account. |
7. Select **Save Changes**.

<a name="account-setup"></a>
### Account setup

Cyclr asks for the following values when you install the Snowflake connector within an account:

| Value                  | Description                                                  |
| :--------------------- | :----------------------------------------------------------- |
| **Client ID**          | The client ID of your Snowflake account, if you did not enter this in step 5 above. |
| **Client Secret**      | The client secret of your Snowflake account, if you did not enter this in step 5 above. |
| **Account Identifier** | The [account identifier](#getting-the-account-identifier) of your Snowflake account. |
| **Warehouse**          | The Snowflake warehouse to process queries with.             |
| **Database**           | The Snowflake database to access data in.                    |
| **Schema**             | The Snowflake schema to access data in.                      |

**Note**: You can install the connector without providing a warehouse, database, and schema and use methods in the `Utilities` category to list accessible warehouses, databases, and schemas.

</section>
