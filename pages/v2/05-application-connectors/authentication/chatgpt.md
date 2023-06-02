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

To connect with Cyclr, you need a OpenAI account and an API key. You can register for an OpenAI account [here](https://platform.openai.com/signup).

> **Note**: OpenAI API access is a paid for service. More information on pricing can be found [here](https://openai.com/pricing).

### Get an API key

1. Go to the [**API keys**](https://platform.openai.com/account/api-keys) page.
2. Select **Create new secret key**.
3. Enter a name for the new secret key.
4. Select **Create secret key**.
5. Make note of the API key displayed in the modal text box.

### Get your organization ID

An organization ID allows API requests to be used against a specific organizations subscription quota:

1. Go to the [Organization settings](https://platform.openai.com/account/org-settings) page.
2. Make note of the **Organization ID**.

</section>

<section class="card">

## Cyclr setup


### Account setup

Cyclr asks you for the below values when you install the ChatGPT connector into an account:

| **Value**               | **Description**                                              |
| :---------------------- | :----------------------------------------------------------- |
| **OpenAI Organization** | The [OpenAI organization](#get-your-organization-id) to use for API requests. Usage from the API requests will count against the specified organization's subscription quota. Optional. |
| **API Key**             | The [OpenAI API key](#get-an-api-key) to make API requests with. |

> **Note**: You can use different details for different accounts.

</section>
