---
title: Velocify Authentication
sidebar: cyclr_sidebar
permalink: authenticate-velocify
tags: [connector]

---

## Authentication ##

Velocify uses basic authentication so all you need to do is to provide a valid username/password combination for your account.

## Creating Leads in Velocify

In order to create leads using the Velocify connector there are a few preliminary steps to be undertaken first:

1. Find and run the *List Fields* method.

2. Once successfully run you should have an XML object containing all the fields that you can use.

3. Get the details of the fields you wish to use in the *Create Lead* method.

4. In connector testing add the fields you wish to use to the connector in the following format: `soapenv:Envelope.Field_ID_#` where `#` is the ID of the field you wish to interact with e.g. if the First Name field had an ID of 1 then the *Field Location* you would create would be `soapenv:Envelope.Field_ID_1`, and it would be best to set the *Display Name* to `First Name`.
![](./images/velocify_custom_field.png)

5. Repeat step 4 for every field you wish to have access to, and you're ready to start creating leads.
