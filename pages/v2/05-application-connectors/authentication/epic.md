---
title: Epic Authentication
sidebar: cyclr_sidebar
permalink: epic-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Partner Setup

#### Retrieving client ID and secret
* Login and navigate to the [app builder](https://fhir.epic.com/Developer/Apps).
* Create a new app, give it an appropriate name. Select <code>Clinicians or Administrative Users</code> as the <code>Application Audience</code>.
* Note the client ID down if you would like to use the connector in a production environment, or note the non-production client ID if you would like to use the sandbox.
* The following table shows the required incoming APIs required for each method:

| Method          | Incoming API        |
|-----------------|---------------------|
| Get Patient     | Patient.Read (R4)   |
| Search Patients | Patient.Search (R4) |

* Enter your redirect URL: <code>https://{{ServiceDomain}}/connector/callback</code>
* Make sure <code>Should Epic require refresh tokens when authenticating?</code> is ticked.
* Generate a secret, note it down, and then store the hash.
* Select <code>R4</code> for the <code>FHIR Version</code>.
* Accept the terms and mark the app as ready for production if you are using the connector in a production environment. Otherwise, mark the app as ready for sandbox.

### Cyclr Setup

Setup your Epic App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Epic**
*   Click the **Setup** button

Enter the following values:

**Endpoint**: The organization API endpoint you would like to query. A list of R4 endpoints can be found [here](https://open.epic.com/MyApps/Endpoints). Please remove the "api/FHIR/R4" substring from the end of the URL. To use the sandbox version, please enter "https://fhir.epic.com/interconnect-fhir-oauth/".

**Client ID**: Retrieve from the above steps.

**Client Secret**: Also retrieved from the steps above.

Your Epic Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</section>
