---
title: Release notes
sidebar: cyclr_sidebar
permalink: release-notes
tags: [managing-cyclr]
menus:
    about-cyclr:
        title: Release notes
        identifier: release-notes
        toggleonly: menutoggleonly
        weight: 8
---
{::options parse_block_html="true" /}
<section class="card">

## 2023

### 21st July 2023

* **API**: Updated CodeMirror so it doesn't incorrectly flag errors.
* **API**: Added validation to the Application User Agent property to avoid errors.
* **Connectors**: Updated the warning text on authentication pages.
* **Connectors**: Ensured that Cyclr displays the correct fields when you change the type of authentication.
* **Dashboard**: Implemented a new Task Usage widget onto the Cyclr dashboard.
* **Dashboard**: Added a redirect to the sign in page when you're logged out of an instance.
* **LAUNCH**: Ensured that the Cancel button works for the authentication process.
* **Partners**: Ensured that the Task Usage reports are accurate.
* **Partners**: Produced a report that aggregates task usage per partner per month for the 13 months up to execution date.
* **Templates**: Excluded text comments from script checks.
* **Templates**: Encoded `#` properly for URL merge fields.
* **Templates**: Made sure that you can promote a template to live when you add or delete a variable.
* **Templates**: Ensured that the Format script button works as expected.
* **Templates**: Added support so you can import a JSON template that has a Wait Until step.
* **Templates**: Disabled System Name text boxes, Value Type dropdowns and User Configurable switches when you promote a template release to live. .

### 30th June 2023

* **Accounts**: Made variable descriptions visible in account cycles.
* **API**: Fixed formatting of the API Report page for long request body strings.
* **API**: Updated jQuery.Validation from 1.19.2 to 1.19.5.
* **Connectors**: Ensured that you can authenticate native connectors via the UI.
* **Connectors**: Set a release notes template for new connectors and new connector drafts.
* **Connectors**: Changed modal title from **Display Field** to **Connector Field** in the Request Format/Response Format tabs when you edit a connector method.
* **Dashboard**: Updated the Console's featured blog post.
* **Security**: Made sure to redact sensitive values in the message when the script engine throws a JavaScript exception.
* **Templates**: Included the `MethodUniqueIdentifier` for a step in the step setup's **Advanced Settings**.
* **Templates**: Added support for square brackets in a **Field Location** to indicate a name.
* **Templates**: Ensured that step request arrays contain all items.
* **Templates**: Improved the performance of the template builder.

### 2nd June 2023

* **Connectors**: Ensured that the padlock icon in the **Connector Library** appears closed when you fill all of the required authentication fields and appears open if not.
* **Dashboard**: Fixed the account reports so they show the correct values.
* **Partners**: Included incidents in task overages.
* **Performance**: Improved function of field mapping for cycles with slow bandwidth.
* **LAUNCH**: Made sure that when someone cancels an install, LAUNCH redirects them to the LAUNCH modal with the tags and other query parameters from the original LAUNCH URL.

### 19th May 2023

* **Accounts**: Allowed sub accounts to view connector method details from their parent account. 
* **Accounts**: Ensured that the **Account Concurrent Transaction Limit** provides the default value, and the upper limit on manual updates in the console when you add a new API or web account.
* **API**: Included non method steps that require setup in **Get Template**, such as `Decision`, `Delay`, and `WaitUntil`. The template install maps these prerequisites to the target account's cycle.
* **Dashboard**: Added a task allowance measure to the sidebar in the console.
* **Partners**: Included connector release version definitions on export. Ensured that on import, the application installs connector versions which don't exist on the partner account/instance. Ensured that the imported template method steps' connector versions are identical to the source template.
* **Performance**: Improved the performance of transaction reports.
* **Template builder**: Re-styled how you authenticate a connector in the builder.
* **Template builder**: Allowed you to configure Cycle steps to use authentication values you obtain externally.



### 28th April 2023

* **Console**: Improved paging for installed accounts in the console.
* **API**: Ensured that the API returns the correct field mappings for custom/copied method categories.
* **Performance**: Improved 429 HTTP response handling.
* **Connectors**: Made sure that you can delete dynamic custom fields in the console.
* **Accounts**: Removed case sensitivity from the console **User Management** search.
* **Partners**: Included connector release version definitions when you export a template. Made sure that Cyclr installs connector versions which do not exist on the instance/partner when you import a template. Ensured that the imported template method steps' connector versions are identical to the source template.
* **LAUNCH**: Added template ID, template release ID and template tag properties to the LAUNCH callback result object.
* **Marketplace**: Ensured that querystring parameters work as expected to allow authentication.
* **Marketplace**: Added the `CompleteParameter` parameter as a custom value included in Marketplace webhook callback.
* **Template builder**: Ensured that you can configure cycle steps to use authentication values that are obtained externally.
* **Documentation**: Added a Help button to the documentation site to contact the support team.

