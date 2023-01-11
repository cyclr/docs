
<section class="userguide" markdown="1">

## User Guide

<div class="section-content" markdown="1">

### Integrate FullContact address books with your apps

Automatically manage, update and enhance your contact's details with Cyclr's FullContact connectors. Make use of the FullContact to connector for data enrichment and the FullContact Contacts API connector for address book management.

### Organising Contacts

Share, sync and collaborate with your team using FullContact's latest contact management solution. Segment your contacts into dedicated groups for each of your organisation's teams and use Cyclr's FullContact Contacts connector to ensure they are kept up to date, within FullContact and your other external applications.

Example Uses:

- Allow your sales teams to manage their contacts in their preferred messaging service
- Automatically keep team address books up to date based on the projects they're working on
- Add additional data to contacts from teams main platforms (eg: Support teams getting data from helpdesk platform)

### Collect Contacts by Team

The Get Teams step, as part of the FullContact Contacts API connector, allows you to retrieve all teams within your account.

![Location of FullContact for Teams method](https://cyclr.com/wp-content/uploads/2017/11/FullContact-Teams-Method.png)

This allows you to connect to other FullContact connector steps in order to select team specific address books.

![Mapping the FullContact for Teams connector](https://cyclr.com/wp-content/uploads/2017/11/FullContact-teams.gif)

**Note**: Within the **Get Contacts** step it is possible to directly select a team while configuring the step. You must authenticate the connector to do this.

### Contact Data Enrichment

Cyclr's [FullContact connector](/integrate/fullcontact) allows you to easily enhance user and customer data as it is entering your business systems.

Example Uses:

- Adding more context to user details from website forms
- Providing more data in your marketing profiles to allow for more granular segmentation
- Updating user records with up to date data
- Adding business context to social media enquiries and contact

### FullContact Connector

The FullContact connector allows you to request additional data on a user based on:

- By email address
- By company URL domain
- By Twitter handle

![FullContact Enhance Connector Methods](https://cyclr.com/wp-content/uploads/2017/11/FullContact-Enhance-Connector.png)

### Field Mapping Example

In this example workflow, a Cycle is triggered when a Contact Form 7 form is submitted. Before the contact form data is sent to Salesforce it is sent to FullContact to discover more information on the user.

![Field mapping the FullContact connector](https://cyclr.com/wp-content/uploads/2017/11/FullContact-Enhance.gif)

You can then pass data values from the FullContact connector to your CRM, which is shown below being mapped in the Salesforce connector.

![Mapping data from FullContact connector](https://cyclr.com/wp-content/uploads/2017/11/FullContact-Enhance-mapping.gif)

</div>

</section>
