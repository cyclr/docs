---
title: Oracle NetSuite Connector Guide
sidebar: cyclr_sidebar
permalink: netsuite-connector
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">
## RESTlet Installation

To enable REST APIs in NetSuite, a "RESTlet" file must be deployed in your NetSuite account.

To support the NetSuite Connector, Cyclr has its own RESTlet file.  Please get in touch with your Support Team to request this.

Once you have the Cyclr RESTlet file, follow the steps in this documentation.

### Locating your NetSuite Account ID

Your NetSuite Account ID is required when installing the NetSuite Connector within Cyclr and is found in your NetSuite account.

In NetSuite to go **Setup** > **Company** > **Company Information**

Then look for **ACCOUNT ID**.

It might also be located under **Setup** > **Integration** > **Webservice Preferences**

### Upload the RESTlet script to NetSuite

You can upload the RESTlet script file to NetSuite from Customization > Scripting > Scripts > New. Make sure you select RESTlet as the Type and enter the GET / POST / DELETE / PUT function names based on your RESTlet script.

![Example1](./images/Netsuite_1.png)

![Example2](./images/Netsuite_2_2.png)

### Deploy the RESTlet script

Once your script is uploaded, you need to deploy the script. Make a note of the External URL which will be used when you install the NetSuite connector in Cyclr.

![Example3](./images/Netsuite_3.png)

To locate the External URL in future, go to **Setup** > **Scripting** > **Script Deployments** and click the **View** option for the appropriate entry.

### Create an integration in NetSuite

To allow Cyclr to access the RESTlet securely, you need to set up a token-based authentication in NetSuite. You can create an integration under Setup > Integration > Manage Integrations > New. Check the token-based authentication on the setup page.

![Example4](./images/Netsuite_4.png)

Save the integration and copy the consumer key and consumer secret. You will need them when installing the NetSuite connector.

### Create an access token

Create an access token from Setup > Users/Roles > Access Tokens > New. The application name should be the integration you created in the previous step. Select a user who have access to make REST calls and permissions to the objects you would like Cyclr to access.

![Example5](./images/Netsuite_5.png)

Make a note of the token ID and token secret. Cyclr will ask for them when you install the NetSuite connector.

</section>
