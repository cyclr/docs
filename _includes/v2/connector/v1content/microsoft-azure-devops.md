
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">


See the full [Microsoft Azure DevOps Authentication documentation](https://docs.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/oauth?view=azure-devops). 

The **Microsoft Azure DevOps** Connector is authenticated using OAuth2.0.

### Application registration

Either your or your end-users will need to [register an application with Microsoft](https://app.vsaex.visualstudio.com/app/register) and provide its details to Cyclr.

If all your users are to accept the same Authorized Scopes when they authenticate a **Microsoft Azure DevOps** Connector, register a single application and set its details and Scopes in your Cyclr Console's **Connectors** > **Application Connector Library** entry.

If users require different Authorized scopes, either they or you can register separate applications with the appropriate scopes set.  Details of the application and scopes must  be provided when authenticating the Connector.

When authenticating the Connector, the Scopes parameter used **must** match the Authorized scopes specified on the application being used.  If they are different, you will see an `InvalidScope` error from Microsoft's API.


Register an application [here](https://app.vsaex.visualstudio.com/app/register)

Set the **Authorization callback URL** to:

`https://<Your Cyclr Service Domain e.g. app-h.cyclr.com>/connector/callback`

Note the values displayed on completing registration:
- `App ID`
- `App Secret`
- `Client Secret`

#### Scopes
Select appropriate **Authorized scopes** for your use-case.

We suggest at least adding "Work items (full)": this is required for most methods apart from Audit Logs and Accounts.
 
See a list of available scopes [here](https://docs.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/oauth?toc=%2Fazure%2Fdevops%2Forganizations%2Ftoc.json&bc=%2Fazure%2Fdevops%2Forganizations%2Fbreadcrumb%2Ftoc.json&view=azure-devops#scopes)


</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

### Same scopes for all users

- Go to your Cyclr Console
- Go to **Connectors** > **Application Connector Library**
- Find the entry for **Microsoft Azure DevOps**
- Enter your `App ID` into the **Client ID** box
- Enter your `Client Secret` into the **Client Secret** box
- Select the same list of **Scopes** that you set on your application
- Click **Save**

### Different scopes

Leave the **Application Connector Library** entry blank: this requires the user to provide all the details when installing the Connector.

This also allows different application details and related Scopes to be used that meet each user's requirements.

### Setting Scopes/InvalidScope Error

The list of permissions you set for the **Scopes** Connector parameter must match the **Authorized scopes** you set when registering your App at [https://app.vsaex.visualstudio.com/app/register](https://app.vsaex.visualstudio.com/app/register).

The connector authentication results in an `InvalidScope` error if the scopes do not match.

### Organization ID and Project Name

When installing the Connector the **Organization ID** and **Project Name** to work with are needed.

Login to the [DevOps portal](https://aex.dev.azure.com/) to get these:

<img src="./images/AzureDevOps1.png" style="zoom:75%;" />


1. Begin installation of the **Microsoft Azure DevOps** Connector and enter the **Organization ID** and **Project Name** values.

2. Click **Sign In** and a new window will open prompting you to log in.

3. Select your Azure account and authorize access.

The Connector is now authenticated and ready for use.


</div>

</section>
