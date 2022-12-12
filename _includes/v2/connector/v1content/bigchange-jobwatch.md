
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

### API Key

Contact your customer service representative to get your BigChange JobWatch API Key.
# Cyclr setup

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

To set up the BigChange JobWatch connector within Cyclr:

1. Go to your **Cyclr Console**.
2. Click the **Connectors** dropdown menu at the top of the page.
3. Click **Application Connector Library**.
4. Use the search bar to find the BigChange JobWatch connector.
5. Click the **Setup Required** button.
6. Enter the following values:
    - **API Key**: Your BigChange JobWatch API key you obtained in the previous section.
    - **Username**: Your BigChange JobWatch username.
    - **Password**: Your BigChange JobWatch password.
7. Click **Next**.

Your BigChange JobWatch connector is now set up! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.

</div>

</section>

<section class="other" markdown="1">

## Custom fields

<div class="section-content" markdown="1">

### Methods with custom fields

Add custom fields to contacts, contact notes, and jobs in the following methods:

-   Create Contact
-   Update Contact
-   Update Contact Note
-   Create Job
-   Update Job

View custom fields for contacts, contact notes, and jobs in the following methods:

-   Get Contact
-   Get Contact Note
-   Get Job
-   List Contact Notes
-   List Contacts
-   List Group Jobs
-   List Jobs
-   List Jobs by Contact
-   Search Contacts
-   Search Contacts By Email
-   Search Contacts By Email, ID, Or Reference
-   Search Contacts By Phone Number
-   Search Contacts By Postcode

### How to add custom fields

1. Go to the **Edit Connector** page for the BigChange JobWatch connector.
2. Under the **Methods & Fields** heading, locate the required method by expanding out the categories and method name.
3. Click the pink **+** button to add a method field.
4. Rpeating these steps for each BigChange JobWatch custom field:
    - **Field Location**: The custom field location, which must have the format ``cust\_&lt;field name&gt;``.
    - **Display Name**: The custom field display name.
    - **Description**: The custom field description.
    - **Data Type**: Text.
5. Click **Create**.

**NB** The **Field Location** ``cust\_&lt;field name&gt;`` value must match an existing field name.

### Custom fields enabled

To confirm that custom fields are enabled, drag the required method(s) into a cycle and view  the **Step Settings**. 

The custom fields are displayed at the bottom of the **Mappings** list.

</div>

</section>