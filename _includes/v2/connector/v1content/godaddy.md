
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

### API Key and Secret
- Login to your GoDaddy Developer Portal
- Click the *API Keys* tab
- Click *Create New API Key*, if no existing key is displayed

The first API Key created is be a test key. Use this for your development against our OTE environment  hosted at https://api.ote-godaddy.com. 

Integrate first with the OTE environment to verify that your API calls are correct. before you go live with calls to the Production environment.

When you are ready for production, create a new `API Key` and `Secret` to call our production environment hosted at https://api.godaddy.com.

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Setup your Go Daddy connector within Cyclr:

- Go to your *Cyclr Console*
- Click the *Connectors*  menu option
- Choose *Connector Library*
- Find *GoDaddy*
- Click the *Setup* button

Enter the following values:

*Server Name*: One of OTE server: https://api.ote-godaddy.com, or production: https://api.godaddy.com

*API Key*: Noted from the Partner Setup


Your GoDaddy Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</div>

</section>
