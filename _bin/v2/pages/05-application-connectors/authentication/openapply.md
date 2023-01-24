---
title: OpenApply Connector Guide
sidebar: cyclr_sidebar
permalink: openapply-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Setup

To authenticate the OpenApply connector you will need a Client ID, Client Secret and the name of you account.

### Client ID & Client Secret

To obtain your Client ID and Client Secret, within your OpenApply account:

1. Navigate to Settings and open the Public API page for which you would like to add a new application.

2. You will find your Client ID, Client Secret, and Redirect URI on this page.

> Redirect URI should be {% raw %}https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback{% endraw %}

### OpenApply Account (name)

Your OpenApply account as displayed in your account URL. Example: if your account URL was https://<span>demo.openapply.</span>com then your account name would be **demo**.

### Connector Setup

1. Locate the OpenApply connector

   > Cyclr Console > Connectors > Connector Library > OpenApply

2. From the Edit Connector interface click 'Setup'

3. Enter your Client ID, Client Secret and OpenApply Account Name, click 'Next'

The connector is now authenticated and ready to use.


</section>
