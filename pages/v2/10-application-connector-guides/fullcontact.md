---
title: FullContact Connector Guide
sidebar: cyclr_sidebar
permalink: fullcontact-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
# FullContact

-------------

<h2>Integrate FullContact address books with your apps</h2>
<p></p>
<p>Automatically manage, update and enhance your contact’s details with Cyclr’s FullContact connectors. Make use of the
    FullContact to connector for data enrichment and the FullContact Contacts API connector for address book
    management.</p>


<h2>Organising Contacts</h2>
<p>Share, sync and collaborate with your team using FullContact’s latest contact management solution. Segment your
    contacts into dedicated groups for each of your organisation’s teams and use Cyclr’s FullContact Contacts connector
    to ensure they are kept up to date, within FullContact and your other external applications.</p>
<p>Example Uses:</p>
<ul>
    <li>Allow your sales teams to manage their contacts in their preferred messaging service</li>
    <li>Automatically keep team address books up to date based on the projects they’re working on</li>
    <li>Add additional data to contacts from teams main platforms (eg: Support teams getting data from helpdesk
        platform)</li>
</ul>
<h3>Collect Contacts by Team</h3>
<p>The Get Teams step, as part of the FullContact Contacts API connector, allows you to retrieve all teams within your
    account.</p>
<p><img class="size-full wp-image-1203 aligncenter" src="https://cyclr.com/wp-content/uploads/2017/11/FullContact-Teams-Method.png"
        alt="Location of FullContact for Teams method" width="267" height="278"></p>
<p>This allows you to connect to other FullContact connector steps in order to select team specific address books.</p>
<p><img class="aligncenter wp-image-1204 size-full" src="https://cyclr.com/wp-content/uploads/2017/11/FullContact-teams.gif"
        alt="Mapping the FullContact for Teams connector" width="700" height="336"></p>
<p><strong>Note</strong>: Within the <strong>Get Contacts</strong> step it is possible to directly select a team while
    configuring the step – just ensure you have authenticated the connector.</p>


<h2>Contact Data Enrichment</h2>
<p>Cyclr’s <a href="/integrate/fullcontact">FullContact connector</a> allows you to easily enhance user and customer
    data as it is entering your business systems.</p>
<p>Example Uses:</p>
<ul>
    <li>Adding more context to user details from website forms</li>
    <li>Providing more data in your marketing profiles to allow for more granular segmentation</li>
    <li>Updating user records with up to date data</li>
    <li>Adding business context to social media enquiries and contact</li>
</ul>
<h3>FullContact Connector</h3>
<p>The FullContact connector allows you to request additional data on a user based on:</p>
<ul>
    <li>By email address</li>
    <li>By company URL domain</li>
    <li>By Twitter handle</li>
</ul>
<p><img class="size-full wp-image-1200 aligncenter" src="https://cyclr.com/wp-content/uploads/2017/11/FullContact-Enhance-Connector.png"
        alt="FullContact Enhance Connector Methods" width="277" height="210"></p>
<p>&nbsp;</p>
<h3>Field Mapping Example</h3>
<p>In this example workflow, a Cycle is triggered when a Contact Form 7 form is submitted. Before the contact form data
    is sent to Salesforce it is sent to FullContact to discover more information on the user.</p>
<p><img class="aligncenter wp-image-1201 size-full" src="https://cyclr.com/wp-content/uploads/2017/11/FullContact-Enhance.gif"
        alt="Field mapping the FullContact connector" width="700" height="336"></p>
<p>You can then pass data values from the FullContact connector to your CRM, which is shown below being mapped in the
    Salesforce connector.</p>
<p><img class="aligncenter wp-image-1202 size-full" src="https://cyclr.com/wp-content/uploads/2017/11/FullContact-Enhance-mapping.gif"
        alt="Mapping data from FullContact connector" width="700" height="336"></p>

</section>
