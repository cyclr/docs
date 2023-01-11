
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Candidate Hub uses OAuth 2.0 for remote API access. 

See the [Mautic API documentation](https://developer.mautic.org/#rest-api) for details.

### Before Starting

Enable API access in your instance of Candidate Hub: 

- Go to **Settings** > **Configuration**
- Select **API Settings**
- Select ``yes`` under **API enabled?**

### Adding a New Application

After you've allowed API access, you will need to follow these steps to be able to use the API with cyclr.

Step 1 - Under settings, you will find a new tab called API Credentials. 

![API Credentials](./images/CandidateHub1.png)

Step 2 - Once inside, select New in the top right corner

Step 3 - In this new screen, set Authorization Protocol to OAuth2, give it an appropriate name, and make the redirect URI your instance of Cyclr.

![New Project Details](./images/CandidateHub2.png)

Step 3a - The Redirect URL should be https://<span></span>{service domain}/connector/callback. Your service domain can be found in your Cyclr console under `Settings > General Settings > Service Domain`.

Step 4 - You'll be taken back to the API Credentials page and be provided with both a Public Key and a Secret Key.

</div>

</section>

<section class="setup partner" markdown="1">

<div class="section-content" markdown="1">

The Connector now can be installed using the credentials obtained in the above steps:

**Client ID**: `Public key`

**Secret**: `Secret Key`

You will also need to add the subdomain of your application to the connector when initialising it. If your URL is 'app.candidatehub.io' you would fill the field with 'app'.

You will then be prompted to log in, select your CandidateHub account information and authorize access to the connector.

</div>

</section>
