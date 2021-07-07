---
title: Pipedrive Connector Guide
sidebar: cyclr_sidebar
permalink: pipedrive-connector.html
tags: [connector]
---

# Pipedrive Integration Workflow Building Examples #
-------------
<h2>Automating Pipedrive</h2> 
<h3 id="deals" class="intercom-align-left">Automating Deals</h3><p class="intercom-align-left">Our Pipedrive connector includes a number of webhooks. These are real-time event notifications that fire when something happens to a deal, e.g. when one is created or updated.</p><p class="intercom-align-left">Example uses:</p><ul><li>Sync new deals with another system</li><li>Trigger time-based actions for deals stuck at a certain stage</li><li>At key deal stages, add the associated contacts to a marketing system</li><li>Automate internal Pipedrive deals, e.g. when a deal hits a certain stage move it to a different pipeline</li></ul><h4 class="intercom-align-left">Deal stage lookups</h4><p class="intercom-align-left">One of the keys to using Pipedrive’s deals is working with the Stage ID in a Cyclr Decision step. In doing this, you can then trigger the next appropriate action – either in Pipedrive or in another app.</p><div class="intercom-container intercom-align-left"><img src="https://downloads.intercomcdn.com/i/o/29084048/e84a2753288301ecbc2bb070/pipedrive-deal-lookup.gif"></div><h3 id="forms" class="intercom-align-left">Forms</h3><p class="intercom-align-left">With Cyclr, you can integrate Pipedrive with a number of form building apps including:</p><ul><li>Contact Form 7</li><li>Gravity Forms</li><li>Typeform</li><li>SurveyMonkey</li></ul>

<h3>Automate Your Sales Pipeline</h3><p>Cyclr lets you automate your sales process by using webhooks and triggers based on movements between pipeline stages.</p><p>Example uses:</p><ul><li>Send deals to separate pipelines for other teams to complete work on</li><li>Automatically assign reminders for yourself or team members based on deal stages</li><li>Trigger external application events when a deal reaches a chosen stage</li><li>Automatically send emails and messages when a deal hits a particular stage</li></ul><h2>Automation Implementation</h2><p>Follow our below video guide to get you started with Pipedrive Automation.</p><p></p><center><iframe width="500" height="281" src="https://www.youtube.com/embed/GTBgHGIh_Mo?feature=oembed" frameborder="0" gesture="media" allowfullscreen=""></iframe></center><p></p>

<h3>Pipedrive Updates with Webhooks</h3><p>Cyclr combined with Pipedrive’s webhook builder allows you to trigger automation workflows based on a wide range of actions in your CRM.</p><p>Our Webhook connect includes an automatic field discovery feature, helping you set up your automation workflows in no time.</p><p>Watch the video below to see how you can make use of Pipedrive’s webhooks.</p><p><center><iframe width="500" height="281" src="https://www.youtube.com/embed/WclcTlrAsi0?feature=oembed" frameborder="0" gesture="media" allowfullscreen=""></iframe></center></p>

<h2>Pipedrive and Contact Form 7 Integration</h2><p>Getting Contact Form 7 to work with your Pipedrive CRM has been a pain for a long time, so you’ll be please to see that you can connect the two with Cyclr.</p><h3>Why Integrate Contact Form 7 and Pipedrive?</h3><p>Contact Form 7 is still one of the most popular form building applications around. While it’s name suggest it is just for contact forms, it has many usages when combined with Pipedrive, including:</p><ul><li>Adding new website enquiries directly into your CRM</li><li>Creating new deals direct from forms</li><li>Managing helpdesk enquiries</li><li>Passing user registration data across your company’s application stack</li></ul><p>Take a look at our video tutorial to find out how to get it set up.</p><p>&nbsp;</p><p></p><center><iframe width="500" height="281" src="https://www.youtube.com/embed/G8gVVAeNB8Q?feature=oembed" frameborder="0" gesture="media" allowfullscreen=""></iframe></center><p></p>

<h2>Automatically Add New Users to your CRM</h2><p>Cyclr lets you integrate Pipedrive with Intercom, so you can add and update user data within your CRM automatically.</p><p>Cyclr’s Intercom connector contains a range of webhooks that can be triggered when an event criteria in Intercom is met. Take a look at the video guide below to see how you can set it up.</p><p></p><center><br> <iframe width="500" height="281" src="https://www.youtube.com/embed/nvwAfTPC6Ak?feature=oembed" frameborder="0" gesture="media" allowfullscreen=""></iframe></center><p></p>

<h2>Authentication</h2>
#### Retrieving Client ID and Secret
*   Login to your Pipedrive front-end.
*   Navigate to Tools and Integrations > Marketplace Manager.
*   Create a new app.
*   Enter all required information. Set the callback URL (https://``Your Service Domain``/connector/callback). Permissions should be set to your specific needs, more information about what each scope does can be found here: https://pipedrive.readme.io/docs/marketplace-scopes-and-permissions-explanations
*   Note the Client ID and Secret from the "OAuth & Access scopes" area.
