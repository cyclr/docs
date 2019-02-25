---
title: Custom Connector Fields
---

Field Properties
----------------

*   **ConnectorField **– the name of the field as used by the remote application’s API. Use Cyclr notation to locate the value, e.g. _[records].EmailAddress_ when receiving an array and retrieving the _EmailAddress _attribute from an element within that array (see _RequestFormat / ResponseFormat_ documentation).
*   **SystemField **– the name to use internally within Cyclr. Use the field as capitalised by the API and remove any spaces. Apps that have the same SystemField name can auto match values in the builder, saving time and making life easier.
*   **DisplayFieldName **– to be displayed in the Cyclr UI to the user. Typically, take the _SystemField _value and add spaces or anything that might help describe it, e.g. in _G_oogle Sheets the _ConnectorField_ _entry.title_ used when working with Rows becomes simply _Row Title_. Think human readable.
*   **Description **– this is the description of the Field to appear in the Cyclr UI for the user to understand how the Field is used. Always include this and keep fairly short (no more than 100 characters).IsOptionalSet to `true` if the Field doesn’t have to be given a value. Leave out if it’s a required Field.

Mergefields
-----------

A mergefields is placeholder will be substituted at runtime.

#### Supported Mergefields

*   LastSuccessfulRunDate – is the last time the cycle successfully ran the method. This is useful to find newly created or updated records in an app. A format string needs to be provided. For example, _{% raw %}{{LastSuccessfulRunDate format=yyyy-MM-ddTHH:mm:ssZ}}{% endraw %}_.

[View the Custom Connector References](./reference)