
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

To authenticate the monday<span></span>.com connector you will need a Board ID and an API Key.

> A new instance of the connector should be installed for each board you want to interface with.

### API Key

1. Log into your [monday.com](https://auth.monday.com/login) account

2. Click on your avatar (picture icon) in the bottom left corner

   ![monday dot com avatar](./images/monday_docs_2.png)

3. Select Admin from the resulting menu (this requires you to have admin permissions)

4. Go to the API section

5. Generate an "API v2 Token"

   ![monday dot com api token](./images/monday_docs_4.png)

6. Copy your token

> You can regenerate a new token at any time. Doing so will cause the existing one to expire.

### Board ID

1. On the left side of your monday<span></span>.com account's dashboard you should see a "Workspaces" menu

2. From that menu, locate the Workspace that contains the board you want to interface with

3. Locate and select the board, you will be redirected to the selected board's user interface

4. The Board ID will be displayed in the URL. From the following image our Board ID would be 123456789

   ![monday dot com board id](./images/monday_docs_1.png)

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

1. Locate the monday<span></span>.com connector

   > Cyclr Console > Connectors > Connector Library > monday<span></span>.com

2. From the Edit Connector interface click 'Setup'

3. Enter your Board ID, click 'Next'

4. Enter your API Key, click 'Next'

The connector is now authenticated and ready to use.

</div>

</section>
