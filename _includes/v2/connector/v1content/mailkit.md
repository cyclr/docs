
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Login to your existing Mailkit account or [sign up for one](https://app.mailkit.eu/).

### Authentication Details

- Click **Create App**
- Go to your Profile page
- Click **Integration** 
- CLick **API Settings**
- On the Settings page, note the `User ID` and `MD5 Hash`
</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">


Authenticate the connector at either Partner level or Account level. 

### Partner Level

At Partner level all account installations of the connector share the same credentials.

Setup your Mailkit App within Cyclr:

- Go to your **Cyclr Console**
- Click the **Connectors** menu along the top
- Choose Application Connector Library
- Search for **Mailkit**
- Click the **padlock** button

Enter the following values:

**Client ID**:  The User ID that we retrieved from the app that we made.

**Client MD5**:  The MD5 Hash that we retrieved from the app that we made.

Your Mailkit Connector is now setup at Partner level. You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

### Account Level

To use separate credentials for each account installation, authenticate the connector at Account level.

From within the account you wish to install the connector:

- Click **Connectors** (top navigation bar)
- Click **Install New Application**
- Find **Mailkit** 
- Click **Install**
- The installation name and description are shown, enter appropriate text
- Click **Next**
- Enter your `Client ID` and `Client MD5`
- Click **Next**

Your Mailkit connector is now setup at Account level. You can test it by executing one of the methods to confirm it can return some data.

</div>

</section>
