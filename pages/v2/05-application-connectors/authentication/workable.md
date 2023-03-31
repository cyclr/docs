---
title: Workable Authentication
sidebar: cyclr_sidebar
permalink: workable-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
### Partner Setup
API credentials will need to be generated in Phrase's frontend:
* Go to the Workable frontend and log in with your details
*  Go to **Settings**
*  Find the **Integrations** section
*  Select **Generate Token**
Make a note of your User Token or Partner token to use in the next steps.
### Cyclr Setup
Setup your Workable connector within Cyclr:
*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Workable**
*   Click the **Setup** button
Enter the following values:
**Sub Domain**: The sub-domain of your Workable instance. This can be found in the URL of your Workable frontend after 'https://'
**Access Token**: Retrieved from the **Partner Setup** steps above.
Select next and your connector will be authenticated.
</section>
