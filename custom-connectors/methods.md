---
title: Custom Connector Methods
---

*   **Name **– the name of the method to appear in the Cyclr UI for the user to see. Should be short and snappy and have initial caps for nouns/verbs, lowercase for minor words (like “a” or “to”), e.g. “Delete Emails”, “Get All Contacts”, “Send to List”.
*   **Description **– this is the description of the method to appear in the Cyclr UI for the user to understand what the method does and be informed of any special/interesting values to pass. Can be quite lengthy if appropriate. Can also include links to helpful API documentation if useful.
*   **Hide **– this will hide the method in the Cyclr UI if set to true. Leave out if not hiding.
*   **Category **– used to group methods in the Cyclr UI. Try to keep to single, pluralised words, e.g. “Emails” or “Contacts”.
*   **MethodType **– this defines where the method will appear in the Cyclr UI: Action or Webhook.
*   **HttpMethod **– this is the action to be performed on the API method. Supported methods are GET, POST, PATCH, PUT, DELETE.
*   **DataType **– this is the data type used by the API, either Json, Xml, or Form. For GET, this is the Accept header. For POST, this is the request data. JSON is our recommended data type.
*   **Endpoint **– this is the URI to the API method. This is null if this method is a webhook.
*   **XmlRootElement **– the single root element for the XML document.
*   **RequestFormat **/ **ResponseFormat **– this contains the request or response message format Fields. Each Field has ConnectorField, SystemField, and DisplayField. ConnectorField is the field name used in the connector. If a field is inside an array, it needs to be defined as \[Array\].Field. Multiple-dimension arrays can be defined as \[Array1\].\[Array2\].Field, etc. What if there is a field called \[Array2\].Field inside an Array1? We use \[Array1\].\\Array2.Field\\ to explicitly define Array2.Field as a field name. SystemField is the system name for the field. We use PascalCasing for system names as a convention. DisplayField is the name shown in the Cyclr UI.
*   **Fields **– the names of fields to use in the API call. Fields must have been defined in the connector to appear here. Name, TriggerName, IdentifierKey, and HumanReadableKey are needed.

[Take a Look at Custom Connector Examples](./examples)