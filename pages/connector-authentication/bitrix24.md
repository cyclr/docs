---
title: Bitrix24 Authentication
sidebar: cyclr_sidebar
permalink: bitrix24-connector
tags: [connector]

---

## Bitrix24 setup

The Bitrix24 connector uses Bitrix24's Inbound Webhooks feature to make API requests.

<a name="create-inbound-webhook"></a>

### Create inbound webhook

Cyclr requires a webhook ID to install the Bitrix24 connector. From the Bitrix24 dashboard:

1. Select **Applications > Developer resources** in the left hand menu.
2. Select **Other**.
3. Select **Inbound webhook**.
4. Get the [webhook ID](#get-webhook-id).
5. [Assign permissions](#assign-permissions).
6. Select **Save**.

<a name="get-webhook-id"></a>

#### Get webhook ID

In the **Webhook to call REST API** field:

1. Make a note of the webhook ID. This is the random 16 character alphanumeric string that makes up part of the URL. For example, if the URL is `https://my.bitrix24instance.co.uk/rest/1/j2zdj8r9h0fdgsb3/` then the webhook ID is `j2zdj8r9h0fdgsb3`.

<a name="assign-permissions"></a>

#### Assign permissions

Cyclr requires the following permissions for the Bitrix24 connector to function correctly:

- `CRM (crm)`
- `Users (user)` 

Under the **Assign permissions** heading for each permission:

1. Select **+ select**.
2. Enter the required permission.
3. Select the required permission from the list.

## Cyclr setup

### Account setup

Cyclr asks you for the below values when you install the Bitrix24 connector within an account:

| Value          | Description                                                  |
| :------------- | :----------------------------------------------------------- |
| **URL**        | The URL of your Bitrix24 instance. For example, `https://my.bitrix24instance.co.uk`. |
| **Webhook ID** | The webhook ID of your Bitrix24 [Inbound Webhook](#create-inbound-webhook). |
