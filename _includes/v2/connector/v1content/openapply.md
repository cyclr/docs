
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

To authenticate the OpenApply connector you need a :
- Client ID
- Client Secret
- your account name

### Client ID & Client Secret

To get your `Client ID` and `Client Secret`, within your OpenApply account:

1. Go to **Settings** and open the **Public API** page where you want to add a new application

2. Find your `Client ID`, `Client Secret`, and` Redirect URI` on this page

> Redirect URI should be `https://{{Your Cyclr service domain e.g. app-h.cyclr.com}}/connector/callback`

### OpenApply Account (name)

Your OpenApply account is displayed in your account URL. 

For example, if your account URL is `https://demo.openapply.com`  your account name is `demo`.

</div>

</section>

<section class="setup cyclr" markdown="1">

## Cyclr Setup

<div class="section-content" markdown="1">

1. Go to your Cyclr Console
2. Go to **Connectors** > **Connector Library**
3. Find the **OpenApply** connector
2. From the **Edit Connector** interface click **Setup**
3. Enter your `Client ID`, `Client Secret` and `OpenApply Account Name`
4. click **Next**

The connector is now authenticated and ready to use.

</div>

</section>

<section class="userguide" markdown="1">

## User Guide

<div class="section-content" markdown="1">


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


</div>

</section>
