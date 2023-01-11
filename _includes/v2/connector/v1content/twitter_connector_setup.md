
## Obtaining Authentication Credentials

To authenticate the Twitter connector you will need a Twitter developer account and to have created a developer app.

Please refer to the [official Twitter documentation](https://developer.twitter.com/en/docs/platform-overview) for a comprehensive guide on setting up API access.

To summarize:

1. If you don't already have one, you can sign up for a developer account [here](https://developer.twitter.com/en/portal/petition/essential/basic-info)

2. When you have a developer account set up, go to your [App dashboard](https://developer.twitter.com/en/apps)

3. Click "Create an App" in the upper right corner (unless you intend to use an existing app)

4. Of most importance are the Callback URL and permissions

5. The Callback URL for the App should be https://{Your Cyclr service domain e.g. <span>app-h.cyclr.</span>com}/connector/callback

6. The permissions for the App should be "Read, write, and Direct Messages"

7. Make a note of the API Key and Secret (also known as Consumer Key and Secret) as these are what you will need to authenticate the connector

## Connector Setup

1. Locate the Twitter connector

   > Cyclr Console > Connectors > Connector Library > Twitter

2. From the Edit Connector interface click 'Setup'

3. Enter your Consumer Key and Consumer Secret, click 'Next'

4. You will be presented with a twitter login modal. Log in and authorise the connector's access

You will then be redirected to Cyclr where the connector is now authenticated and ready to use.
