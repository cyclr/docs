---
title: Epicor authentication
sidebar: cyclr_sidebar
permalink: epicor-connector
tags: [connector]

---

{::options parse_block_html="true" /}

<section class="card">

## Cyclr setup

You need the following information to authenticate the Epicor connector:

| Field            | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| Kinetic Server   | The Epicor Kinetic Server account domain and subdomain not including the protocol. For example, if the Epicor Kinetic Server URL is `https://ukkineticserver00.epicorsaas.com` then enter `ukkineticserver00.epicorsaas.com` |
| Kinetic Instance | The Epicor Kinetic Server unique instance ID. For example, `Test001Pilot`. |
| API Key          | The Epicor Kinetic account API key used to connect to the Epicor Kinetic Instance. To request an API Key, please contact [Epicor Support](https://epiccare.epicor.com/epiccare). |
| Company ID       | The Epicor Kinetic account company ID. |





To set up the Epicor connector in Cyclr, go to your Cyclr console:

1. Go to **Connectors** > **Application Connector Library**.

2. Use the search box to find the Epicor connector.

3. Select the **Setup Required** icon.

4. Enter the **Kinetic Server** of your Epicor account.

5. Enter the **Kinetic Instance** of your Epicor account.

6. Enter the **Company ID** of your Epicor account.

7. Enter the **API Key** from your Epicor account.

8. Select **Save Changes**.

</section>
