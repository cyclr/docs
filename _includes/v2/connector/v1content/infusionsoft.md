
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

The Infusionsoft Connector authentication requires:
- `Client ID`
- `Client Secret`
- `Username`
- `Password`

### Client ID And Client Secret

Get the `Client ID` and `Client Secret` from your Keap developer account. Keap is the parent company of Infusionsoft.

You need a developer account and a registered App. When authenticating the Connector we link this App to the desired Infusionsoft account using these credentials.

1. Log in to your [existing account](https://keys.developer.keap.com/accounts/login) or [create an account](https://keys.developer.keap.com/accounts/create)

2. From the far right of the top navigation bar, click your username/email and then click **Apps**

   ![keap portal](./images/infusionsoft_1.png)

3. Click **+ NEW APP**

   ![keap portal](./images/infusionsoft_2.png)

4. Enter a name for the App and a description (optional)

5. Clicking the toggle switch to activate API access for this App as pictured below

   ![keap portal](./images/infusionsoft_3.png)

6. Click **CREATE**

7. Your `Client ID` (Key) and `Client Secret `(Secret) are displayed under **API Keys**

   ![keap portal](./images/infusionsoft_4.png)

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

1. Find the Infusionsoft Connector

   > Cyclr Console > Connectors > Connector Library > Infusionsoft

2. From the Edit Connector interface click **Setup**

3. Enter your `Client ID` and `Client Secret`

4. Click **Next**

5. On the next page click **Sign In**

6. You are redirected to the Infusionsoft interface

7. When prompted log in to the Infusionsoft account to which you want to link the Connector/App

   > Note: The login credentials required here are **not the credentials for your developer account**. We are linking the App from your developer account to the desired Infusionsoft account.

8.If prompted,  select the Infusionsoft account you are linking the Connector/App to

   ![keap portal](./images/infusionsoft_6.png)

9. Allow the App access

   ![keap portal](./images/infusionsoft_7.png)

10. You are redirected to the Cyclr interface where the Connector is now authenticated and ready to use

</div>

</section>

<section class="userguide" markdown="1">

## User Guide

<div class="section-content" markdown="1">

The Create and Update Contacts functionality is handled with a single method **Upsert Contacts**. 

This performs a duplicate check within Infusionsoft for the entered email address. 

If a matching email address is found, the existing contact is updated. 

If no match is found, a new contact is created.

When entering a State or Country code we advise that you use our Lookup feature, as the Infusionsoft API has strict requirements for valid Province and Country codes.

![keap portal](./images/infusionsoft_8.png)

![keap portal](./images/infusionsoft_9.png)

</div>

</section>
