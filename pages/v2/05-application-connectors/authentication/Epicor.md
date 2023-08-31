---
title: Epicor authentication
sidebar: cyclr_sidebar
permalink: epicor-connector
tags: [connector]

---

{::options parse_block_html="true" /}

<section class="card">

## Cyclr setup

To authenticate your connector, you need the following information Epicor account.

| Field            | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| Kinetic Server   | The Kinetic Server domain of your Epicor Kinetic account. this will be just domain without any HTTP protocals for example: `ukkineticserver00.epicorsaas.com` |
| Kinetic Instance | The unique ID for the Instance of the Epicor Kinetic Server you wish to access. for example: `Test001Pilot` |
| API Key          | The API Key for your Epicor account. To request an API Key you will need to contact [Epicor Support](https://epiccare.epicor.com/epiccare) |
| Company ID       | The ID associated to the Company for the Epicor Kinetic account. |





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
