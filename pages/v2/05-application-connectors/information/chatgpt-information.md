---
title: ChatGPT information
sidebar: cyclr_sidebar
permalink: chatgpt-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">
  
## Chat sessions

Cyclr uses chat sessions to store chat history for the ChatGPT connector. Each chat session contains the ID of the chat, a log of the messages sent and received in the chat, and the date and time the chat was created and modified.

Methods inside the **Chat Sessions** and **Chats** method categories operate using chat sessions.

You can identify and access chat sessions with a **Chat Session ID**. This ID is stored as a string and can have any format. If the **Chat Session ID** doesn't exist when a method inside the Chat's method category is used, this creates a new chat session with the entered **Chat Session ID**.

> **Warning**: Cyclr prunes any chat session created or modified more than 30 days ago.

</section>
<section class="card">
  
## Token trimming

Each chat message sent has a token value based on the total content of all the messages in the chat session. As each chat session logs messages, the token total for the chat session increases as the chat session is used. For more infomration, see OpenAI's documentation on [tokens and how to count them](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them).

Each model has a limit on the number of tokens that can be used per request. For methods in the **Chats** method category, the available models have token limits as follows:

| Model name        | Model         | Token limit |
| ----------------- | ------------- | ----------- |
| ChatGPT           | gpt-3.5-turbo | 4,096       |
| GPT-4 8k context  | gpt-4         | 8,192       |
| GPT-4 32k context | gpt-4-32k     | 32,768      |

To automatically manage chat session tokens, methods in the **Chats** method category have **Trim Tokens?** and **Custom Token Limit** parameters that you can use.

#### Trim Tokens? 

Set this parameter to `true` to automatically trim chat sessions down to below the token limit for the model. If no model is found, a default token limit of `4096` is used. When you trim a chat session, Cylr trims the oldest message in the chat session first. This process repeats until the chat session is below the token limit, and then Cyclr sends the request with the trimmed chat session.

> **Note**: The token total for a chat session is an approximation made by Cyclr and may not reflect the token total the API calculates.

> **Warning**: If you enable **Trim Tokens?**, messages that Cyclr removes from chat sessions are permanently removed.

#### Custom Token Limit

Set this parameter to force a custom token limit for Cyclr to trim a chat session down to. This overrides the limit for the model and the default token limit. There is a lower limit of 100 tokens for this value to make sure that at least one message can be sent in the request.

</section>
<section class="card">

## Basic chat bot Cycle

You can set up a basic chat bot cycle:

### Install the Generic Webhook Utility Connector

1. Navigate to the install a Utility Connector page:
   - In the Cyclr Console:
     - Navigate to **Templates** > **Template Connectors**.
     - Select **+ Install New Utility**.
   - In the Cycle builder:
     - Select **+ Add Utility**.
2. Find the **Generic Webhook** connector and select **Install**.
3. Edit the **Name** field if you need to. This example sets the name to `ChatGPT webhook`.
4. Select **Next**.

### Setup the Generic Webhook connector

1. Navigate to the **Edit Connector** page of the **Generic Webhook** Connector:
   - In the Cyclr Console:
     - Navigate to **Templates** > **Template Connectors**.
     - Under the **Installed Utility Connectors** heading, select **Edit Connector** next to the **ChatGPT webhook** Connector.
   - In the Cycle builder:
     - In the right hand menu, under the **Utility Connectors** heading, select the **ChatGPT webhook** Connector.
     - Select **Settings**.
2. Under the **Methods and Fields** heading, select **Webhooks** > **Webhook**.
3. Under the **Request Fields** heading, select the **+** (Add Field) icon to add request fields for:
   - A `Chat Session ID` field that will receive the chat session ID to use for the chat request.
   - A `Message` field that will receive the message to send to the API.
4. Under the **Methods and Fields** heading, select **Webhooks** > **Synchronous Response**.
5. Under the **Response Fields** heading, select the **+**  icon to add a response field for:
   - A `Message` field that will return the message response from the API.

### Create the Cycle

Create a new Cycle as follows:

![chatgpt-cycle](./images/chatgpt-cycle.png)

Map the fields according to what you need:

#### List Chat Session Messages
The **Webhook** step grabs the request body.  

| Field           | Source                            |
| --------------- | --------------------------------- |
| Chat Session ID | **Webhook** > **Chat Session ID** |

#### Send System Message
The **List Chat Session Messages** step checks if the chat session already exists and sends an initial system message using the **Send System Message** if it doesn't.

| Field           | Source                                                       |
| --------------- | ------------------------------------------------------------ |
| Chat Session ID | **Webhook** > **Chat Session ID**                            |
| Model           | Use **Select a Value** to set the model.                     |
| Message         | Enter a system message that will define the tone of a new chat session. The user will not see this but ChatGPT will take this into account when the Cycle uses the **Send User Message** step. |

#### Send User Message
The **Send User Message** step sends the user message. 

| Field           | Source                                   |
| --------------- | ---------------------------------------- |
| Chat Session ID | **Webhook** > **Chat Session ID**        |
| Model           | Use **Select a Value** to set the model. |
| Message         | **Webhook** > **Message**                |

#### Synchronous Response
The **Synchronous Response** step replies to the external source with the answer ChatGPT generated.

| Field   | Source                                             |
| ------- | -------------------------------------------------- |
| Message | **Send User Message** > **Choice Message Content** |

### Use the cycle

To start the cycle, select **Run** in the Cycle builder. To use the chat bot cycle:

1. Select the **Step Setup** of the **Webhook** step.
2. Make note of the webhook URL
3. Post to this webhook URL from an external source, either another Cycle or an external client such as Postman, with a request body structure as follows:

   ```json
   {
   	"chatSessionId": "test-chat-session-1",
   	"message": "How do I convert miles to centimeters?"
   }
   ```

Cyclr saves all messages (system, user, and assistant) with the **Chat Session ID** provided. In this example, the ID is `test-chat-session-1`, and you can therefore post follow up requests with the same **Chat Session ID** to continue the conversation.
  
</section>
