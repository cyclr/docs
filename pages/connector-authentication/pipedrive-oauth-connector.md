---
title: Pipedrive (OAuth2.0) Connector Guide
sidebar: cyclr_sidebar
permalink: pipedrive-oauth-connector
tags: [connector]
---

# Partner Setup
-------------
Cyclr requires Pipedrive to use OAuth 2.0 authentication for remote API access. You must register Cyclr within Pipedrive as its own App to receive a Client ID and Client Secret. This enables Cyclr to authenticate and connect with Pipedrive.

> Note: Due to how Pipedrive authentication works, customers themselves will need to follow the below Pipedrive setup process.  You may wish to use the standard (non-OAuth) Pipedrive Connector if you don't want your customer to have this responsibility.  With the standard Connector only their personal API Key is required for installation. (https://support.pipedrive.com/en/article/how-can-i-find-my-personal-api-key)

## Pipedrive Setup

To obtain Client ID and Client Secret values from within Pipedrive:

### Enable a Developer Sandbox Account

To create a Developer Sandbox Account, Pipedrive requires you to complete the following [form](https://developers.pipedrive.com/start-here). This allows you to access the **Marketplace Manager**. Without this, you will be unable to create the Pipedrive App required for authentication with Cyclr. The official Pipedrive documentation on this process can be found [here](https://pipedrive.readme.io/docs/developer-sandbox-account).

### Create an app within the Marketplace Manager

Create a new App and obtain the Client ID and Client Secret using the steps below. The official Pipedrive documentation for creating an App can be found [here](https://pipedrive.readme.io/docs/marketplace-creating-a-proper-app).

1. Go to the **Marketplace Manager** found [here](https://cyclrdevs.pipedrive.com/settings/marketplace_manager). This is only accessible if you have a Developer Sandbox Account as explained above.
2. Click `Create New App`.
3. Select `No` to set the App to unlisted and internal/private, then click `Next`. Pipedrive's documentation on app types can be found [here](https://pipedrive.readme.io/docs/marketplace-creating-a-proper-app#types-of-apps).
4. Complete the App form as required by Pipedrive.
5. Cyclr authentication is handled under the **OAuth & Access scopes** heading. Enter the callback URL in the **Callback URL** field. The callback URL has the following format:
   https://{Your Cyclr service domain e.g. app-h.cyclr.com}/connector/callback
6. Enable the required **Access scopes** as either **Read only** or **Full access**. The official Pipedrive documentation on access scopes can be found [here](https://pipedrive.readme.io/docs/marketplace-scopes-and-permissions-explanations).
7. Click `Save` to create the App. This will take you back to the Marketplace Manager.
8. Click the newly created App within the **Marketplace Manager** to be taken to the settings again. Under the **OAuth & Access scopes** heading you will now find the **Client ID** and can click `Show` to reveal the **Client secret**. Make a note of these as they will be required by Cyclr to set up the Pipedrive Connector.

# Pipedrive Integration Workflow Building Examples
-------------
<h2>Automating Pipedrive</h2> 
<h3 id="deals" class="intercom-align-left">Automating Deals</h3><p class="intercom-align-left">Our Pipedrive connector includes a number of webhooks. These are real-time event notifications that fire when something happens to a deal, e.g. when one is created or updated.</p><p class="intercom-align-left">Example uses:</p><ul><li>Sync new deals with another system</li><li>Trigger time-based actions for deals stuck at a certain stage</li><li>At key deal stages, add the associated contacts to a marketing system</li><li>Automate internal Pipedrive deals, e.g. when a deal hits a certain stage move it to a different pipeline</li></ul><h4 class="intercom-align-left">Deal stage lookups</h4><p class="intercom-align-left">One of the keys to using Pipedrive’s deals is working with the Stage ID in a Cyclr Decision step. In doing this, you can then trigger the next appropriate action – either in Pipedrive or in another app.</p><div class="intercom-container intercom-align-left"><img src="https://downloads.intercomcdn.com/i/o/29084048/e84a2753288301ecbc2bb070/pipedrive-deal-lookup.gif"></div><h3 id="forms" class="intercom-align-left">Forms</h3><p class="intercom-align-left">With Cyclr, you can integrate Pipedrive with a number of form building apps including:</p><ul><li>Contact Form 7</li><li>Gravity Forms</li><li>Typeform</li><li>SurveyMonkey</li></ul>

<h3>Automate Your Sales Pipeline</h3><p>Cyclr lets you automate your sales process by using webhooks and triggers based on movements between pipeline stages.</p><p>Example uses:</p><ul><li>Send deals to separate pipelines for other teams to complete work on</li><li>Automatically assign reminders for yourself or team members based on deal stages</li><li>Trigger external application events when a deal reaches a chosen stage</li><li>Automatically send emails and messages when a deal hits a particular stage</li></ul><h2>Automation Implementation</h2><p>Follow our below video guide to get you started with Pipedrive Automation.</p><p></p><center><iframe width="500" height="281" src="https://www.youtube.com/embed/GTBgHGIh_Mo?feature=oembed" frameborder="0" gesture="media" allowfullscreen=""></iframe></center><p></p>

<h3>Pipedrive Updates with Webhooks</h3><p>Cyclr combined with Pipedrive’s webhook builder allows you to trigger automation workflows based on a wide range of actions in your CRM.</p><p>Our Webhook connect includes an automatic field discovery feature, helping you set up your automation workflows in no time.</p><p>Watch the video below to see how you can make use of Pipedrive’s webhooks.</p><p><center><iframe width="500" height="281" src="https://www.youtube.com/embed/WclcTlrAsi0?feature=oembed" frameborder="0" gesture="media" allowfullscreen=""></iframe></center></p>

<h2>Pipedrive and Contact Form 7 Integration</h2><p>Getting Contact Form 7 to work with your Pipedrive CRM has been a pain for a long time, so you’ll be please to see that you can connect the two with Cyclr.</p><h3>Why Integrate Contact Form 7 and Pipedrive?</h3><p>Contact Form 7 is still one of the most popular form building applications around. While it’s name suggest it is just for contact forms, it has many usages when combined with Pipedrive, including:</p><ul><li>Adding new website enquiries directly into your CRM</li><li>Creating new deals direct from forms</li><li>Managing helpdesk enquiries</li><li>Passing user registration data across your company’s application stack</li></ul><p>Take a look at our video tutorial to find out how to get it set up.</p><p>&nbsp;</p><p></p><center><iframe width="500" height="281" src="https://www.youtube.com/embed/G8gVVAeNB8Q?feature=oembed" frameborder="0" gesture="media" allowfullscreen=""></iframe></center><p></p>

<h2>Automatically Add New Users to your CRM</h2><p>Cyclr lets you integrate Pipedrive with Intercom, so you can add and update user data within your CRM automatically.</p><p>Cyclr’s Intercom connector contains a range of webhooks that can be triggered when an event criteria in Intercom is met. Take a look at the video guide below to see how you can set it up.</p><p></p><center><br> <iframe width="500" height="281" src="https://www.youtube.com/embed/nvwAfTPC6Ak?feature=oembed" frameborder="0" gesture="media" allowfullscreen=""></iframe></center><p></p>
