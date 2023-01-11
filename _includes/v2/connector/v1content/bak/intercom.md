
# Intercom #

Partner Setup
-------------

Intercom uses OAuth 2 for remote API access. You must register Cyclr within Intercom as your own App to receive OAuth Client ID and Client Secret values to enable Cyclr to authenticate with Intercom.

The official Intercom documentation describing the process can be found here:
* [Creating an App](https://developers.intercom.com/building-apps/docs/get-started-developing-on-intercom)
* [Setting up OAuth](https://developers.intercom.com/building-apps/docs/setting-up-oauth)

**Redirect URL**: you must add a callback URL to allow Intercom to be used in your Cyclr Console and its accounts.

The URL is:

*   {% raw %}https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback{% endraw %}

Your Cyclr Partner **Service Domain** can be found in your Cyclr Console under Settings > General Settings.

**Required Permissions**
* Read one user and one company
* Write conversations
* Read admins

Choosing The Correct Version
-------------

As you will see we have connectors for multiple versions of the Intercom API. As the available endpoints differ for these different versions, it's important that you use the connector that matches the version your Intercom app uses.

To find out which version your app is set to:

1. [Login](https://app.intercom.com/admins/sign_in?on_pageview_event=sign_in_nav) to your account

2. Hover over the icon in the bottom left corner and select 'Settings'

   ![intercom home](./images/intercom_docs_1.png)
   
3. From the settings page, select Developers > Developer Hub

   ![intercom settings](./images/intercom_docs_2.png)
   
4. Once in the Developer Hub, select the relevant app

5. From the 'Basic Information' page you will see various information about the app, including the version

   ![intercom app information](./images/intercom_docs_3.png)
   
6. If you want to change the version, click 'Change version' and then select the desired version from the dropdown menu

   ![intercom change version](./images/intercom_docs_4.png)
   
> **Important: Please review the [changelog](https://developers.intercom.com/building-apps/docs/api-changelog) for a detailed description of the differences between each API Version.**
