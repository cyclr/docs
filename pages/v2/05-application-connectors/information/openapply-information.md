---
title: OpenApply Connector Guide
sidebar: cyclr_sidebar
permalink: openapply-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">
## Custom Fields

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

</section>
