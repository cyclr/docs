---
title: Create account, install template, and run a cycle
sidebar: cyclr_sidebar
permalink: create-account-and-install-template
tags: [examples]
menus:
    api-examples:
        title: Create account and install template
        identifier: create-account-and-install-template
        weight: 1
---
{::options parse_block_html="true" /}
<section class="card py-5 my-5">
This document describes how to approach the following use case via API calls 

1. Creating an Account
2. Installing a Template into it
3. Authenticating the Connector
4. Setting the Step Field Mapping

Note: Throughout this document, the domain used in the example requests is ```api.cyclr.com```.

If you are on the UK instance, this should be replaced with ```api.cyclr.uk```, and for the EU, ```api.eu.cyclr.com```.


</section>
<section class="card py-5 my-5">
## 1. Create Account

```curl
curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d  '{ \ 
 "Id": "(Optional) The External Account ID you would like for this account", \  "Name": "Account Name", \ 
 "Description": "(Optional) Account Description", \ 
 "Timezone": "(Optional) Timezone for the account, IANA time zone database format.", \  }' 'https://api.cyclr.com/v1.0/accounts'
 ```

See **Create Account** docs for more details: [Click Here](/create-account)


</section>
<section class="card py-5 my-5">
## 2. Install template into new account

```curl
curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -- header 'X-Cyclr-Account: ACCOUNT ID FROM PREVIOUS STEP' -d '{ \  }' 'https://api.cyclr.com/v1.0/templates/TEMPLATE-ID/install'
```

Depending on the template being installed, there may be more to specify in this call, but this is the minimum.

See **Install a Template** docs for more details: [Click Here](/install-from-template)



</section>
<section class="card py-5 my-5">
## 3. Authenticate connector (OAuth)

### 3a. Get Sign-in Token

```curl
curl -X POST --header 'Content-Type: application/json' --header 'Accept:  application/json' -d '{ \
"Username": "string" \ 
 }' 'https://api.cyclr.com/v1.0/accounts/ACCOUNT ID FROM STEP 1/signintoken'
```

### 3b. Update Connector Auth

```curl
curl --request POST \
  --url 'https://YOUR-SERVICE-DOMAIN/connectorauth/updateaccountconnectoroauth?id=ACCOUNT CONNECTOR ID FROM STEP 2&token=TOKEN-FROM-STEP-3a&targetOrigin=https://www.cyclr.com'
```

Your service domain can be found by visiting General Settings in your Cyclr console.  It generally has a format matching one of the following:

* mycompany-h.cyclr.com
* mycompany-h.eu.cyclr.com
* mycompany-h.cyclr.uk

``targetOrigin`` should be either the origin of another browser window for the  JavaScript callback event to be dispatched to, or a URL to redirect the user to.

See our docs for more on authenticating via OAuth: [Click Here](/oauth-authentication).  Documentation for other auth routes is also available.


</section>
<section class="card py-5 my-5">
## 4. Set Step Field Mapping

```curl
curl -X PUT --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'X-Cyclr-Account: ACCOUNT ID FROM STEP 1' -d '{ \ 
     "Field": { \ 
         "Id": 0 \ 
     }, \ 
     "MappingType": "StaticValue", \ 
     "Value": "string" \ 
 }' 'https://api.cyclr.com/v1.0/steps/STEP-ID-FROM-STEP-2/fieldmappings/FIELD-ID-FROM-STEP-2'
```

See **Set Step Field Mapping** in our documentation for more details: [Click Here](/set-step-field-mapping)


</section>
<section class="card py-5 my-5">
## 5. Start Cycle

```curl
curl -X PUT --header 'Content-Type: application/json' --header 'Accept: application/json' -- header 'X-Cyclr-Account: Account ID' -d '{ \ 
 "StartTime": "2021-12-07T09:17:50.888Z", \ 
 "Interval": 0, \ 
 "RunOnce": true \ 
 }' 'https://api.cyclr.com/v1.0/cycles/Cycle ID/activate'
```

See **Cycle Activation** for more details: [Click Here](/cycle-activation)

</section>
