---
title: Five9 information
sidebar: cyclr_sidebar
permalink: five9-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}

<section class="card">
  
## Managing sessions

The Five9 connector requires a session to be active to make requests to the API. This session is a connection between Cyclr and the Five9 API. You can only have one active session per account. The session will time out if you do not make a request to the API within a specified time period.

### Create a session

Create a session by using the **Sessions > Set Session Parameters** method. The **Rolling Period** and **Statistics Range** parameters define how statistics are returned from the API for requests in the session. The time out duration is defined by the **Idle Time Out** parameter, this will default to `180` seconds if not set.

If a session is already active when this method is called, the already active session will be updated with a new session with the set parameters. If no session is active when this method is called, a new session will be started.

### Check session status

Check the status of a session by using the **Sessions > List Session Parameters** method. When placed in a cycle, this method has true/false exits that will reflect the status of the current session:

- If there is an active session, the method will return the session parameters and exit through the true exit.

- If there is no active session, the method will exit through the false exit.

### Maintain a session

To permanently maintain an active session using a cycle:

1. Create a cycle with the following Five9 methods from the **Sessions** category: ![Cycle example showing the false exist of the List Session Paramaters method connected to the Set Session Parameters method](../../../../images/Five9-cycle.png)
2. In the cycle, select **Step Setup** for the **Set Session Parameters** method.
3. Set any required parameters and set the **Idle Time Out** parameter to `1800`.
4. Select **Close**.
5. Select **Run > Repeat**.
6. Set **Run this cycle every** to `15 minutes`.
7. Select **Run Now**.

</section>
