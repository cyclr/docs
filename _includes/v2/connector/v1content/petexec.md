
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

To authenticate the PetExec connector you need:
- `Client ID`
- `Client Secret`
- Your account name

### Client ID & Client Secret

To obtain your Client ID and Client Secret:
1. Login to your PetExec account
2. Go to **Company Preferences** > **Misc. Settings** > **Maintain API Applications**

   ![petexec portal](./images/petexec_img_1.png)

3. Enter an application name
4. Enter the callback URL. This is your Cyclr service domain, e.g. `https://{Your Cyclr service domain e.g. <span>app-h.cyclr.</span>com}/connector/callback`
5. Select the `report_read` and `owner_read` scopes
6. Click **Add Application**

Your `Client ID` and `Client Secret` are displayed.

### Account Name

Your PetExec account as it is formatted in the URL.

If the URL for your account is `https://secure.mycompany.net/`,  your account name is `mycompany`.

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

1. Login to your Cyclr Console
2. Go to **Connectors** > **Connector Library** > **PetExec**
3. From the Edit Connector interface click **Setup**
4. Enter your `Client ID`, `Client Secret` and PetExec Account Name
5. Click **Next**
6. Click **Sign In**
7. Login to your PetExec account when prompted

You are redirected to Cyclr.

The connector is now authenticated and ready to use.

</div>

</section>
