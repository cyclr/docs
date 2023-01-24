---
title: Marketo Connector Guide
sidebar: cyclr_sidebar
permalink: marketo-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Authentication

To get a **client ID** and **client secret** you must login to your Marketo installation as an admin.

1. Go to **Admin** > **LaunchPoint** under the **Integration** menu.
2. Click on **View Details** under the service that you want to use. If no services are shown, create a new one.
3. Copy the **client ID** and **client secret** from the prompt.

### Cyclr Setup

Setup your Marketo App within Cyclr:

- Go to your **Cyclr Console**
- Click the **Connectors** menu along the top
- Choose Connector Library
- Scroll down to **Marketo**
- Click the **Setup** button

Enter the following values:

**Client ID**:  Enter the client ID that we retrieved from LaunchPoint.

**Client Secret**: Enter the client secret that we retrieved from LaunchPoint.

**API Subdomain**: The subdomain from your api instance endpoint. For example, "https://{{subdomain}}.mktorest.com".

Your Marketo Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.


</section>
