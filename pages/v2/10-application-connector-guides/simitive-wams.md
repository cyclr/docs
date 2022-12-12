---
title: Simitive WAMS Authentication
sidebar: cyclr_sidebar
permalink: simitive-wams-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
# Simitive WAMS setup

You need the following information to setup the Simitive WAMS connector:

1. The client ID of your Simitive WAMS account.
2. The client secret of your Simitive WAMS account.

Your Simitive WAMS account manager/project manager should provide you with these.


</section>
<section class="card py-5 my-5">
## Cyclr setup

### Console setup

To setup the Simitive WAMS connector within your Cyclr console:

1. Go to your **Cyclr Console**.
2. Select **Connectors** > **Application Connector Library** at the top of the page.
3. Use the search box to find the **Simitive WAMS** connector.
4. Select the **Setup Required** icon.
5. Enter the below values, omitting this step will allow you to use different settings for each account on installation:

    | Value             | Description                                      |
    | ----------------- | ------------------------------------------------ |
    | **Client ID**     | The client ID of your Simitive WAMS account.     |
    | **Client Secret** | The client secret of your Simitive WAMS account. |

6. Select **Save Changes**.

### Account setup

You will be asked for the following values when installing the Simitive WAMS connector within an account:

| Value             | Description                                                                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Client ID**     | The client ID of your Simitive WAMS account, if you did not enter this in step 5 above.                                                                                         |
| **Client Secret** | The client secret of your Simitive WAMS account, if you did not enter this in step 5 above.                                                                                     |
| **Domain**        | The domain of your Simitive login URL. For example, if you use `http://myuni.simitive.com/` to sign in to your Simitive account, then enter the domain as `myuni.simitive.com`. |

</section>
