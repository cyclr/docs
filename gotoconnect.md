| title                       | sidebar       | permalink             | tags      |
| --------------------------- | ------------- | --------------------- | --------- |
| GoTo Connect Authentication | cyclr_sidebar | gotoconnect-connector | connector |

## GoTo Connect setup

You will need to log into your server's developer portal and obtain a Client ID and Client Secret. Please refer to GoTo Connect's [documentation](https://developer.goto.com/Authentication/#section/Obtaining-Client-Credentials) on how to obtain these.

To set up the GoTo Connect connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the GoTo Connect connector.

3. Select the **Setup Required** icon.

4. Enter the below values:

   | Value             | Description                                                  |
   | ----------------- | ------------------------------------------------------------ |
   | **Client ID**     | The Client ID. This can be accessed from the developer's portal. |
   | **Client Secret** | The Client Secret from your GoTo Connect account.            |
   | **Domain**        | The server where the account is hosted, e.g. api.jive.com    |

5. Select **Save Changes**.

> Note: To use different settings for different accounts, leave the value blank. This means Cyclr asks for the value when you install the connector into an account.
