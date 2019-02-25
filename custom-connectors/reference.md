---
title: Custom Connector Reference
---

A connector is a JSON formatted text file made up of the following parts.

*   **Authentication **– how the connector should connect to the target API (e.g. OAuth, API key, login, etc).
*   **Properties **– the description, version, icon, etc.
*   **Methods **– the endpoints for the API.
*   **Fields **– the fields used in the methods.
*   **Parameters and Triggers** – if the method requires parameters, mergefields, or internal look-up methods.
*   **Paging **– if the target API supports paging for large record sets.
*   **Scripting **– add JavaScript for custom API requirements.

[Learn About Custom Connector Properties](./properties)