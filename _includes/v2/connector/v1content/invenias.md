
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

- Go to your Invenias Swagger definition at `https://**{{SubDomain}}**.invenias.com/api/swagger/index`
- Change the **{{SubDomain}}** to your Invenias subdomain
- This is the first part of your portal URL, for example if you login to Invenias via `https://**company**.invenias.com` , your subdomain is `**company**`

### Client ID and Secret

- After reaching your Invenias Swagger page, double click the **API Key** text box at the top of the page

![](./images/invenias-api-key.png)
- You may be prompted to login. After logging in, an `API Key` will appear in the text box
- Navigate to **ThirdPartyApplications**, and click on the first option
- Enter the following into the **Request** text box:
```
{
  "Expiration": "FiveYears",
  "Name": "Integration",
  "ReplyUrl": "https://{service domain}/connector/callback",
  "FlowType": "ResourceOwner"
}
```
- Change the values to your liking; **Name** can be customized, and set the **ReplyUrl** to your redirect URL. This can be found in your Cyclr console under `Settings > General Settings > Service Domain`. An example:

![](./images/invenias-example-request.png)
- Click the **Try it out** button. Below the button you will find a **Response Body**. Note down the **ClientId** and **ClientSecret** values from the script

![](./images/invenias-response.png)

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Setup your Invenias App within Cyclr:

- Go to your **Cyclr Console**
- Click the **Connectors** menu along the top
- Choose Connector Library
- Scroll down to **Invenias**
- Click the **Setup** button

Enter the following values:

- **Client ID**: The `Client ID` retrieved from the previous steps
- **Client Secret**:  The `Secret` retrieved from the previous steps
- **Username**: The username used to login to your Invenias portal
- **Password** The password used to login to your Invenias portal
- **Subdomain**: The subdomain used for the previous steps


Your Invenias Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.


</div>

</section>