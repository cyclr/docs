---
title: README
permalink: README
sidebar: cyclr_sidebar
---
# Cyclr Documentation v2

You can use the [editor on GitHub](https://github.com/cyclr/docs/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

## Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing.

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Kramdown

Kramdown is the default Markdown renderer for Jekyll.

See the [Kramdown documentation for more info](https://kramdown.gettalong.org/index.html).

#### HTML parsing

Add this option to the md file to enable HTML parsing.  
``
{::options parse_block_html="true" /}
``

See the [Kramdown documentation for more info](https://kramdown.gettalong.org/parser/kramdown.html).

By default, the Kramdown parser does not convert HTML tags to native representation. Enabling this option means we can use HTML tags in the md. This is useful to provide container or content elements with attributes (class,id) in order to implement the required style and UX.

Amend v1 markdown to include the relevant html eg:
- The 'Required' sections : green left border, grey background with drop shadow, exclamation mark icon 
- The code sections : dark grey left border, grey background with drop shadow, 'C' icon 

## Setting up your GitHub Pages site locally with Jekyll

1. If you don't have Docker installed, install [Docker](https://docs.docker.com/install/).
2. Open the terminal.
3. On your local computer, clone the Git repository for Cyclr Documentation:
```Shell
$ git clone https://github.com/cyclr/docs.git
```
4. Install [Ruby](https://www.ruby-lang.org/en/documentation/installation/)
5. Run bundle install to install all dependencies
6. Start up the application:
```Shell
$ docker-compose up
```

## Gems and plugins
See the Gemfile and \_config.yml for plugins.
 
| plugin | github |
| --- | --- |
| jekyll-seo-tag | https://github.com/jekyll/jekyll-seo-tag |
| jekyll-redirect-from | https://github.com/jekyll/jekyll-redirect-from |
| jekyll-toc | https://github.com/toshimaru/jekyll-toc |
| jekyll-menus | https://github.com/forestryio/jekyll-menus |


## Sidebar Menu
The sidebar menu is implemented with the jekyll-menus plugin. This relies on front matter, any pages which don't have the required front matter are omitted from the menu.

See https://github.com/forestryio/jekyll-menus for details.

This implementation includes customisations :

| customisation | where | description |
| --- | --- | --- |
| externalurl | front matter | Use externalurl instead of url to open the page in a new tab or window |
| toggleonly | front matter | Add toggleonly: true if the front matter is used to provide a toggle to control a nested menu. For those items, the md file includes front matter only, with no other content  |
| menu object parse | \_includes/generic/menu.html | Renders a link with no href to provide the toggle for the submenu display |


## Pages and front matter

All v2 pages are defined in the pages/v2 folder.
The pages should be organised in sub folders which reflect the relationship between pages and group them logically. 

The folder structure reflects the sidebar menu structure.

Note that the menu struture is managed via the front matter in each md file, not via the page/v2 structure.

This allows for the displayed menu options to be managed via front matter:
- menu text
- menu option behaviour: toggle submenu or page link
- link type: same browser window or new window

The numeric prefix is used to control the order in which the options are displayed. The jekyll-menus plugin builds the data object from the md front matter, appending the relevant data from each file to its arrays. Amend the numeric prefixes to achieve the required menu option order.

### Omit page from menu
To prevent a page appearing as a menu item, remove the 'menus' item and its children from the front matter. 

### index.md
This provides the front matter for each sub menu.

#### No content
When the page md is defined to provide a submenu toggle

| item | description |
| --- | --- |
| [parentmenuid] | child of the menus front matter item - this defines the immediate parent of this page |
| title | The menu item text  |
| identifier | this menu id - to be used as the [parentmenuid] in any child pages |
| weight | can be used to control menu item order |


## Categories and Application Connector Guides

### Demo content

Copy the **Authentication** and **Documentation** from the ``_data/connector/contentdemo.json`` file to any 
``_data/v2/connectors`` json file and build.

The demo json objects are parsed in ``_includes/v2/connector/connector.html`` to provide content with the relevant style. 


### V1 connector content
The content from the first version has been ported to v2 using the **\_bin/v2/portconnectormdtov2.py** script
The script copies the md files from the **pages/connector-authentication/** folder to **\_includes/v2/connector/v1content/**, and discards the front matter as the md is not to be built into standalone pages. 

This content is included where available to provide the connector setup and auth details.  It is intended that this content will be replaced once fields have been added to the connector database, and populated with the required content. The connector API response will be modified to include all the connector setup and other content.


#### Name discrepancies 
The version 1 content was added manually and there are many discrepancies in the file naming conventions. Some files are camel case, some are slugified using hyphens, some use suffixes such as \_doc or \_setup.

As the naming is arbitary, the python script includes  a manually maintained lookup ``md_dict`` to map from the original name to the corresponding slugified conenctor name.

The ``md_dict`` is defined at the top of **portconnectormdtov2.py**. 


| v1 md filename| v2 md filename |
| --- | --- | 
| 3DCart | 3dcart |
| access_crm_setup | access-crm |
| adestra_setup | adestra |
| Amadeus | amadeus |
| appdirect-connector | appdirect |
| aws-ec2 | amazon-ec2 |
| aws-s3 | amazon-s3 |
| azure_ad_connector_docs | azure-ad |
| azure-devops-connector | azure-devops |
| bamboohr_setup | bamboohr |
| bntouch_docs | bntouch-mortgage-crm |
| breathehr | breathe-hr |
| calendly_setup | calendly |
| CampusIvy | campusivy |
| Cardpointe | cardpointe |
| casavi_setup | casavi |
| Cavelo | cavelo |
| chargifyadmin | chargify |
| choosing_dynamics | choosing-dynamics |
| clicksend | clicksend-sms |
| clubready | club-ready |
| CoinGecko | coingecko |
| deltek_workbook | deltek-workbook |
| disciple_media | disciple-media |
| doc_360_readme | document-360 |
| engagement_multiplier_docs | engagement-multiplier |
| envision | envision-salon-spa |
| facebook-marketing | facebook-marketing-api |
| FluentCommerce | fluentcommerce |
| Follow-Up-Boss | follow-up-boss |
| foodtec_docs | foodtec |
| GoCardless | gocardless |
| GoDaddy | godaddy |
| Google_Analytics | google-analytics |
| google-calendar-workspace | google-calendar |
| gym_sales | gym-sales |
| High Level | high-level |
| infusionsoft_docs | infusionsoft |
| insider | insider |
| installing-bronto | bronto |
| instantco | instant-co |
| intelliflo_setup_guide | intelliflo |
| JobNimbus | jobnimbus |
| jotform_setup | jotform |
| less_annoying_crm_docs | less-annoying-crm |
| liana_cms_docs | liana-cms |
| listrak-rest | listrak |
| LiveForce | liveforce |
| magento_2_webhooks | magento-2-webhooks |
| Mailkit | mailkit |
| marketo_import_export | marketo |
| Marketron | marketron |
| MemoQ | memoq |
| microsoft_education | microsoft-education |
| mondaydotcom_setup | monday-com |
| netsuite_suitetalk_rest_setup | netsuite-suitetalk |
| openapply_setup | openapply |
| opencrm_setup | opencrm |
| petexec_setup | petexec |
| PhoneBurner | phoneburner |
| podio_docs | podio |
| ProfitWell | profitwell |
| retail_express | retail-express |
| rockgympro | rock-gym-pro |
| rybbon_setup_docs | rybbon |
| sage50 | sage-50 |
| sage50cloud | sage-50-cloud |
| salesforce_chatter | salesforce-chatter |
| Salesforce_External_ID_Setup | salesforce-external-id |
| salesforce_marketing_cloud | salesforce-marketing-cloud |
| salesforce_meta_setup | salesforce-meta |
| salesforce_pardot | salesforce-pardot |
| salesforceSoap | salesforce-soap |
| Salesloft | salesloft |
| salesnexus_docs | salesnexus |
| sap_successfactors | sap-successfactors |
| service_monster_setup | servicemonster |
| service_now_docs | servicenow |
| serviceminder | serviceminder-io |
| shireburn_docs | shireburn |
| shopify_oauth | shopify-oauth |
| spark_connector_setup | spark_membership |
| spotme_docs | spotme |
| SproutSend | sprout-send |
| stripe_oauth | stripe |
| superphone_docs | superphone |
| tazworks_setup | tazworks |
| Tenstreet | tenstreet |
| Totango | totango |
| trustpilot_readme | trustpilot |
| twiliovoice | twilio-voice |
| Unbounce | unbounce |
| userdotcom_docs | user-com |
| Velocify | velocify |
| Vincere | vincere |
| vonage_docs | vonage |
| Voucherify | voucherify |
| Voyado | voyado |
| xero_oauth20 | xero-oauth20 |

#### Redundant v1 content
Once new and consitent content is available and has been reviewed and signed off, remove the v1 content from **\_includes/v2/connector/v1content/**. As **portconnectormdtov2.py** provides the option to recover the v1 content at any time, it's not an issue if the content has been deleted but must be reinstated.  

### Build process

The Category Connector pages are created using python scripts and API calls. 
The scripts are in **\_bin/v2/**, with md and other templates in the **\_bin/v2/assets/** folder

Install python (https://www.python.org/downloads/) and the required libraries (pip install \[library\])
- requests
- slugify
- re
- os
- arr
- glob
- json


If existing connector content is to be rebuilt. it's advisable to stop any running docker/jekyll processes which watch the relevant source folders.
Delete the existing md files from the **pages/v2/04-application-connector-guides/** folders, backing up to an archive folder if required.

#### getcategories.py

Creates the md files for each connector category . The md files provide the source for the category hub pages, where tiles act as links to the individual connectors associated with the category.

- Makes API call https://my.cyclr.com/api/categories
- Parses the returned JSON array:
  - copies **\_bin/v2/assets/templatecategory.md** to **pages/v2/04-application-connector-guides/category-name-slugified.md**
  - copies **\_bin/v2/assets/templatecategory.yml** to **\_data/v2/categories/category-name-slugified.yml**
  - subsitutes the category text from the JSON array item for the placeholder text in the new md file
  - subsitutes the category text from the JSON array item for the placeholder text in the new yml file


#### getallconnectorscontent.py

Use this to create md and associated json for all live connectors. 

The process overwrites any existing files. If you need to retain any existing md or json from the target folders, back up to another folder before running the script.

- Makes API call https://my.cyclr.com/api/connectors?pageSize=1000&details=true
- Parses the returned JSON array:
  - copies **\_bin/v2/assets/templateconnector.md** to **pages/v2/connectors/connector-name-slugified.md**
  - derives the corresponding version 1 content for the connector **\_includes/v2/connector/v1content/'+file_name+'.md'**
  - subsitutes the connector text from the JSON array item for the placeholder text in the new md file
  - checks if the version 1 connector md file exists
  - if the version 1 md files exists, sets the new md content to include that file
  - creates **\_data/v2/connectors/connector-name-slugified.json**
  - writes the connector json object to the new json file


#### getconnectorscontent.py

Use this to create the files for a single connector, supplying the connector id as an argument. 

The process overwrites any existing files.

For each new connector or new release, run this to create the new connector content or update to include new release content.

```
c:\cyclr_docs\_bin\v2> python .\getconnectorscontent.py --help 
usage: getconnectorscontent.py [-h] [-c CONNECTORID]

Get connector content

options:
  -h, --help            show this help message and exit
  -c CONNECTORID, --connectorid CONNECTORID
                        Get connector for given ID


```
The JSON response is processed in the same way as detailed getallconnectorscontent.py


#### jekyll build
After the python scripts have created the category and connector md and other files, run the jekyll/docker processes to rebuild the site from the new md and data files.


### SCSS
The site uses SASS. The source files are defined in the **\_sass** folder.

The scss files are compiled and included in the site css via **css/style.scss**. This is the one sass file that includes front matter: the two '---' lines direct jekyll to process the file using sass.

The **css/style.scss** uses @import directives to include the required style files: this includes the google font files, the bootstrap files and the custom files. 


### Bootstrap

See https://veithen.io/2015/03/26/jekyll-bootstrap.html for notes on using Bootstrap with jekyll

The current Bootstrap source is version 3: in order to incorporte Bootstrap 5 flex/grid, the relevant Bootstrap 5 scss files have been added .

** TO DO **

- Replace the current setup with Bootstrap 5 installed as a submodule or package.
- Amend html class/id attributes to include Bootstrap 5 values. 
- Update accordion menus and any other UI to ensure consistent with required markup for Bootstrap 5  

#### Accordion 

The connector guides render the methods in collapsible accordions. See https://getbootstrap.com/docs/5.0/components/accordion/ for the markup.

The methods content is defined in the connector's json in  **\_data/v2/connectors**, and that content is parsed in **\_includes/v2/connector/connector.html** to create the accordion content. 

#### Tables

Some connector connect is presented in tables: no id or class attributes are required to apply the default style to tables rendered in the  **main.content** element. 

All  the document pages use the same layout, so the content is always rendered in **main.content**. 

To apply alternative table styles, the style rules must be added to the scss, and the corresponding attributes defined where appropriate in **\_includes/v2/connector/connector.html**