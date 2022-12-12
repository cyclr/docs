
<section class="setup partner" markdown="1">

*This guide applies to Salesforce, Salesforce Service Cloud, and other services that use Salesforce authentication.*

## Partner Setup

<div class="section-content" markdown="1">

Salesforce uses OAuth 2 for remote API access. You must register Cyclr within Salesforce as your own Connected App to receive OAuth Client ID and Client Secret values to enable Cyclr to authenticate with Salesforce.

The official Salesforce documentation for creating a **Connected App** can be found [here](https://help.salesforce.com/articleView?id=connected_app_create.htm).

### Register Your Application

You can register for a free [Salesforce Developer Edition account here (click **Sign Up** at the top of that page)](https://developer.salesforce.com/) or log into your existing Salesforce account if you have one. 

You can use any Salesforce account to create a Connected App, it doesn't have to be a Developer Edition account.
We advise against using a Sandbox account as Connected Apps are destroyed when they are refreshed.

#### Create your App within Salesforce

The process of creating an app in Salesforce varies slightly depending upon whether you are using **Salesforce Classic**, or **Lightning Experience**.

##### Salesforce Classic 
1. Log into your Salesforce account
2. Click **Setup** in the top right
3. From the menu on the left, select **Build > Create > Apps**
4. From the **Connected Apps** table click **New**

##### Lightning Experience
1. Log into your Salesforce account
2. Click **Setup** in the top right
3. From the menu on the left, select **Platform Tools  >  Apps  >  App Manager**
4. Click **New Connected App**

#### Basic Information

Whether you are using **Salesforce Classic** or **Lightning Experience**, when the **New Connected App** screen is shown, complete the form as follows:

**Connected App Name:** enter a name for your application

**API Name:** this will default to the same value as your Connected App Name

**Contact Email:** your email address

#### API (Enable OAuth Settings)

Tick the **Enable OAuth Settings** box to display further options.

**Callback URL**: you must add a callback URL to allow Salesforce to be used in your Cyclr Console and its accounts.

The URL is:

- ``https://[Your Cyclr service domain e.g. app-h.cyclr.com]/connector/callback``
- **Selected OAuth Scopes**: you must add the following 2 Scopes to enable Cyclr to use your App:
    - Full access (full)
    - or if you know which data you wish to restrict to you can select from this [list](https://help.salesforce.com/articleView?id=sf.remoteaccess_oauth_tokens_scopes.htm&type=5)
- Perform requests on your behalf at any time (refresh\_token, offline\_access)

The OAuth settings should look like this:

![Salesforce OAuth Partner Setup](./images/salesforce-partner-setup-oauth.png)

After saving your App, make a note of your **Consumer Key** and **Consumer Secret** values as you'll need to enter these into Cyclr.

**IMPORTANT** It can take up to 10 minutes for any changes to your Connected App to take effect in Salesforce.

![Salesforce Update Error](./images/salesforce_update_error.png)

If you attempt to use your app before it has had time to update, you may encounter this error.

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Setup your Salesforce App within Cyclr:

- go to your **Cyclr Console**
- click the **Connectors** menu along the top
- choose **Connector Library**
- scroll down to **Salesforce**
- click the **Setup** button

Enter the following values:

**Client ID**: the ``Consumer Key`` of your Salesforce Connected App

**Client Secret**: the ``Consumer Secret`` of your Salesforce Connected App

Your Salesforce Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

## Enduser Salesforce Account Setup

For the best experience when using the Salesforce Connector, and to reduce the frequency at which Cyclr must obtain a new Access Token and avoid some connection issues, ensure the following Session Settings have been set:

Log in to the Salesforce organization, go to Setup, then use the Search to find **Session Settings**.

Under **Session Timeout**
- Timeout Value: set this for as long as possible, e.g. 24 hours.
- Force logout on session timeout: disable this.

Under **Session Settings**
- Lock sessions to the IP address from which they originated: disable this.

</div>

</section>

<section class="faq" markdown="1">

## FAQ

<div class="section-content" markdown="1">

### Expired access/refresh token errors

Salesforce only allows up to five unique access/refresh token pairs to be issued for each user in a Connected App. Older tokens will be automatically revoked by Salesforce. 

[More information](https://help.salesforce.com/articleView?id=remoteaccess_request_manage.htm).

### Disabling Assignment Rules

When creating Accounts, Cases, or Leads in Salesforce, it may be desirable to prevent Salesforce's **active assignment rules** from being applied.  This very much depends on what assignment rules have been setup within Salesforce so will depend on the enduser's requirements.

To prevent assignment rules from being applied, add this Script to a Salesforce step in the Cycle Builder:

```javascript
function before_action() {
    // Don't apply Salesforce's assignment rules.
    method_request_headers['Sforce-Auto-Assign'] = 'FALSE';

    return true;
}
```
[More information](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/headers_autoassign.htm)

### Working with CSV documents

To retrieve the contents of a CSV document, you will need to take the following steps:

1. Find the Document ID.  This can be found in the response you recieved when you made the file, or by running ``List Content Documents``.
2. Use this ID in a ``Get Content Version`` call to get the Content Version ID.
3. Enter the Content Version ID in a ``Get Content Document Data (CSV)`` call.
4. You will need to add the fields within connector settings so that you can map them.  The field location will be ``[].yourcolumname`` .

</div>

</section>

