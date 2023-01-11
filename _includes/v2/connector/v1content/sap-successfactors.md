

<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

**The SAP SuccessFactors connector is currently a beta connector.**

To authenticate the SAP SuccessFactors connector you will need the following:

- `Client ID`
- `Private Key`: This is used within the SAML assertion stage of the SAP Authentication (found within your Certificate.pem file)
- Your Domain: You can also select from a dropdown of predefined production servers
- Your User ID
- Company ID: Your SuccessFactors Instance

### Setting up an application in SAP SuccessFactors

1. Go to the **Admin Center** page in your SAP SuccessFactors account
2. Click **Manage OAuth2 Client Applications**
3. Click **Register**
3. Generate a X509 Certificate using your Application name and URL. 
4. Download the .pem file: This contains your `Private Key` and `Certificate` which can be viewed in a text editor like Notepad++
5. Save the configuration

You should be able to now access your `API Key` which will be used as your Client ID in Cyclr.

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">


Setup your SAP SuccessFactors within Cyclr:

- Go to your **Cyclr Console**
- Click the **Connectors** menu along the top
- Choose **Connector Library**
- Find the **SAP SuccessFactors** connector.
- Click the **Setup** button

Enter the required values, as found above in previous section.

Your SAP SuccessFactors Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</div>

</section>
