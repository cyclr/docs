
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

### Client ID and Secret

- Go to your Brightspace instance
- Click the cogs at the top right part of the screen, next to your account name
- Click **Locale Management** under the **Organisation Related** category: you must log in as an administrator to see this
- Go to the **OAuth 2.0** area
- Click **Register and app**
- Enter an appropriate name, and enter your Cyclr redirect URL,  `https://[Your Service Domain]/connector/callback`
- Enter the appropriate scopes for your integration 
	> See [here](https://docs.valence.desire2learn.com/http-scopestable.html) for more information. To use all availableBrightspace connector methods, set scopes to `content:*:* core:*:* datahub:*:* enrollment:*:* extended-user-profile:values:manage grades:*:* quizzing:*:* users:*:*`
- Leave the access token lifetime as the default (3600)
- Accept the agreement and click **Register**
- Go to the next screen to see `Client ID` and `Client Secret`
- Note these two values for Cyclr setup

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Setup your Brightspace App within Cyclr:

- Go to your **Cyclr Console**
- Click the **Connectors** menu along the top
- Choose Connector Library
- Scroll down to **Brightspace**
- Click the **Setup** button

Enter the following values:

- **Domain**: Your Brightspace instance URL. The same URL used to create the  app. If your Brightspace instance is `"`https://teaching.school.edu.uk/`"`,  enter `teaching.school.edu.uk`
- **Client ID**: noted during partner setup
- **Client Secret**: noted during partner setup
- **Scope**: The API scope, outlining which areas this connector can access. See the [Brightspace Scopes Table](https://docs.valence.desire2learn.com/http-scopestable.html) for more information.
- **LE API Version**: The specific version to use for all LE-based API calls - always use the most recent version unless you need a specific version.
- **LP API Version**: as above but for LP-based API calls
- **BFP API Version**: as above but for BFP-based API calls


Your Brightspace Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</div>

</section>

