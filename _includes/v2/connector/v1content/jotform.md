
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

To authenticate the JotForm connector you need:
- `API Key` 
- `API Domain`

### API Key

1. Login to your JotForm account
2. Go to **(user menu icon in top-right corner)** > **Settings**
3. On your dashboard, click **API** in the menu
4. If there are no API Keys, click the **Create New Key** button
5. Set the permissions to **Full Access**
6. Note the `API Key` 

### API Domain

The 'API Domain' is one of:
   - api.jotform.com for US
   - eu-api.jotform.com for EU 
   - custom domain

To find out which server your JotForm account uses:

1. Go to your JotForm dashboard 
2. Click the **Data** menu option
3. If the "Europe Datacenter" box is checked your account uses the EU server. If it's unchecked your account uses the non-EU (US) server.

### File Access

To download files using the connector, disable one of the privacy settings in JotForm as follows:

1. Go to your JotForm dashboard 
2. Click the **Settings** menu option
2. Find the **Privacy** section
3. Uncheck the **Require log-in to view uploaded files** checkbox if it is checked

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

1. Go to the JotForm connector

   > Cyclr Console > Connectors > Connector Library > JotForm

2. Click **Setup** in the Edit Connector interface 

3. Enter your API Domain, one of:
   
   - api.jotform.com for US
   - eu-api.jotform.com for EU 
   - custom URL

4. Click **Next**

5. Enter your `API Key`

6. Click **Next**

The connector is now authenticated and ready to use.

</div>

</section>
