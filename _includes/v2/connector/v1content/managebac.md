
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Login to your [existing ManageBac account](https://www.managebac.com/login) via your ManageBac front-end.

### Retrieving an API Key

- Go to **Settings** > **Develop** > **API Manager**
- Click **"Add New Token"** or **copy** an existing API token
- To **create** a new token:
    - Set an appropriate name for the API token
    - Set the appropriate permissions for the token
        - Setting all permissions is a security breach: choose carefully
        - Permissions can be set on actions in each category, to restrict API actions as required
            e.g. to restrict the  API to update students tick the **"update"** box under the **students** category
    - Click **"Add Token"**
- Note the **API Token**

See the [ManageBac Public API for integrations](https://managebac.zendesk.com/hc/en-us/articles/360018226931-Enabling-ManageBac-Public-API-for-Integrations) for more information.

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Setup your ManageBac App within Cyclr:

- Go to your **Cyclr Console**
- Click the **Connectors** menu along the top
- Choose Connector Library
- Scroll down to **ManageBac**
- Click the **Setup** button

Enter the following values:

**API Key**: The API token noted during Partner setup.

Your ManageBac Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</div>

</section>
