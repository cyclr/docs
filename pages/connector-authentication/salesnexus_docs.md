---
title: SalesNexus Connector Guide
sidebar: cyclr_sidebar
permalink: salesnexus-connector
tags: [connector]
---

## Connector Setup

The SalesNexus connector is authenticated with an API Key (authorization token).

You can use the following methodology to obtain a temporary API Key within the connector. The temporary API Key will expire after an unspecified amount of time, resulting in failed calls to the SalesNexus API. If you require a permanent API Key that will not expire (recommended), please contact SalesNexus support.

### Authenticate the connector

1. Locate the SalesNexus connector

   > Cyclr Console > Connectors > Connector Library > SalesNexus

2. From the Edit Connector interface click 'Setup'

3. If you have obtained a permanent API Key go to step 4. If you do not have a permanent API Key go to step 5

4. Enter your API Key and click 'Next'. The connector is now authenticated and ready to use.

The connector is now authenticated and ready to use.

5. Enter any random string into the 'API Key' field (eg. abc)

   ![salesnexus setup](./images/salesnexus_setup_1.png)

6. Locate the method 'Get API Key'

   ![salesnexus setup](./images/salesnexus_setup_2.png)

7. Click the 'Test' tab and then enter the Email and Password associated with your SalesNexus account. Click 'Run'

8. Your temporary API Key will be returned, copy it and go back to the 'Setup' page

   ![salesnexus setup](./images/salesnexus_setup_3.png)

9. Paste in your API Key and click 'Next'

The connector is now authenticated and ready to use.
