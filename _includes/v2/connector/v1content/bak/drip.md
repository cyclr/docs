
## Drip Setup
In order to authenticate the connector, you will need your **Client ID** and **Client Secret**.  You get these by setting up an Application within Drip.

You will need to provide your Cyclr Partner **Service Domain** as part of the process of setting up access so best to have that information to hand before starting. This is specific to your instance of Cyclr and it can be found from the Cyclr Partner Console under: **Settings > General Settings > Service Domain**.

### Setting up oAuth Application

- Go to https://www.getdrip.com/user/applications
- choose a name for your application
- click **Create Application**.
- in Callback URL, put ``https://YourServiceDomain/connector/callback`` 
- copy the Client ID and Client Secret for use in setting up the connector.
- click **Save**, and then **Activate**.

### Installing the Connector

- You will now be able to authenticate the connector.
- Use the credentials from above steps.
