---
title: Authentication example
sidebar: cyclr_sidebar
permalink: example-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

To access the authentication guide for a specific connector, you can either open the **Authentication Settings** page for the connector and select the **Authentication Setup Guide** button, or you can search for the connector guide in the [Application connectors](connector-guides) section of the documentation.

Different connectors use different authentication methods. Many use OAuth, but you can also use basic username and password or API Keys. You can either [authenticate the connector at partner level](#partner-level-authentication) or allow your customers to [authenticate on an individual account](#account-setup) basis.

</section>
<section class="card">

## Connector setup

The connector setup section includes information about what you need to do in the external application in order to connect with Cyclr. This can include setting up or configuring an account in the third party application, or might just list the authentication credentials that you need.

### **Requirements**

In order to connect with a third party application, you may need a specific type of account within that application, or may need to adjust your settings and permissions. The authentication guide for your specific connector specifies what you need to do.


### **Get authentication details**

To connect with Cyclr, you need to obtain authentication details from the third party application. For example, you may need to get values such as the following:

* Consumer Key
* Consumer Secret

</section>
<section class="card">

## Partner level authentication

You can authenticate most connectors at a partner level, which means that your customers can pass through the authentication process with your credentials when they install a connector into an account. This means that your customer only needs to log into their account to authenticate.

There are several ways in which authenticating a connector with OAuth can benefit you can your customers:

* You can keep Cyclr invisible when your customers install an integration cycle.
* Your customers can pass through your application’s credentials, so you can show them your name and branding for a consistent user experience.
* It can save your customers time as they don’t need to create their own credentials.

## Cyclr setup example

To set up the 1st Connect connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the 1st Connect connector.

3. Select the **Setup Required** icon.

4. Enter the following authentication details:

| **Value** | **Description** |
|---|---|
| **Consumer Key** | The Consumer Key from the 1st Connect account. |
| **Consumer Secret** | The Consumer Secret from the 1st Connect account. |
| **Callback URL** | Cyclr fills this field by default. |

5. Select **Save Changes**.

**Note**: If you leave any values blank, Cyclr asks for the value when you install the connector into an account. This means you can use different settings for different accounts, or allow your customers to authenticate with their individual credentials.

## Account setup

Some connectors don’t have the option for partner level authentication, or might have more fields available when the connector is installed into an account. Alternatively, if you need your customer to use their own individual credentials, you can allow them to do this when they install the connector into their account instead of authenticating the connector at partner level. If this is the case, the connector guide will outline what credentials your customer needs to install and authenticate the connector.

</section>