
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Set up an app within GitHub to obtain a `Client ID` and `Client Secret`.

1. Go to your [GitHub user's *Developer Settings](https://github.com/settings/developers) then *OAuth Apps* and create a new application.

2. Provide the following information:

    - *Application name*: The name displayed to your users when they grant your app access to their data
    - *Homepage URL*: The URL of your website
    - *Authorization callback URL* : Your Cyclr Callback URL available in your Cyclr Console , go to Connectors > Application Connector Library and find the GitHub Connector

3. On the next screen generate a `Client Secret` , note that and your `Client ID` for the Cyclr setup

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

1. In your Console, access *Connectors* > *Application Connectors*

    ![Application Connectors](./images/ApplicationConnectors.png)

2. Search for *GitHub*, and click the *Setup Required* padlock

    ![GitHub in Console](./images/GitHubInConsole.png)

3. In the next screen, enter your GitHub `Client ID` and `Client Secret` and *Save Changes*

4. Your GitHub connector is now set up, and you won't need to enter this information to authenticate the connector

</div>

</section>
