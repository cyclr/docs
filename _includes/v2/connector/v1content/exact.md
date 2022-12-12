
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

Register an app with Exact to get the `Client ID` and `Client Secret`.

1. Go to the [Exact Online App Centre](https://apps.exactonline.com/gb/en-gb/V2)
2. From the country menu in the upper right corner of the website, select the preferred language
3. Be aware that selecting a country defines the Exact Online website
4. Click *Login*
5. Enter your user name and password and click *Login*
6. When you are authenticated you will be redirected to the App Centre
7. Click *Manage my apps*
8. Click one of the options:

    - *Register for a testing app*: Your app is not visible in the App Centre and is not available to external clients
  
    - *Register a production app*: Your app is visible and available to external clients, you can publish your  app in the App Centre, subject to your partner manager approval

9. Enter a unique app name 

   >A unique SEO name is automatically generated for the app name. The name of the app you create is unique per country, so an app may have same name across multiple countries.
  
10. For Redirect URI enter: `https://{{ServiceDomain}}/connector/callback` , subsitute your service domain for ServiceDomain
    
    >Go to your Cyclr Console  Settings > General Settings > Service Domain to find your ServiceDomain, e.g. yourcompany.cyclr.com

11. Scroll down to find your `Client ID` and `Client Secret`. Use these to authenticate your Exact connector.

See the [Exact OAuth docs](https://support.exactonline.com/community/s/knowledge-base#All-All-DNO-Content-oauth-eol-oauth-devstep1) for more information.

</div>

</section>
