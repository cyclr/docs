
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

### Client ID and Client Secret
- Navigate to [the app console](https://www.dropbox.com/developers/apps) page
- Click *Create App*
- Click *Scoped access*, choose full access or specific folder access and enter a name for the app
- Open the newly created app
- Enter your redirect URL `https://[Your Cyclr Service Domain]/connector/callback`
- Note down the *App Key* and *App Secret*
- Navigate to the *Permissions* tab
- Tick the following permissions to fully use the connector:
  - *files.metadata.read* to use the *Search Files and Folders* method
  - *files.content.read* to use the *Get Temporary File* method
- Save your changes

</div>

</section>

<section class="setup partner" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Setup your Dropbox App within Cyclr:

- Go to your *Cyclr Console*
- Click the *Connectors* menu along the top
- Choose Connector Library
- Scroll down to *Dropbox*
- Click the *Setup* button

Enter the values noted during the partner setup:

- `Client ID`:  The Client ID
- `Client Secret`:  The Secret ID


Your Dropbox connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</div>

</section>
