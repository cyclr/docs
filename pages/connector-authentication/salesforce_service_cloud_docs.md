---
title: Salesforce Service Cloud Connector Guide
sidebar: cyclr_sidebar
permalink: salesforce-service-cloud-connector
tags: [connector]
---

## Connector Setup

1. Locate the Insider connector in the Cyclr console.

   > Cyclr Console > Connectors > Connector Library > Salesforce Service Cloud

2. Click the open padlock and on the next page enter the following information:

   | Name          | Description                                                                             |
   | ------------- | --------------------------------------------------------------------------------------- |
   | Client ID     | Your Salesforce Connected Apps 'Consumer Key'                                           |
   | Client Secret | Your Salesforce Connected Apps 'Consumer Secret'                                        |
   | Username      | Your Salesforce Username                                                                |
   | Password      | Your Salesforce Password + Security Token (**Important: Must include security token**)  |
   | Subdomain     | The subdomain of your Salesforce account. (eg. https://{{Subdomain}}.my.salesforce.com) |

#### Password Format

If your Salesforce password is "mypassword" and your security token is "XXXXXXXXXX" you would enter "mypasswordXXXXXXXXXX".

#### Security Token

The security token is included in the initial email from Salesforce when you create an account. If you can't locate that email or the token, you should request a new token. The process for that is as follows:

1. Log in to Salesforce
2. In the User Menu, select Setup.
3. In the menu on the left, under Personal Setup, expand My Personal Information, and then click Reset My Security Token.
4. Follow onscreen instructions.

A new email message will be sent containing the security token.