### 13th February 2023
* **Marketplaces**: Added support for naming a package at installation for packages that allow multiple installations.
* **Performance**: Addressed slowness encountered when listing dynamic custom fields.
* **Builder**: Displayed partner and account name.
* **API**: Added support for authenticating multiple partner connectors when you generate a Marketplace URI.

</section>
<section class="card">
## 2022

### 28th November 2022
* **Performance**: Improved Cycle execution performance for Cycles with lots of decision steps

### 21st November 2022
* **Performance**: Reduced latency for synchronous webhooks
* **Script**: Added HMAC-SHA512 to cyclr_sign

### 14th November 2022
* **API**: Added the ability to get and set Data Retention values for accounts
* **Script**: Made `script_parameters` accessible in ``before_oauth2_authorise``,``before_oauth2_token``, ``after_oauth2_token``, ``before_oauth2_refresh`` &amp; ``after_oauth2_refresh``

### 10th October 2022
* **API**: Included Marketplace tags in the Marketplace notifications.

### 26th September 2022
* **Recycle Bin**: Delete all option
* **Templates**: Copying a template release, can pick a folder to copy into

### 5th September 2022
* **API**: Cycle variables included in Cycle prerequisites
* **Connectors**: Auth fields can be hidden and labels customised
* **Connectors**: A new method type of Script can be used for steps that don't require API calls
* **Platform**: Deleted Cycles and Templates are now moved to a Recycle bin for 90 days before permanent deletion

### 15th August 2022
* **API**: Custom connectors can be created, updated and deleted via the API
* **Connectors**: Neo4j support has been added
* **Marketplace Notifications**: Partner user agent is included in HTTP request
* **Marketplace Notifications**: Include InstallDetails in all notifications

### 25th July 2022
* **Connectors**: Support multiple authentication types
* **Cycles**: Added 6 Hour interval

### 18th July 2022
* **Custom Fields**: Can delete custom fields in bulk
* **Custom Fields**: Support for reordering custom fields

### 11th July 2022
* **Builder**: Can hide unmapped fields in step setup
* **Reports**: Transactions can be ordered by column
* **Platform**: Improved copy/install cycle performance

### 4th July 2022
* **Platform**: Improved CSV performance and max file size
* **Platform**: Cycle error retry can be configured for between 1 and 5 retry attempts

### 27th June 2022
* **Connectors**: Can import OpenAPI 3 definitions
* **Reports**: Reports and logs can be exported from the Console

### 17th May 2022
* **Console**: Improve performance when deleting large amounts of transactions
* **Webhooks**: Webhook cleanup after step upgraded

### 10th May 2022
* **Connectors**: When a connector is de-authenticated, 3rd party webhooks are automatically deregistered

### 3rd May 2022
* **API**: Include account connector info in Template Install endpoint response
* **Builder**: Improve parent transaction identification in transactions view
* **Launch**: Display template descriptions
* **API**: Support enhanced objects
* **API**: Support template import/export
* **Platform**: Allow for authentication failure page customisation

### 25th April 2022
* **Console**: Improve transactions view with split notification and filter view by parent transaction
* **Console**: Make templates/cycles directly navigable from transactions view
* **API**: Enforce name field requirement for account creation calls
* **Launch**: Add user visible template note
* **Connector Management**: Improve method category deletion experience

### 19th April 2022
* **API**: Support cycle import and export
* **Platform**: Improve Time Filter Field errors
* **Console**: Allow partner admins to set users with private instance admin role
* **Console**: Allow private instance administrators access to scheduled jobs view
* **API**: Include account connector IDs in template install call response

### 4th April 2022
* **Connector Setup**: Indicate optional fields

### 28th March 2022
* **Marketplaces**: Enforce connector authentication order
* **Builder**: Allow partners to control help links in white label consoles

### 21st March 2022
* **Platform**: Updated MongoDB native driver to 2.14.1
* **Connectors**: Remove dynamic custom fields if no longer found at source
* **Launch/Marketplaces**: Added data type mismatch warnings
* **Templates**: Cycle variables now support value lists

### 14th March 2022
* **Custom Connectors**: Support custom objects

### 28th February 2022
* **Connectors**: Added support for Kafka connector
* **Webhooks**: Improved performance, reduces time to accept webhooks
* **Script**: Add encoding support for atob &amp; btoa

