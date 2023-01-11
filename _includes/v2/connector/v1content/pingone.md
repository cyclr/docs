
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

PingOne uses OAuth 2 Client Credentials for remote API access. 

You must register a worker application within PingOne to receive `OAuth Client ID` and `Client Secret` values to enable Cyclr to authenticate with PingOne.

See the [PingOne application documentation](https://apidocs.pingidentity.com/pingone/platform/v1/api/#getting-started) for more information.

### Register Your Application

Login to your PingOne admin portal to configure your oAuth application. 

To create the application connection:
1. Select the environment that you wish to connect to
2. Click **Connections**
2. Click **+ Add Application**
3. Select the `Worker` application type
4. Click **Configure**
5. Create the application profile:
    - Enter the Application name - a unique identifier
    - Click **Save** and **Close**
6. Expand the application just created
7. Click on the **edit** icon
8. Select **Configuration** tab 
9. Set **Grant Type** to `Client Credentials`
10. Set TOKEN ENDPOINT AUTHENTICATION METHOD to `Client Secret Post`
11. Save the following information:
    - `Client ID`
    - `Client Secret`
    - `Auth Domain` e.g. with **AUTHORIZATION URL** https://auth.pingone.eu/cd91070f-c371-480e-80b2-753c735f8aa1/as/authorize the value is `auth.pingone.eu`
    - `Environment ID`   with the above **AUTHORIZATION URL** the value is  `cd91070f-c371-480e-80b2-753c735f8aa1`

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Setup your PingOne connector within Cyclr:

- Go to your **Cyclr Console**
- Click the **Connectors** menu along the top
- Choose **Connector Library**
- Scroll down to **PingOne**
- Click the **Setup** button

Enter the following values:

- **Client ID**: `Client ID` of the PingOne App
- **Client Secret**: `Client Secret` of the PingOne App
- **Auth Domain**: e.g. `auth.pingone.eu`, or `auth.pingone.com`, or auth.pingone.asia`
- **Environment ID**: UID for the environment you wish to connect to

</div>

</section>
