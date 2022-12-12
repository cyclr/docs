---
title: Freshdesk Connector
sidebar: cyclr_sidebar
permalink: freshdesk-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
## Freshdesk Setup

To find your API key:

1. Visit the Freshdesk dashboard.
2. Click your profile picture in the top right of the screen.
3. Select **Profile Settings**
4. You will now see your API key on the right.



</section>
<section class="card py-5 my-5">
## Connector Setup

When the connector is setup on an account you will need to provide:
* **Freshdesk Domain**: The name of your Freshdesk domain, e.g. "myaccount.freshdesk.com" without "https://" or a trailing forward slash.  Must be a freshdesk.com domain; custom domains are not allowed.
* **API Key**: See above steps on where this can be found.



</section>
<section class="card py-5 my-5">
## Webhooks

If you wish to set up a **Ticket Closed** webhook step, you will first need to add it to your cycle.

Then open the Freshdesk dashboard, and follow these steps:


1. Click the **Admin** cog on the left hand side navigation bar.
    
    ![Admin cog](./images/cog.png)
2. Scroll down to the **Helpdesk Productivity** Section, and select **Automations**.

    ![Automations](./images/automations.png)
3. Choose **Rules that run on: Ticket Updates**.
4. Click **New rule**.
5. Set **Rule name** and **Involves any of these events** as follows:

    ![Rule settings](./images/rule_settings.png)
6. You can leave **On tickets with these properties** as it is.
9. Under Perform these actions, set **Choose Action** to **Trigger Webhook**.
10. Set Request Type to **POST**.
11. For the **URL**, you will need to go back to your Cyclr workflow, and copy the address from the webhook step.  You can find it by clicking the step's settings cog.
12. Leave the other fields as they are, and under Content, select **Advanced**.
13. The section should now look like this:

    ![Rule settings 2](./images/rule_settings2.png)
13. In the **Write custom API request** text box, paste the following template:
<!-- {% raw %} -->
```handlebars
{
	"ticket": {
		"id": " {{ticket.id}} ",
		"subject": " {{ticket.subject}} ",
		"ticket_type": " {{ticket.ticket_type}} ",
		"priority": " {{ticket.priority}} ",
		"due_by_time": " {{ticket.due_by_time}} ",
		"helpdesk_name": " {{helpdesk_name}} ",
		"portal_name": " {{ticket.portal_name}} ",
		"product_description": " {{ticket.product_description}} ",
		"source": " {{ticket.source}} ",
		"status": " {{ticket.status}} ",
		"triggered_event": " {{triggered_event}} ",
		"tags": " {{ticket.tags}} ",
		"latest_public_comment": " {{ticket.latest_public_comment}} ",
		"latest_private_comment": " {{ticket.latest_private_comment}} ",
		"portal_url": " {{ticket.portal_url}} ",
		"agent": {
			"name": " {{ticket.agent.name}} ",
			"email": " {{ticket.agent.email}} "
		},
		"company": {
			"name": " {{ticket.company.name}} ",
			"description": " {{ticket.company.description}} ",
			"note": " {{ticket.company.note}} ",
			"domains": " {{ticket.company.domains}} ",
			"health_score": " {{ticket.company.health_score}} ",
			"account_tier": " {{ticket.company.account_tier}} ",
			"renewal_date": " {{ticket.company.renewal_date}} ",
			"industry": " {{ticket.company.industry}} "
		},
		"contact": {
			"name": " {{ticket.contact.name}} ",
			"firstname": " {{ticket.contact.firstname}} ",
			"lastname": " {{ticket.contact.lastname}} ",
			"mobile": " {{ticket.contact.mobile}} ",
			"email": " {{ticket.contact.email}} ",
			"phone": " {{ticket.contact.phone}} ",
			"address": " {{ticket.contact.address}} ",
			"unique_external_id": " {{ticket.contact.unique_external_id}} "
		},
		"group": {
			"name": " {{ticket.group.name}} "
		}
	}
}
```
<!-- {% endraw %} -->
14. Click **Preview and save**.
15. Check that the summary looks like this:
    ![Summary](./images/summary.png)

16. Save and enable.  Your webhook step should now be fully usable.

> NB. If you accidentally delete the webhook step and need a new one, you can simply edit the rule and update the URL with that of the new step.

</section>
