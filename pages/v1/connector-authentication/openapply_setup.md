---
title: OpenApply Connector Guide
sidebar: cyclr_sidebar
permalink: openapply-connector
tags: [connector]
---

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

## User Guide

### Custom Fields

Student and Parent objects support the use of custom fields.

The "Field Location" format for each of the supported methods is as follows:

| Method Name                     | Field Location                              | Example                            |
| :------------------------------ | :------------------------------------------ | :--------------------------------- |
| Get Parent By ID                | parent.custom_fields.<em>FieldName</em>     | parent.custom_fields.eyeColour     |
| List Parents                    | [parents].custom_fields.<em>FieldName</em>  | [parents].custom_fields.eyeColour  |
| List Updated Parents            | [parents].custom_fields.<em>FieldName</em>  | [parents].custom_fields.eyeColour  |
| Search Parents                  | [parents].custom_fields.<em>FieldName</em>  | [parents].custom_fields.eyeColour  |
| Get Student By ID               | student.custom_fields.<em>FieldName</em>    | student.custom_fields.eyeColour    |
| List Students                   | [students].custom_fields.<em>FieldName</em> | [students].custom_fields.eyeColour |
| List Updated Students           | [students].custom_fields.<em>FieldName</em> | [students].custom_fields.eyeColour |
| Search Students By Field Value  | [students].custom_fields.<em>FieldName</em> | [students].custom_fields.eyeColour |
| Search Students By Student Slug | [students].custom_fields.<em>FieldName</em> | [students].custom_fields.eyeColour |
| Search Students By Tag          | [students].custom_fields.<em>FieldName</em> | [students].custom_fields.eyeColour |

The following is a guide for adding custom fields to a method: [adding custom fields](https://docs.cyclr.com/adding-custom-fields).
