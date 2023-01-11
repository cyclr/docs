
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

First you will need the API name of your object.  The process of finding this is slightly different depending upon whether you use Salesforce *Lightning Edition* or Salesforce *Classic*.

### Finding the API name in Salesforce (Lightning)

1. Click the Setup Cog, and choose **Setup**.

    ![Salesforce Setup Cog](./images/sf_lightning_setup_cog.png)

2. Select the Object Manager. (This can be also be found under **Platform Tools** > **Objects and Fields**)

3. Find the Custom Object in the list, and identify its **API Name**.  This will be something like `My_Custom_Object__C`.

### Finding the API name in Salesforce (Classic)

1. Select **Setup**
2. In the left navigational menu, select **Build** > **Create** > **Objects**
3. Find the Custom Object in the list, and select it by clicking its name.
4. In the next screen you will see the object's **API Name**.  This will be something like `My_Custom_Object__C`.

### Using the Custom Object within Cyclr

1. Access Connector Settings for the Salesforce Connector.

    ![Salesforce Connector Settings](./images/sf_settings.png)

2. From the **Custom Objects** > **Utilities** sub-category, run **List Object Fields**, passing in the API Name of your object.

3. Copy the list of field names from the response.

    ![Salesforce Example Object Fields](./images/sf_fields.png)

4. Select which of the three available custom objects numbered 1-3 will be used for this object.  If for example you choose 1, use the **Custom Objects** > **Object 1** method group to set up access.

5. Run the method **List Records 1**, passing the API Name as the **Object Name**, and the field list that you previously copied into the **Fields** box.  This will provide you with a sample of data in the object.

6. Once this has run scroll down to the Method Response section of the results and copy it.

    ![Salesforce Example Object Fields](./images/sf_method_response.png)

7. On the method, switch tabs from **Test** back to **Fields**.

8. Click the magnifying glass to bring up the **Generate Fields** window.  Paste the response from step 6 in here and click **Generate**.  This will add all the required fields to your List Records method.

9. Repeat steps 5-8, this time using the method **Get Record By ID 1**.  If you need an ID to use here, you can find one by running **List Records** again.

</div>

</section>