### 7th February 2022
* **Webhooks**: added support for refreshing external IDs for partner webhooks

### 17th January 2022
* **LAUNCH/Marketplace**: prevent single install packages being installed more than once

### 10th January 2022
* **Console**: Add new Search filter option to exclude errors and warnings in transactions view

### 4th January 2022
* **Console**: add Cyclr API Reference to Help menu
* **Webhooks**: support multiple IDs for partner webhooks
* **API**: include connector categories in API response



</section>
<section class="card">
## 2021

### 29th November 2021
* **Templates**: added builder annotations
* **Script**: added transaction_id script variable
* **Connectors**: added support ftps TLS session reuse
* **Console**: added messaging widget to dashboard

### 15th November 2021
* **Webhooks**: add webhook replay
* **LAUNCH/Marketplace**: enforce mapping steps order

### 8th November 2021
* **Marketplaces**: Add installing view
* **Script**: added cycle_variables to after_action_paging

### 25th October 2021
* **API**: deauthenticate endpoint to de-authenticate an account connector
* **Marketplaces**: Installing view can be enabled on Marketplaces
* **Reports**: Connector report can drill down to show accounts using the connector
* **Script**: cycle_variables avalible in after_action_paging event

### 4th October 2021
* **API**: Parameters include IsSensitive flag
* **LAUNCH/Marketplace**: Can change display text used for connectors
* **Reports**: Total Incident count added to Account and Cycle reports
* **Script**: Execution context is available from script_execution_context
* **Templates**: Template Export/Import now supports Cycle Variables

### 31st August 2021
* **Error Summarisation**: Count errors for steps that continue on error

### 23rd August 2021
- File Download/Upload for (S)FTP
* **API**: New endpoint to create/update multiple cycle variables at once

### 16th August 2021
* **Console**: New Account Connector Method Report

### 9th August 2021
* **Database Connectors**: Support SSH tunneling

### 2nd August 2021
* **API**: Get the sub accounts of an account
* **Connectors**: Improved support for custom objects in third party APIs
* **Connectors**: Improved links for non Cyclr users to authenticate connectors
* **Tagging**: Tags are now case sensitive

### 27th July 2021
* **Builder**: Display timezone with next run time
* **Builder**: new system mergefields (i.e. Account ID, Account External ID, Cycle ID and Transaction ID)

### 19th July 2021
* **Console Templates**: Allow export and import of template releases as JSON objects

### 12th July 2021
* **Corporate Partner**: Task usage warning emails as limit approached

### 5th July 2021
* **Console Reports > New Account UI**: Console report links use the new Console Account UI instead of behaving as a Sign In button

### 28th June 2021
* **Error Webhooks**: Account API (External) ID included in Error Webhooks

### 21st June 2021
* **Builder**: Can view field locations in step setup
* **Corporate Partner**: Integration Reports
* **Connectors**: Support for XML 1.1
* **LAUNCH/Marketplaces**: Templates that cannot be setup by users will not be displayed

### 14th June 2021
* **Security**: Enforce MFA for console administrators

### 7th June 2021
* **Console**: New page to access and update Partner Account details and view price plan information
* **Marketplaces**: Added auto-start option for integration packages

### 31st May 2021
* **Password Policy Update**: Cyclr console administrator passwords must now be 10 characters long and contain a non-alphanumeric character
* **Builder**: Improved performance in Cycle/Template builder
* **Marketplaces**: Action Link, Category and Integration Packages can now have HTML in there description
* **Console Dashboard Quick Actions**: Allow creating a Template or Account from the console dashboard
* **Connector > Install**: Can type a value for parameters where the options provided are not applicable
* **Account > Install Template**: Allows picking the account connectors to use for installed cycle
- New account UI for console administrators

### 17th May 2021
* **Folder breadcrumb**: added folder breadcrumb in cycle builder
* **Webhook auto update**: new Webhook Update Method. Supports webhooks with expiry if created using Webhook Create Method.

### 4th May 2021
* **Console**: Corporate edition support 

### 26th April 2021
* **Script Engine**: add `method_response_parameters_in_use` parameter for accessing response fields used in descendant cycle steps.

### 19th April 2021
* **Builder**: new Run Once option in Consonle > Template > Publish Settings.
* **API**: Account APIs allowed to have unset parameters.


</section>
<section class="card">
## 2021 and older

For release notes before 23rd February 2021, please visit [the Cyclr website](https://cyclr.com/changelog){:target="_blank"}.

</section>
