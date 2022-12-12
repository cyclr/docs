
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

### API Key Setup ###

- Login to DevicePilot 
- Go to the token settings
- Create a new token - Select *POST* as the token type and enter an appropriate name
- Click *Show token* to view the token and note the value. It should start with *TOKEN*

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

In the connector setup enter the full `API Key` in the API Key textbox.

### Updating and Inserting Device Data

User can submit any data that is relevant to their devices. 

To support this, Cyclr provides `custom fields` in the connector setup. Add the fields here to be submittde to DevicePilot.

</div>

</section>

<section class="userguide" markdown="1">

## Webhooks

<div class="section-content" markdown="1">

Webhooks are managed by DevicePilot, so will need to be setup through the admin portal. To do this:

1. Add the webhook method that is present in the connector. Enter *Step setup* and note the webhook URL. It should look similar to *https://my.cyclr.com/api/webhook/ABC123* depending on your region.
2. Navigate to the [connections](https://app.devicepilot.com/#/connect/manage) area  in DevicePilot.
3. Create a new webhook by clicking *Get Started* underneath the *Webhooks* category.
4. Enter in the appropriate details.
    1. Set URL to the Cyclr webhook URL (see step 1).
    2. Set Method to *POST*.
    3. Headers should contain *Authorization* which is set to the `API key` entered in during connector setup, and *content-type* is set to *application/json*.
    4. Body represents the response and data.
5. The webhook setup should look similar to the following:
\
![Example webhook setup](./images/devicepilot-webhook.png)
6. Save the changes.

See the [DevicePilot help page](https://help.devicepilot.com/webhook) for more details.

</div>

</section>
