---
title: Field Mapping
sidebar: cyclr_sidebar
permalink: field-mapping
tags: [getting-started]
---

When using a (blue) Action step, you will need to map its fields.

#### Field mapping example

![](./images/field-mapping.png)

The left most column is the **Destination** (the app you are connecting to). Some of these fields may be required.

The **Source** for these fields, shown to the right, can be any preceeding step or a combination of steps.

#### Field mapping sources

Depending the app you’re connecting to and the field you are using, only some of these source types will be available.

*   **Type a Value**: type in text or merge one or more values into the field.
*   **Previous Step**: select any previous step and then a field from this step.
*   **Lookup**: connect to the Destination app to retrieve a list of possible mapping values. For example, a mailing lists in an email marketing platform.
*   **Select a Value**: choose from a pre-configured value.
*   **Ignore**: do not use the field.

#### System mergefields

You can use Cyclr system mergefields as the **Source** value in Field Mapping.

*   **{% raw %}{{LastSuccessfulRunDate}}{% endraw %}**: get the last successful run date of the current step. This is particularly useful if you only want to get the latest data.
*   **{% raw %}{{Cyclr_Auth_ApiKey}}{% endraw %}**: get the API key if the connector is using API key as the authentication type.
*   **{% raw %}{{Cyclr_Auth_Username}}{% endraw %}**: get the username if the connector is using username/password as the authentication type.
*   **{% raw %}{{Cyclr_Auth_Password}}{% endraw %}**: get the password if the connector is using username/password as the authentication type.

<br />

Initially, these Mergefields had to appear as the only content in the **Type a Value** box, but have since been updated to allow them to be used with other text, e.g.:
```
The last run was {% raw %}{{LastSuccessfulRunDate}}{% endraw %}.
```
and even Inline Script:
```
=require('moment');moment(`{% raw %}{{LastSuccessfulRunDate}}{% endraw %}`).subtract(1, 'days').toISOString();
```


[How to Test your Cycles](./testing-cycles)
