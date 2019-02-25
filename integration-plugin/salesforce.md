---
title: Saleforce Plugin
---

![Salesforce Integration Plugin](https://cyclr.com/wp-content/uploads/2017/10/Salesforce.png)

The Cyclr Salesforce plugin allows you to synchronise contacts and campaigns with a number of email marketing platforms, including [Sentori](http://sentoriapp.com/), [Campaign Monitor](http://campaignmonitor.com/), and [MailChimp](http://mailchimp.com/).

It does not require a Salesforce account with API access available.

You can find the Cyclr plugin on the [Salesforce AppExchange](https://appexchange.salesforce.com/listingDetail?listingId=a0N30000000q4YdEAI).

#### Prerequisites

*   Salesforce User with suitable admin permissions for installing plugins and managing pages/fields.
*   An account for either CampaignMonitor, MailChimp, or Sentori
*   API key (CampaignMonitor and Sentori only)
*   Cyclr account

Features list
-------------

#### Synchronise Campaigns

*   Create draft emails
*   Synchronise contacts to lists

#### Synchronise Reports

You can send reporting data from your email marketing platform back to Salesforce. The data available depends on which email platform you use, but can include:

*   Recipients
*   Total Opened
*   Clicks
*   Unsubscribed
*   Bounced
*   Unique Opened
*   Spam Complaints
*   Forwards
*   Likes
*   Mentions

#### Install Connectors

If you haven’t already done so, install the connector for your email marketing platform.

1.  In Cyclr’s builder, click the Add Connector button in the right sidebar.
2.  Click to install the connector for the Salesforce Plugin; this will take you to your Salesforce account and (when logged in) request the permissions necessary for Cyclr to connect to your account.

#### Install the Cyclr Salesforce Plugin

[Install Cyclr Salesforce Plugin](https://appexchange.salesforce.com/listingDetail?listingId=a0N30000000q4YdEAI)

_Note: to install the plugin, and make the necessary changes to pages and fields, your Salesforce user must be an admin or have appropriate permissions._

#### Customise Campaigns in Salesforce

The default Campaign object in Salesforce needs some additional fields to store your email marketing report data. In addition, there’s two buttons that need to be added to the Campaign pages.

_Note: ensure your Salesforce is an admin, or has the necessary permissions, to make the below customisations._

#### Customise Campaign Page

*   Go to Go to Setup > Build > Customize / or under Settings use search for “campaigns”.
*   From here, click on Page Layouts > Edit.
*   The screen should now show a selection of buttons.
*   Click and drag the Connect Campaign and Setup Cyclr buttons to the custom buttons region (in page preview below the buttons).

#### Customise Campaign Page

On the same screen used above to add buttons to the Campaign Page, you can also drag on the necessary fields. These fields were created for you when the Cyclr Salesforce Plugin was installed.

Click and drag on the following fields:

*   Recipients
*   TotalOpened
*   Clicks
*   Unsubscribed
*   Bounced
*   UniqueOpened
*   SpamComplaints
*   Forwards
*   Likes
*   Mentions

How it Works
------------

The Cyclr Salesforce Plugin takes a “Salesforce first and last” approach, with all marketing activitiy starting and ending in Salesforce. The email marketing campaigns the plugin creates and interacts with are handled by services like MailChimp, Campaign Monitor, Sentori, etc.

Example process:

*   Create a new Campaign in Salesforce
*   Attach contacts
*   The plugin pushes the campaign and its contacts to your email marketing platform
*   A draft campaign is created and the contacts are attached
*   After sending, Cyclr will pull back reporting data to Salesforce

#### Creating a Campaign

First a Campaign needs to be created in Salesforce. This Campaign is made of a name and members (the contacts). It acts as a the mechanism to sync data from Salesforce to your email platform and as the container to bring back and store reporting data.

Setup process:

*   Log into Salesforce.
*   Under Campaigns, click Create New > Campaign.
*   Setup your Campaign: Name (used for the draft email name) and Type (set to Email) are required, other fields are optional.
*   Save your Campaign and you will now be shown the Campaign Detail screen.
*   Scroll to the bottom section of the screen to Campaign Members, click the dropdown to add Members.
*   Choose Leads or Contacts and use the standard Salesforce tools to search and filter to find the Members you wish to market to.
*   To add Campaign Members to your Campaign, select them and click the Add With Status button (using Sent).

#### Connect Campaign

Once your Campaign is setup and has Members, you should click the **Connect Campaign** button on the **Campaign Detail** page. On the connect screen, most of the settings will be correct and will not need adjusting.

Click the **Sync Campaign** button, which will:

*   Create a new draft email campaign in your connected email marketing platform
*   Import and attached the selected Campaign Members
*   Create the link to pull back report data

_Note: in order to connect your Campaign, you must first have clicked the Setup Cyclr button to connect the Cyclr Salesforce Plugin with your Cyclr account._

#### Common Problems

“Cannot find any Cyclr account with admin access” – Please ensure your account has the correct admin privileges. Ensure you are also logged into the same Salesforce account that your Cyclr is authenticated with.