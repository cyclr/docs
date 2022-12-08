---
title: Google Classroom - Workspace Authentication
sidebar: cyclr_sidebar
permalink: google-classroom-workspace-connector
tags: [connector]
---

# Google Workspace Setup

> Note: Due to how Google Classroom authentication works, clients themselves will need to follow the Google Workspace setup process described below.

To allow the Google Classroom connector to manage Google classrooms within your workspace, you need to do the following:

1. Enable the Google Classroom API for a project within your workspace.
2. Create a service account.
3. Enable domain-wide delegation for the service account and set the correct scopes.

## Enabling the Google Classroom API

To access the Google Classroom API endpoints, you need to enable the Google Classroom API within a project in your workspace. Google's documentation on how to do this can be found [here](https://support.google.com/googleapi/answer/6158841?hl=en).

## Creating a service account

A service account needs to be created to allow admin-level access to Google classrooms within your workspace. Google's documentation on how to do this can be found [here](https://developers.google.com/identity/protocols/oauth2/service-account#creatinganaccount). When creating the service account, set up the fields below as follows:

-   **Grant this service account access to project**: Set the service account role to **Owner**.
-   **Grant users access to this service account**: Set the **Service account admins role** field to any users that will be administering the service account.

Make note of the **OAuth 2 client ID** and **Email** for your service account. You will need these to enable domain-wide delegation and to authorize your account with Cyclr. You can find this on the [service accounts page](https://console.developers.google.com/iam-admin/serviceaccounts).

When adding the service account key, set the **Key type** to JSON, then open the downloaded .json key file and make note of the **private_key** field. You need this to authorize your account with Cyclr.

## Enabling domain-wide delegation for your service account

Domain-wide delegation needs to be enabled for your service account to allow it to access user data on behalf of users in your workspace. You need to be a "super administrator" of the workspace to configure this. Google's documentation on how to do this can be found [here](https://developers.google.com/identity/protocols/oauth2/service-account#delegatingauthority). When enabling domain-wide delegation, set up the fields below as follows:

-   **Client ID**: Set to the **OAuth 2 client ID** from the previous section.
-   **OAuth scopes (comma-delimited)**: Add the following scopes as a comma separated list:
    -   **https://www.googleapis.com/auth/classroom.courses** for course access.
    -   **https://www.googleapis.com/auth/classroom.coursework.students.readonly** for coursework access.
    -   **https://www.googleapis.com/auth/classroom.rosters** for student and teacher access.
    -   **https://www.googleapis.com/auth/admin.directory.user** for workspace user access.

# Cyclr Setup

## Client installation

When using a template containing the Google Classroom connector, clients will be prompted for the following information from the previous sections:

-   **Private Key**: The **private_key** field from the .json key file.
-   **Client Email**: The **Email** address of your service account.
-   **Administrator Email**: The email address of the user for which the application is requesting delegated access. This should be the email of the administrator of the Workspace account.
-   **Scopes**: The required scopes. These must match the scopes set for the service account in the previous section. **Full access** is required for all methods to function.

## Partner templates

To setup the Google Classroom connector within a template:

1. Go to the **Cyclr Console**.
2. Click the **Templates** dropdown menu at the top of the page.
3. Click **Template Library**.
4. Click **Design New Template** and enter a **Template Name** to create a new template, or click **Edit Most Recent Draft** to change an existing template.
5. Click **+Add Application** in the right hand menu.
6. Use the search bar to find the **Google Classroom** connector and click **Install**.
7. Change the **Name** and **Description** as required and click **Next**.
8. Enter the following values from the previous sections:
    - **Private Key**: The **private_key** field from the .json key file.
    - **Client Email**: The **Email** address of your service account.
    - **Administrator Email**: The email address of the user for which the application is requesting delegated access. This should be the email of the administrator of the Workspace account.
    - **Scopes**: The required scopes. These must match the scopes set for the service account in the previous section. **Full access** is required for all methods to function.
9. Click **Next**.

Your Google Classroom connector is now setup! You can test it by running a method within the template it's installed in to confirm it returns data.
