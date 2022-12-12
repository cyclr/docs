
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content required" markdown="1">

To authenticate the Bullhorn connector you  need a ``Client ID`` and ``Client Secret``.  

Contact with Bullhorn Support to obtain these credentials.

If asked for a callback URI during this process, give

https://``Your Service Domain``/connector/callback 

Your service domain can be found in your Cyclr console under ``Settings > General Settings > Service Domain``.

</div>

</section>

<section class="setup partner" markdown="1">

## FAQ

<div class="section-content" markdown="1">

### Apache Tomcat Error

After you are redirected to Bullhorn during the authentication process, sometimes Bullhorn displays an Apache Tomcat error like this:

![Bullhorn Redirect Error](./images/bullhorn-redirect-error.png)

This is a known issue with Bullhorn. Either clear the Bullhorn cookies in your browser, or open Cyclr and authenticate the connector in a private window.

</div>

</section>

<section class="setup partner" markdown="1">

## User Guide

<div class="section-content" markdown="1">

### Retrieving Custom Objects

> Note: This currently only applies to the Job Order methods

To retrieve custom object fields with your Job Order requests the steps to do so are:

1. Find the fields of the custom object using the method Job Orders > Get Custom Object Fields

   ![Custom Object Fields](./images/bullhorn_cf_1.png)

2. Add the fields of the custom object to the desired method with
   - Field Location [data].**CustomObjectName**.[data].**FieldName** for List New Job Orders or List Updated Job Orders
   - data.**CustomObjectName**.[data].**FieldName** for Get Job Order. For Example (with List New Job Orders):

   ![Add Custom Fields](./images/bullhorn_cf_2.png)
   
3. Add the custom object name and field names to the Custom Objects parameter when making the request. The format must be ObjectName(FieldName,FieldName,FieldName). For example:

   ![Add Query](./images/bullhorn_cf_3.png)

</div>

</section>
