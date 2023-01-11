
<section class="setup partner" markdown="1">

<div class="section-content" markdown="1">

## Partner Setup

### OAuth2 Details

- [Login](https://app.optimizely.com/signin) to an Optimizely developer account, or [sign up for an account.](https://www.optimizely.com/rollouts/)
- Click **Account Settings** in the bottom left area of the navigation tree
- Navigate to the **Registered Apps** tab
- Click **Register New Application**
- Enter an appropriate name for the application
- Enter your redirect URL **https://\[Your Service Domain\]/connector/callback**
- Set the **Client Type** as Confidential
- Click **Apply**
- Copy the generated `Client ID` and `Client Secret` values

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Setup your Optimizely App within Cyclr:

- Go to **Cyclr Console**
- Click the **Connectors** menu along the top
- Choose **Connector Library**
- Scroll down to **Optimizely**
- Click the **Setup** button

Enter the following values:

- **Client ID**: The `Client ID` retrieved in the Partner Setup
- **Client Secret**: The `Client Secret` retrieved in the Partner Setup

Your Optimizely Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.


</div>

</section>
