
### Partner Setup

To set up the GoCardless connector for your users, you will need a Client ID and a Client Secret.  You get these by creating a new application in GoCardless.  

### Preparation 

When creating your oAuth App, you will need to provide your Cyclr Partner **Service Domain** so it's best to have that information to hand before you begin.

This is specific to your instance of Cyclr and can be found in your Cyclr Partner Console under **Settings > General Settings > Service Domain**.

Your Cyclr Partner may have been setup with a default Service Domain, but this can be changed if you would prefer to remove mentions of 'cyclr' from it.  Contact Support for more.

### Creating a oAuth App

There are instructions on how to do that here ([https://developer.gocardless.com/getting-started/partners/connecting-your-users-accounts/#creating-an-app](https://developer.gocardless.com/getting-started/partners/connecting-your-users-accounts/#creating-an-app)).

When asked for a Redirect URI, enter the following: `https://[Your Cyclr Service Domain]/connector/callback`

### Cyclr Setup

From your Cyclr Console, click the **Connectors** option along the top then **Application Connector Library**, find **GoCardless** - you may need to use the Search box to locate it - then click the Padlock button and paste and save your values there.

You should now be able to successfully install a **GoCardless** Connector.

At this point it would be a good idea to install a Connector and run a test against one of the Methods, just to make sure the authentication process has been completed successfully.
