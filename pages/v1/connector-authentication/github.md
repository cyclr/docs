---
title: GitHub Authentication
sidebar: cyclr_sidebar
permalink: github-authentication
tags: [connector]

---

To use the GitHub connector you will need to set up an app within GitHub, to obtain a Client ID and Client Secret.

## Setting up your GitHub app

1. Go to your [GitHub user's **Developer Settings**](https://github.com/settings/developers) then **OAuth Apps** and create a new application.

2. Provide the following information:

    * **Application name**: This name will be presented to your users when they grant your app access to their data.
    * **Homepage URL**: This should be the URL to your application's website where users can find out more information about your system.
    * **Authorization callback URL** : This is your Cyclr Callback URL and can be found in your Cyclr Console from the Connectors menu &gt; Application Connector Library, then in the entry for the GitHub Connector.

3. On the next screen generate a Client Secret and record that and your Client ID for later use.

## Authenticating your GitHub Cyclr Connector

1. In your Console, access `Connectors` > `Application Connectors`

    ![Application Connectors](./images/ApplicationConnectors.png)

2. Search for "GitHub", and click the `Setup Required` padlock.

    ![GitHub in Console](./images/GitHubInConsole.png)

3. In the next screen, enter your GitHub Client ID and Client Secret and `Save Changes`.

4. Your GitHub connector is now set up, and you won't need to enter this information again when authenticating the connector.
