
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

See [Clover](https://cyclr.com/integrate/clover) for details of Clover intregration.

Go to [clover.com/developers](https://www.clover.com/developers/) and create a new application.  

- Get your Cyclr Service Domain from Cyclr Console > Settings > General Settings
- In your new Clover application, go to *Settings* 
- Update the Web Configuration setting `Site URL` to your Cyclr Service Domain. 
- Update the permissions setting checking everything other than *Process Credit Cards*
- The App ID is the `Client ID` and the App Secret is the `Client Secret`.  Not these for the Cyclr setup.

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

### No webhooks

If you don't need to use webhooks:

- login to your Cyclr Console
- in the top menu go to *Connectors > Connector Library*
- find the Clover connector in the list and click its *Setup* button.
- Set the `Client ID` as the App ID
- Set the `Client Secret` as the App Secret

#### Install/Authenticate a connector

- Enter the domain for Clover, either US or Europe
- Click the sign in button
- If required in the popup, install the application, then close the popup and the sign in button again.

### Webhooks

Clover only supports sending webhooks to one webhook step per Clover application. 

To use webhooks with Cyclr, create a separate Application in [clover.com/developers](https://www.clover.com/developers/) for each connector install.

#### Setup Webhook

1.  Add the Clover Event Webhook step to the cycle
2.  Run the cycle
3.  Copy the URL from the webhook step and paste it into the Clover setting for clover webhook
4.  Clover will now send a verification message to the webhook cycle, open the step data for the webhook and copy the verification code
5.  Paste the verification code into the Clover application to authenticate the URL.

![Clover Webhooks](./images/clover-webhooks-1.png)

Enable the subscriptions that you wish to receive events for.

**Each subscription requires the corresponding read permission. If you change permissions after a merchant installs your app, the permissions won't update for that merchant until the merchant uninstalls and reinstalls the app.**

</div>

</section>
