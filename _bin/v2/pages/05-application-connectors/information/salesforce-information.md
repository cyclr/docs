---
title: Salesforce Information
sidebar: cyclr_sidebar
permalink: salesforce-information
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
## Additional information

### Webhook Setup
#### Add Webhook class to SalesForce account
* Login into your Salesforce Account, navigate to the top right corner and click the **Clog** icon, then click **Setup**.
* Navigate to the left panel, scroll down and click **Custom Code**, then click **Apex Classes**
* Create a new **Apex Class** by clicking **New**
* Name it **Webhook** and paste the following code snippet:

```javascript
  public class Webhook implements HttpCalloutMock {

    public static HttpRequest request;
    public static HttpResponse response;

    public HTTPResponse respond(HTTPRequest req) {
        request = req;
        response = new HttpResponse();
        response.setStatusCode(200);
        return response;
    }

    public static String jsonContent(List<Object> triggerNew, List<Object> triggerOld) {
        String newObjects = '[]';
        if (triggerNew != null) {
            newObjects = JSON.serialize(triggerNew);
        }

        String oldObjects = '[]';
        if (triggerOld != null) {
            oldObjects = JSON.serialize(triggerOld);
        }

        String userId = JSON.serialize(UserInfo.getUserId());

        String content = '{"new": ' + newObjects + ', "old": ' + oldObjects + ', "userId": ' + userId + '}';
        return content;
    }

    @future(callout=true)
    public static void callout(String url, String content) {

        if (Test.isRunningTest()) {
            Test.setMock(HttpCalloutMock.class, new Webhook());
        }

        Http h = new Http();

        HttpRequest req = new HttpRequest();
        req.setEndpoint(url);
        req.setMethod('POST');
        req.setHeader('Content-Type', 'application/json');
        req.setBody(content);

        h.send(req);
    }

}
```
####  Add Service Domain
* Go to your Cyclr console, click **Setings** and **General Settings**
* Copy your **Service Domain**  
* Login into your Salesforce Account, navigate to the top right corner and click the **Clog** icon, then click **Setup**.
* Navigate to the left panel, scroll down and click **Security**, then click **Remote Site Settings**
* Click **New Remote Site** and give it a name and add your **Service Domain** from the second step.

Now your account is set and ready to use webhooks in your account.

### Enduser Salesforce Account Setup

For the best experience when using the Salesforce Connector, and to reduce the frequency at which Cyclr must obtain a new Access Token and avoid some connection issues, ensure the following Session Settings have been set:

Log in to the Salesforce organization, go to Setup, then use the Search to find "Session Settings".

Under **Session Timeout**
*  Timeout Value: set this for as long as possible, e.g. 24 hours.
*  Force logout on session timeout: disable this.

Under **Session Settings**
*  Lock sessions to the IP address from which they originated: disable this.

### Disabling Assignment Rules

When creating Accounts, Cases, or Leads in Salesforce, it may be desirable to prevent Salesforce's "active assignment rules" from being applied.  This very much depends on what assignment rules have been setup within Salesforce so will depend on the enduser's requirements.

To prevent assignment rules from being applied, add this Script to a Salesforce step in the Cycle Builder:

```javascript
function before_action() {
    // Don't apply Salesforce's assignment rules.
    method_request_headers['Sforce-Auto-Assign'] = 'FALSE';

    return true;
}
```
[More information](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/headers_autoassign.htm)

### Working with CSV documents

To retrieve the contents of a CSV document, you will need to take the following steps:

1. Find the Document ID.  This can be found in the response you recieved when you made the file, or by running "List Content Documents".
2. Use this ID in a "Get Content Version" call to get the Content Version ID.
3. Enter the Content Version ID in a "Get Content Document Data (CSV)" call.
4. You will need to add the fields within connector settings so that you can map them.  The field location will be '[].yourcolumname' without quotes.

</section>
