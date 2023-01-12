---
title: Cyclr Documentation README
permalink: README
sidebar: cyclr_sidebar
---

{::options parse_block_html="true" /}
<section class="card">
## Doc amends

Use the [editor on GitHub](https://github.com/cyclr/docs/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

The docs repo is configured to run the GitHub Actions workflow when a pull request to the master branch is made. The workflow rebuilds and deploys the master branch to the live site.

</section>

<section class="card">
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

### h3 heading
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

<section class="card">

## Pages and front matter

All Cyclr Docs v2 pages are defined in the pages/v2 folder.

The folder and subfolder structure reflects the menu organisation and provides logical grouping of the pages.

NB: the menu front matter alone determines where the page is displayed in the menu.

This allows for the displayed menu options to be managed via front matter:
- menu text
- menu option behaviour: toggle submenu or page link
- link type: same browser window or new window

The numeric prefix is used to control the order in which the options are displayed. The jekyll-menus plugin builds the data object from the md front matter, appending the relevant data from each file to its arrays. Amend the numeric prefixes to achieve the required menu option order.

### Sidebar Menu

The sidebar menu requires the front matter used by jekyll-menus plugin. 

The jekyll-menus plugin works on local sites, however it is not compatible with the GitHub Actions workflow. Custom functionality using the same front matter builds the menu. 

Pages without required front matter are omitted from the menu. Connector pages are not included in the menu.

See https://github.com/forestryio/jekyll-menus for details.

This implementation includes customisations :

| customisation | where | description |
| --- | --- | --- |
| externalurl | front matter | Use externalurl instead of url to open the page in a new tab or window |

### Omit page from menu
To prevent a page appearing as a menu item, remove the 'menus' item and its children from the front matter. 

### Category page
The index.md file in each pages/v2 folder provides the front matter and markdown for the site's category pages.

The front matter defines how the category is displayed in the sidebar menu, and the category menu id provides the parent menu id to include in all the category's doc pages 


| item | description |
| --- | --- |
| [parentmenuid] | child of the menus front matter item - this defines the immediate parent of this page |
| title | The menu item text  |
| identifier | this menu id - to be used as the [parentmenuid] in any child pages |
| weight | can be used to control menu item order |

#### Default category


#### Search category

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

</section>
