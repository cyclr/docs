
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

### Login / Sign Up

Login to Caspio [here](https://id.caspio.com/) or begin the sign up process [here](https://www.caspio.com/).

### Setting up your Account

For your API integrations to work, you must:

1. Select your account.
2. Open an existing Application or Create a new Application.
3. In the top navigation bar, access: Account -> Access permissions -> Web Services profiles.
4. If no accounts exist, [create a Web Services Profile](https://howto.caspio.com/web-services-api/creating-a-web-services-api-profile/).
5. Click the properties label under your account name.
6. You will then be able to see:
   > **Token Endpoint URL**: This contains your Account Subdomain. The Account Subdomain is the string of characters between 'https://' and '.caspio.com'.
   >
   > _For Example_: https://__example__.caspio.com/oauth/token
   >
   > **Client ID**: Your client ID.
   >
   > **Client Secret**: Your client secret.
   > For more detailed instructions on where to find this information, try the [official documentation](https://howto.caspio.com/web-services-api/rest-api/authenticating-rest/).

For further information, please see the [Official Caspio documentation](https://howto.caspio.com/).

</div>

</section>

<section class="setup partner" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

Setup your Caspio within Cyclr:

- Go to your **Cyclr Console**
- Click the **Connectors** menu along the top
- Choose Connector Library
- Scroll down to **Caspio**
- Click the **Setup** button

Enter the following values:

> **Account Subdomain**
>
> **Client ID**
>
> **Client Secret**
>
> Please see _'Setting up your account'_ for where to get these details.

Your Caspio Connector is now set up! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

## Utilising Custom Object Categories

The methods within some categories (like Tables) require you to create a custom object category. This is to create a clearer user experience when creating cycles.

In Cyclr:

1. Go to My Connectors.
2. Select Capsio.
3. When some categories are expanded (to reveal their methods) a copy button will appear below the category name.
4. Once you press this button, you will be able to select which item to create the Custom Category for (For example a specified Table).
5. Now when you return to your Cycle editor, you will see the new category (marked with a star), which will automatically connect with the object that was assigned to it.

</div>

</section>
