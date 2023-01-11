
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Create a new application in GoCardless to get a `Client ID` and a `Client Secret`.  

### Service Domain 

The oAuth App creation requies  your Cyclr Partner **Service Domain** . Get this information before you create the GoCardless app.

This is specific to your instance of Cyclr.

- Login to your Cyclr Partner Console
- Go to  **Settings > General Settings > Service Domain**

Your Cyclr Partner may have been setup with a default Service Domain, but this can be changed if you would prefer to remove mentions of 'cyclr' from it.  Contact Support for more information.

### Creating a oAuth App

See [GoCardless Creating an app](https://developer.gocardless.com/getting-started/partners/connecting-your-users-accounts/#creating-an-app) for more information.

When asked for a Redirect URI, enter `https://[Your Cyclr Service Domain]/connector/callback`.

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

- Go to your Cyclr Console
- Click the **Connectors** option 
- Click **Application Connector Library**
- Find **GoCardless**
- Click the *Padlock* icon
- Enter 

You should now be able to successfully install a **GoCardless** Connector.

Install a Connector and run a test against one of the Methods, to make sure the authentication process has been completed successfully.

</div>

</section>
