---
title: Salesforce Custom Objects
sidebar: cyclr_sidebar
permalink: salesforce-custom-objects
tags: [salesforce]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">

## Access custom objects in Salesforce

To use custom objects, you need the API name of your object. The process to find the API name is slightly different depending on whether you use Salesforce Classic or Salesforce Lightning Edition.

### Find the API name in Salesforce (Lightning)

1. Select the Setup Cog, and choose **Setup**.

    ![Salesforce Setup Cog](./images/sf_lightning_setup_cog.png)

2. Select the **Object Manager**. 
    * **Note**: You can also find the object manager in **Platform Tools** > **Objects and Fields**.

3. Find the Custom Object in the list, and note the **API Name**. For example, the format is `My_Custom_Object__C`.

### Find the API name in Salesforce (Classic)

1. Select **Setup**.
2. In the left navigational menu, go to **Build** > **Create** > **Objects**.
3. Find and select the Custom Object in the list.
4. Note the **API Name** of the object on the next screen. For example, the format is `My_Custom_Object__C`.

### Using the Custom Object in Cyclr

1. Open the Salesforce Connector **settings**.

    ![Salesforce Connector Settings](./images/sf_settings.png)

2. From the **Custom Objects** > **Utilities** sub-category, run **List Object Fields**, and pass in the **API Name** of your object.

3. Copy the list of field names from the response.

    ![Salesforce Example Object Fields](./images/sf_fields.png)

4. Select the custom object (from 1-3) that you want to use. For example, you can use the **Custom Objects** > **Object 1** method group to set up access.

5. Run the **List Records 1** method. Pass the API Name as the **Object Name**, and the field list that you previously copied into the **Fields** box. This provides you with a sample of data in the object.

6. Once the method has run, scroll down to the **Method Response** section of the results and copy it.

    ![Salesforce Example Object Fields](./images/sf_method_response.png)

7. On the method, switch tabs from **Test** back to **Fields**.

8. Select the magnifying glass to bring up the **Generate Fields** window, paste in the response from step 6, and select **Generate**.  This adds all the required fields to your List Records method.

9. Repeat steps 5-8, but with using the method **Get Record By ID 1**.  If you need an ID to use here, you can run **List Records** again to find it.
</section>