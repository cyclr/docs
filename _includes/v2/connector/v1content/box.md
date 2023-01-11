
<section class="authentication" markdown="1">

## Authentication

| Type      | OAuth2 |
| Description |  |
| OAuth 2 Type | AuthorisationCode |
| Authorise URL | https://account.box.com/api/oauth2/authorize |
| Access Token URL | https://api.box.com/oauth2/token |
{: .table .vheader}

<div class="section-content" markdown="1">
</div>

</section>

<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">


- If you have a Box account already, [sign in](https://account.box.com/login). Otherwise [create a new account](https://www.box.com/pricing).
- Once signed in, go to 'Dev console' from the left hand menu. That will take you through to your apps. You can either select a pre-existing app or create a new one.

![connector setup](./images/box_setup_8.png)
![connector setup](./images/box_setup_1.png)

- Once you have selected the app you would like to authenticate, on the following page click 'Configuration' from the left hand menu.

![connector setup](./images/box_setup_5.png)

- In the configuration page make sure that 'Authentication method' is set to 'Standard OAuth 2.0 (User Authentication)'.

![connector setup](./images/box_setup_2.png)

- Scroll down to find your **Client ID** and **Client Secret**. For Redirect URI enter: https://{{ServiceDomain}}/connector/callback (ServiceDomain should be substituted for your actual service domain)

> Your Cyclr service domain, e.g. yourcompany.cyclr.com can be found in your Cyclr Console under Settings > General Settings > Service Domain.

![connector setup](./images/box_setup_4.png)

</div>

</section>

<section class="setup partner" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">


- Locate the Box connector in the Cyclr console.

> (https://{{ServiceDomain}}/console) > Connectors > Connector Library > Box

- Click the open padlock and on the next page enter your Client ID and Client Secret.

![connector setup](./images/box_setup_7.png)

- Upon installation of the connector in your account, you will be redirected to Box and prompted to 'Grant access to Box'. Once completed, you will be redirected back to Cyclr where the connector is authenticated and ready to use.

![connector setup](./images/box_setup_9.png)

</div>

</section>
