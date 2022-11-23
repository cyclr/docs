---
title: Map fields
sidebar: cyclr_sidebar
permalink: field-mapping
tags: [templates]

---

When using an Action step, you will need to map its fields.  You can do this through the 'cog' icon on the step which gives access to the Step Setup functionality.

## Field mapping example

![](./images/field-mapping-eg.png)

The left most column is the **Destination** (the app you are connecting to). Some of these fields may be required.

The **Source** for these fields, shown to the right, can be any preceding step or a combination of steps.

## Field mapping sources

Depending on the app you're connecting to and the field you are using, only some of these source types will be available.

| Source | Usage |
| --- | --- |
| Ignore | The field will be left blank and will not be included in the API call. |
| Variable | This is a 'parameter' that has been defined for the Template overall.  The variable may then be used at various places in the Template design. |
| Type a Value | You can type in text or merge one or more values into the field. |
| Previous Step | First select any previous step.  Cyclr will then display a searchable list of the available date from that step. If possible Cyclr will suggest a mapping. |
| Lookup | Cycler will connect to the Destination app to retrieve a list of possible mapping values. For example, a mailing lists in an email marketing platform. |
| Select a Value | There may be a pre-configured list of values from which you can choose a mapping. |

## User Configurable

Setting the field to be **User Configurable** means that this mapping will be finalised by the user when the Template in installed into an Account.  For the purposes of testing a value may be provided but this value will NOT be copied over on Template installation.

## System mergefields

You can use Cyclr system mergefields as the **Source** value in Field Mapping.

| Merge Field | Usage |
| --- | --- |
| {% raw %}{{LastSuccessfulRunDate}}{% endraw %} | The last successful run date of the current step. This is particularly useful if you only want to get the latest data. |
| {% raw %}{{Cyclr_Auth_ApiKey}}{% endraw %} | The API key if the connector is using API key as the authentication type. |
| {% raw %}{{Cyclr_Auth_Username}}{% endraw %} | The username if the connector is using username/password as the authentication type. |
| {% raw %}{{Cyclr_Auth_Password}}{% endraw %} |The password if the connector is using username/password as the authentication type.|

These Mergefields can be used to map fields directly and as part of the content within the **Type a Value** box.  For example, to construct the sentence:
```
The last run was {% raw %}{{LastSuccessfulRunDate}}{% endraw %}.
```