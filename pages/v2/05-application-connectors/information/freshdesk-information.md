---
title: Freshdesk information
sidebar: cyclr_sidebar
permalink: freshdesk-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Webhooks

If you want to set up a **Ticket Closed** webhook step, you heed need to add it to your cycle, and then open the Freshdesk dashboard:


1. Select the **Admin** cog on the left hand side navigation bar.
    
    ![Admin cog](./images/cog.png)
2. Scroll down to the **Helpdesk Productivity** Section, and select **Automations**.

    ![Automations](./images/automations.png)
3. Choose **Rules that run on: Ticket Updates** and select **New rule**.
4. Set **Rule name** and **Involves any of these events** as follows:

    ![Rule settings](./images/rule_settings.png)
5. Set Request Type to **POST**.
6. For the **URL**, you need to go back to your Cyclr workflow, and copy the address from the **settings** in the webhook step.
7. Leave the other fields as they are, and under Content, select **Advanced**.
	* The section should now look like this:

    ![Rule settings 2](./images/rule_settings2.png)
8. In the **Write custom API request** text box, paste the following template:
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
9. Select **Preview and save**.

To make sure you set the webhook up correctly, check that the summary looks like this:
    ![Summary](./images/summary.png)

To use your webhook, save and enable it.

> **Note**: If you accidentally delete the webhook step and need a new one, you can simply edit the rule and update the URL with that of the new step.

</section>
