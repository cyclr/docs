
<section class="authentication" markdown="1">

## Authentication

| Type      | OAuth2 |
| Description |  |
| OAuth 2 Type | AuthorisationCode |
| API Key Header | Authorization |
| Authorise URL | https://apirest.3dcart.com/oauth/authorize?store_url={{StoreURL}}|exclude:scope,display,immediate |
| Access Token URL | https://apirest.3dcart.com/oauth/token |
{: .table .vheader}

</section>

<section class="servers" markdown="1">

## Servers
| Server | URL | IP Address |
| --- | --- | --- 
| US (North Virginia) | my.cyclr.com | 52.22.119.215 |
| UK (London) | my.cyclr.uk | 52.56.244.97 |
| EU (Frankfurt) | eu.cyclr.com | 18.185.231.228 |

</section>

<section class="setup partner" markdown="1">

## Partner Setup

Login to your existing 3DCart Developer account or [sign up for one.](https://devportal.3dcart.com/login.asp)

Login to your existing 3DCart Secure Store account or [sign up for a free trial.](https://www.shift4shop.com/login-page.html)


<div class="section-content required" markdown="1">
### Retrieving OAuth2 Details

- [Login](https://devportal.3dcart.com/login.asp) to your 3DCart Developer Account.
- Click Add New.
- Enter a name and click next. 
- On your Developer Portal Dashboard, enter the callback URL (https://[Your Cyclr Service Domain]/connector/callback) for your app. 
- Enter the IP Address for the [relevant server](##Servers) in the IP White List.
- Set the scopes for your Application (Permissions on the right of the dashboard), **Contacts** & **Orders** are required.
- To use the  **List Order Status** method, select the scope **OrderStatus**.
- Click Save.
- Note the **Public Key**, **Client ID** and the **Secret Key** from this page.
- Test the application at this stage  to ensure that it works with your 3DCart Store.
</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

Setup your 3DCart within Cyclr:

- Go to your **Cyclr Console**
- Click the **Connectors** menu along the top
- Choose Connector Library
- Scroll down to **3DCart**
- Click the **Setup** button

Enter the following values:

**Client ID**:  The Client ID that we retrieved from the app that we made.

**Client Secret**:  The Secret Key we retrieved from the app that we made.

- Login to your Secure Store

Your 3DCart Connector is now setup! 

### Testing

Install the connector in one of your Cyclr accounts and execute one or more methofd to confirm that data is returned.

</section>
