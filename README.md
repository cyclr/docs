---
title: Cyclr Documentation README
permalink: README
sidebar: cyclr_sidebar
---
{::options parse_block_html="true" /}
<section class="card">
## Doc amends

Use the [editor on GitHub](https://github.com/cyclr/docs/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

When a change is pushed to the docs repo master branch, the GitHub Actions workflow executes. The workflow rebuilds and deploys the master branch to the live site.

</section>

<section class="card">
## Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing.

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Kramdown

Kramdown is the default Markdown renderer for Jekyll.

See the [Kramdown documentation for more info](https://kramdown.gettalong.org/index.html).

#### HTML parsing

Cyclr Docs uses the [kramdown option](https://kramdown.gettalong.org/options.html) to process block HTML tags.


``
{::options parse_block_html="true" /}
``

By default, the Kramdown parser does not convert HTML tags to native representation. Enabling this option means we can use HTML tags in the md. 

Each md file includes the option as the first item after the front matter, to add html tags with attributes (e.g. class,id). These are essential implement the required Cyclr Docs style and UX.

</section>

<section class="card">

## Pages and front matter

All Cyclr Docs v2 pages are defined in the pages/v2 folder.

The folder and subfolder structure reflects the menu organisation and provides logical grouping of the pages. 

### Menu front matter

The front matter **menus:** section defines where the page is displayed in the menu. 

Connector guide pages do not include the menus section: they are not listed in the sidebar menu.

#### Example: Top level menu item

``` 
---
title: Cycle templates
sidebar: cyclr_sidebar
permalink: cycle-templates
tags: [cycle-templates]
layout: page
toc: false
introtitle: Create cycle templates
introtext: >-
    Create and configure reusable integrations as cycle templates which you build once and can deploy multiple times in order to scale your integrations.
menus:
  mainmenu:
    title: Cycle templates
    identifier: cycle-templates
    icon: template
    weight: 3
---
```
{: .overflow-visible}

#### Example: Nested menu item

```
---
title: Stop a cycle
sidebar: cyclr_sidebar
permalink: stopping-a-cycle
tags: [templates]
menus:
    cycle-templates:
        title: Stop a cycle
        identifier: stopping-a-cycle
        weight: 5
---
```
{: .overflow-visible}



| Menu variable | Description |
| --- | --- |
| parentmenuid | The parent menu for this item, cycle-templates in example above. Top level parentmenuid is **mainmenu** |
| title | The menu item text  |
| identifier | This menu id: can be the parentmenuid for nested menu items |
| icon | Cyclr 2 font icon displayed in the sidebar menu **NB: for top level menu items only** |
| weight | The ordinal position of this item in the menu |


#### Sidebar Menu

The sidebar menu uses the front matter used by [jekyll-menus plugin] (https://github.com/forestryio/jekyll-menus). 

The jekyll-menus plugin works on local sites. At present it is not compatible with the GitHub Actions workflow. 

Custom functionality using the same front matter builds the menu, and does not reqire the jekyll-menus plugin.

The sidebar menu is rendered using  _includes/v2/generic/menu.html, which is recursive to support nested menus.


### Category page

The index.md file in each pages/v2 folder provides the front matter and markdown for category pages.

Category page front matter includes additional custom variables.

```
---
title: Cycle templates
sidebar: cyclr_sidebar
permalink: cycle-templates
tags: [cycle-templates]
layout: page
toc: false
introtitle: Create cycle templates
introtext: >-
    Create and configure reusable integrations as cycle templates which you build once and can deploy multiple times in order to scale your integrations.
menus:
  mainmenu:
    title: Cycle templates
    identifier: cycle-templates
    icon: template
    weight: 3
---
```
{: .overflow-visible}

| Custom variable | Description |
| --- | --- |
| introtitle | Not used at present |
| introtext | Displayed on the category page before the page content |

#### Default category

Displays a list of all pages in this category.

The build identifies each files which use the category's identifier for the parent menu id and adds a link to that page.

Collapsible menus display nested items.

#### Search category

Displays the search box, same style and functionality as the homepage search. 

Aslo displays cards with links to other pages: the card content is defined in _data/categories/[category-page-permalink].yml. The yml is defined manually.

At present the [Application connectors](https://docs.cyclr.com/connector-guides) is the only category page of this type. 

#### Doc page

| Custom variable | Description |
| --- | --- | --- |
| externalurl |To open the page in a new tab or window |


</section>

<section class="card">

## Style and UX

### SCSS

The site is built with [MDB Pro](https://mdbootstrap.com/docs/standard/pro/).

The source files are in the **\_sass** folder.

The scss files are compiled and included in the site css via **assets/css/style.scss**. 

This is the one sass file that includes front matter: the two '---' lines direct jekyll to process the file using sass.

The **assets/css/style.scss** uses @import directives to include the required style files: this includes the google font files, the mdbootstrap files and the custom files. 

### JavaScript

JS libraries are in the js folder:

* native mdb and boostrap js provide the UI for various mdb and bs components, such as the sidebar menu toggle, top nav dropdown menus
* toc.js provides the UI for the table of contents displayed on all pages except homepage and category pages
* customscripts.js includes functionality for the nested menu in the sidebar 

</section>

<section class="card">
## Local site 

To set up a local site:

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

### Gems and plugins
See the Gemfile and \_config.yml for plugins.
 
</section>
