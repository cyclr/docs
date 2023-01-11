
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Login to your existing Notion account.

Cyclr requires Pipedrive to use OAuth 2.0 authentication for remote API access. You must register Cyclr within Pipedrive as its own App to receive a `Client ID` and `Client Secret`. This enables Cyclr to authenticate and connect with Pipedrive.

**NB**: Due to Pipedrive authentication, customers need to follow the below Pipedrive setup process.

## Pipedrive Setup

To obtain `Client ID` and `Client Secret`  from  Pipedrive:

### Enable a Developer Sandbox Account

To create a Developer Sandbox Account, Pipedrive requires you to complete the following [form](https://developers.pipedrive.com/start-here). This allows you to access the **Marketplace Manager**. Without this, you will be unable to create the Pipedrive App required for authentication with Cyclr. The official Pipedrive documentation on this process can be found [here](https://pipedrive.readme.io/docs/developer-sandbox-account).

### Create an app within the Marketplace Manager

Create a new App and obtain the `Client ID` and `Client Secret` using the steps below. 

See the official Pipedrive documentation for [creating an App](https://pipedrive.readme.io/docs/marketplace-creating-a-proper-app).

See the Pipedrive [app types documentation](https://pipedrive.readme.io/docs/marketplace-creating-a-proper-app#types-of-apps).

See the Pipedrive [access scopes documentation](https://pipedrive.readme.io/docs/marketplace-scopes-and-permissions-explanations).

1. Go to the **Marketplace Manager** found [here](https://cyclrdevs.pipedrive.com/settings/marketplace_manager):  this is accessible only if you have a Developer Sandbox Account
2. Click **Create New App**
3. Select **No** to set the App to unlisted and internal/private
4. Click **Next** 
5. Complete the App form as required by Pipedrive
6. Go to the **OAuth & Access scopes** heading to provide Cyclr authentication
7. Enter the callback URL in the **Callback URL** field. The callback URL has the following format:
   `https://{your Cyclr service domain}/connector/callback`
8. Enable the required **Access scopes** as either **Read only** or **Full access**
7. Click **Save** to create the App. This will take you back to the Marketplace Manager
8. Click the newly created App within the **Marketplace Manager** to see the settings again
9. Under the **OAuth & Access scopes** find the `Client ID` and note the value to use in the Cyclr setup
10. Click **Show** to reveal the `Client Secret` and note the value 

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

To set up the Pipedrive Connector within Cyclr:

1. Go to the **Cyclr Console**
2. Click the **Connectors** dropdown menu at the top of the page
3. Click **Application Connector Library**
4. Use the search bar to find the **Pipedrive (OAuth2.0)** App
5. Click the **Setup Required** button
6. Enter the **Client ID** and **Client Secret** found in the previous section 
7. Click **Next**
7. Click **Sign In** to sign in to Pipedrive to allow Cyclr to connect to it
8. Click **Allow and Install** to authorize the Pipedrive App to use the listed permissions and install it to your account

Your Pipedrive Connector is now set up! You can test it by installing it to one of your Cyclr accounts and using one of the methods to confirm it returns data.

</div>

</section>

<section class="userguide" markdown="1">

## Pipedrive Integration Workflow Building Examples

<div class="section-content" markdown="1">

### Automating Pipedrive 

#### Automating Deals

Our Pipedrive connector includes a number of webhooks. These are real-time event notifications that fire when something happens to a deal, e.g. when one is created or updated.

Example uses:

- Sync new deals with another system
- Trigger time-based actions for deals stuck at a certain stage
- At key deal stages, add the associated contacts to a marketing system
- Automate internal Pipedrive deals, e.g. when a deal hits a certain stage move it to a different pipeline

##### Deal stage lookups

One of the keys to using Pipedrive's deals is working with the Stage ID in a Cyclr Decision step. In doing this, you can trigger the next appropriate action, either in Pipedrive or in another app.

![Deal stage lookups screen grab](https://downloads.intercomcdn.com/i/o/29084048/e84a2753288301ecbc2bb070/pipedrive-deal-lookup.gif)

#### Forms

With Cyclr, you can integrate Pipedrive with a number of form building apps including:

- Contact Form 7
- Gravity Forms
- Typeform
- SurveyMonkey

#### Automate Your Sales Pipeline

Cyclr lets you automate your sales process by using webhooks and triggers based on movements between pipeline stages.

Example uses:

- Send deals to separate pipelines for other teams to complete work on
- Automatically assign reminders for yourself or team members based on deal stages
- Trigger external application events when a deal reaches a chosen stage
- Automatically send emails and messages when a deal hits a particular stage

### Automation Implementation

Follow our below video guide to get you started with Pipedrive Automation.

<iframe width="500" height="281" src="https://www.youtube.com/embed/GTBgHGIh_Mo?feature=oembed" frameborder="0" gesture="media" allowfullscreen=""></iframe>

#### Pipedrive Updates with Webhooks

Cyclr combined with Pipedrive's webhook builder allows you to trigger automation workflows based on a wide range of actions in your CRM.

Our Webhook connect includes an automatic field discovery feature, helping you set up your automation workflows in no time.

Watch the video below to see how you can make use of Pipedrive's webhooks.

<iframe width="500" height="281" src="https://www.youtube.com/embed/WclcTlrAsi0?feature=oembed" frameborder="0" gesture="media" allowfullscreen=""></iframe>

### Pipedrive and Contact Form 7 Integration

Getting Contact Form 7 to work with your Pipedrive CRM has been a pain for a long time, so you'll be please to see that you can connect the two with Cyclr.

#### Why Integrate Contact Form 7 and Pipedrive?

Contact Form 7 is still one of the most popular form building applications around. While it's name suggest it is just for contact forms, it has many usages when combined with Pipedrive, including:

- Adding new website enquiries directly into your CRM
- Creating new deals direct from forms
- Managing helpdesk enquiries
- Passing user registration data across your company's application stack

Take a look at our video tutorial to find out how to get it set up.

<iframe width="500" height="281" src="https://www.youtube.com/embed/G8gVVAeNB8Q?feature=oembed" frameborder="0" gesture="media" allowfullscreen=""></iframe>

### Automatically Add New Users to your CRM

Cyclr lets you integrate Pipedrive with Intercom, so you can add and update user data within your CRM automatically.

Cyclr's Intercom connector contains a range of webhooks that can be triggered when an event criteria in Intercom is met. Take a look at the video guide below to see how you can set it up.

<iframe width="500" height="281" src="https://www.youtube.com/embed/nvwAfTPC6Ak?feature=oembed" frameborder="0" gesture="media" allowfullscreen=""></iframe>

</div>

</section>
