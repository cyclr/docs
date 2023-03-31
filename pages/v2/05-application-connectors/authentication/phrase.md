---
title: Phrase Authentication
sidebar: cyclr_sidebar
permalink: phrase-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

### Partner Setup

API credentials will need to be generated in Phrase's frontend:

* Go to the Phrase frontend and log in with your details
*  Go to **Settings** in the left menu bar
*  Find the **Integrations** section and select **Registered OAuth apps**
*  Select **New**
*  Enter a name and your callback URL (`https://[Your Cyclr Service Domain]/connector/callback`)
*  Select **Save**

Make a note of your Client ID to use in the next steps.

### Cyclr Setup

Setup your Phrase connector within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Phrase**
*   Click the **Setup** button

Enter the following values:

**Client ID**: Retrieved from the **Partner Setup** steps above.
**Client Secret**: Leave this value empty.
**US Instance?**: If your account has been created within Phrase's US data center, set this to true.

Select next and your connector will be authenticated.

</section>
