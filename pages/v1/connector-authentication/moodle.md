---
title: Moodle Authentication
sidebar: cyclr_sidebar
permalink: moodle-connector
tags: [connector]
---

## Partner Setup

To authenticate the Moodle connector you will need an `API Token`. This is obtained by setting up an application within your Moodle environment.

### Setting up an application in Moodle

Navigate to `Site Administration > Plugins > Web Services`

Start following the guide for "Allow an external system to control Moodle" (Pictured below).

![](./images/moodle0.png)

The only protocol you will need to enable in *Step 2* is `REST`.

After creating your specific user in *Step 3*, you will need to create and assign a role to this user. Follow these steps to do this.

Navigate to `Site Administration > Users > Permissions > Define Roles`

Scroll to the bottom of the page, and click "Add a new role". The Manager archetype is recommended. 

After the first step you will reach a page that allows customisation of this role; the part we are interested in sits at the bottom of the page (Pictured below).
![](./images/moodle3.png)

You must enable all the capabilities listed in the table below. Copying and pasting is recommended to save time. Once this is done click "Create this role".

| User Capability    |
| ------------------ |
| moodle/course:view |
| moodle/course:update |
| moodle/course:viewhiddencourses |
| moodle/course:managegroups |
| moodle/user:create |
| moodle/user:viewdetails |
| moodle/user:viewhiddendetails |
| moodle/course:useremail |
| moodle/user:update |
| enrol/manual:enrol |
| moodle/grade:view |

You now need to assign this role to the user. To do this you need to navigate to `Site Administration > Users > Permissions > Assign system roles`

Click the role you have just created, and then on the next page assign the user.

For *Step 6* you will need to enable the following functions to be able to use all Cyclr methods:

| Service Functions               |
| ------------------------------- |
| core_group_add_group_members    |
| core_group_assign_grouping      |
| core_group_create_groupings     |
| core_group_create_groups        |
| core_group_delete_group_members |
| core_group_delete_groupings     |
| core_group_delete_groups |
| core_group_get_activity_allowed_groups |
| core_group_get_activity_groupmode |
| core_group_get_course_groupings |
| core_group_get_course_groups |
| core_group_get_course_user_groups |
| core_group_get_group_members |
| core_group_get_groupings |
| core_group_get_groups |
| core_group_unassign_grouping |
| core_group_update_groupings |
| core_group_update_groups |
| enrol_manual_enrol_users |
| enrol_manual_unenrol_users |
| core_course_get_courses |
| core_user_create_users |
| core_user_get_users |
| gradereport_overview_get_course_grades |
| core_auth_request_password_reset |

Once the Moodle Web Service application has been created, you need to create a token, selecting the user with the above permissions, and the newly created service (Pictured below).

![](./images/moodle1.png)

![](./images/moodle2.png)

Copy this token, and use it to authenticate in Cyclr.
