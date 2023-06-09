---
title: ChatGPT authentication
sidebar: cyclr_sidebar
permalink: chatgpt-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## ChatGPT setup

### Requirements

To connect with Cyclr, you need a OpenAI account, **API key**, and **organization ID**. You can register for an OpenAI account on the [OpenAI website](https://platform.openai.com/signup).

> **Note**: OpenAI API access is a paid for service. For more information on pricing, see the [OpenAI documentation](https://openai.com/pricing).

### Get an API key

1. Go to the [**API keys**](https://platform.openai.com/account/api-keys) page.
2. Select **Create new secret key**.
3. Enter a name for the new secret key.
4. Select **Create secret key**.
5. Make note of the API key displayed in the modal text box.

### Get your organization ID

An organization ID allows you to use API requests against a specific organization's subscription quota. You can find the organization ID on the [Organization settings](https://platform.openai.com/account/org-settings) page of the OpenAI website.

</section>
<section class="card">

## Cyclr account setup

Cyclr asks for the below values when you install the ChatGPT connector into an account:

| **Value**               | **Description**                                              |
| :---------------------- | :----------------------------------------------------------- |
| **OpenAI Organization** | **Optional**: the [OpenAI organization](#get-your-organization-id) to use for API requests. Usage from the API requests will count against the specified organization's subscription quota. |
| **API Key**             | The [OpenAI API key](#get-an-api-key) to make API requests with. |

> **Note**: You can use different details for different accounts.

</section>
