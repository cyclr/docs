
## Partner Setup

#### Retrieving public and private key
* Login to your Zendesk Sell front-end. 
* Click the settings cog on the left side of the page.
* Navigate to **Integrations** > **OAuth** > **Developer Apps**.
* Create a new app, enter your Cyclr redirect URL (https://``Your Service Domain``/connector/callback).
* Click save, and then **Details** and note down the Client ID and Client Secret.

### Cyclr Setup

Setup your Zendesk Sell App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Zendesk Sell**
*   Click the **Setup** button

Enter the following values:

**Client ID**: Retrieved from the above steps.

**Client Secret**: Retrieved from the above steps.


Your Zendesk Sell Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
