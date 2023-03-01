---
title: Salesforce information
sidebar: cyclr_sidebar
permalink: salesforce-information
tags: [connector-information]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Webhook Setup

### Add Webhook class to SalesForce account
1. Log in into your Salesforce Account, navigate to the top right corner, select the **Clog** icon, and select **Setup**.
2. Navigate to the left panel, scroll down and select **Custom Code**, and then **Apex Classes**
3. Select **New** to create a new **Apex Class**.
4. Name the class **Webhook** and paste the following code snippet:

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
###  Add service domain

To add a service domain, go to your Cyclr console:

1. Go to **Settings** > **General Settings**
2. Copy your **Service Domain**.  
3. Login into your Salesforce Account, navigate to the top right corner and click the **Clog** icon, then click **Setup**.
4. Navigate to the left panel, scroll down and click **Security**, then click **Remote Site Settings**
5. Select **New Remote Site**, enter a name and add your **Service Domain** from step 2.

</section>
<section class="card">

## End user Salesforce Account Setup

For the best experience when using the Salesforce Connector, and to reduce the frequency at which Cyclr must obtain a new Access Token and avoid some connection issues, you need to set specific session settings.

Log in to the Salesforce organization, go to **Setup**, then use the Search to find **Session Settings**.

Under **Session Timeout**
*  **Timeout Value**: Set this for as long as possible, for example, 24 hours.
*  **Force logout on session timeout**: Disable this setting.

Under **Session Settings**
*  **Lock sessions to the IP address from which they originated**: Disable this setting.

</section>
<section class="card">

## Disable assignment rules

When you create **Accounts**, **Cases**, or **Leads** in Salesforce, you can prevent the application of Salesforce's **active assignment** rules. This depends on what assignment rules are setup within Salesforce and the enduser's requirements.

To prevent the application of assignment rules, add this Script to a Salesforce step in the Cycle Builder:

```javascript
function before_action() {
    // Don't apply Salesforce's assignment rules.
    method_request_headers['Sforce-Auto-Assign'] = 'FALSE';

    return true;
}
```
[More information](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/headers_autoassign.htm)

</section>
<section class="card">

## Work with CSV documents

You can use Cyclr to retrieve the contents of CSV documents:

1. Find the Document ID in the response you recieve when you make the file, or by run **List Content Documents** to retrieve the Document ID.
2. Use the Document ID in a **Get Content Version** call to get the Content Version ID.
3. Enter the Content Version ID in a **Get Content Document Data (CSV)** call.
4. Add the fields within connector settings so that you can map them. Enter the field location in the format `[].{yourcolumname}`

</section>
