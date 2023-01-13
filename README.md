---
title: Cyclr Documentation README
permalink: README
sidebar: cyclr_sidebar
---

{::options parse_block_html="true" /}
<section class="card">
## Doc amends

Use the [editor on GitHub](https://github.com/cyclr/docs/edit/master/README.md){:target="_blank"} to maintain and preview the content for your website in Markdown files.

The docs repo is configured to run the GitHub Actions workflow when a pull request to the master branch is made. The workflow rebuilds and deploys the master branch to the live site.

</section>

<section class="card">
## Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing.

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/){:target="_blank"}.

### Kramdown

Kramdown is the default Markdown renderer for Jekyll.

See the [Kramdown documentation for more info](https://kramdown.gettalong.org/index.html){:target="_blank"}.

#### HTML parsing

Add this option to the md file to enable HTML parsing.  
``
{::options parse_block_html="true" /}
``

See the [Kramdown documentation for more info](https://kramdown.gettalong.org/parser/kramdown.html){:target="_blank"}.

By default, the Kramdown parser does not convert HTML tags to native representation. With this option, we add containers such as ``<section>`` tags with attributes (class,id) to implement the required style and UX.

</section>

<section class="card">


## Local site 

To set up a local site:

1. If you don't have Docker installed, install [Docker](https://docs.docker.com/install/){:target="_blank"}.
2. Open the terminal.
3. On your local computer, clone the Git repository for Cyclr Documentation:
```Shell
$ git clone https://github.com/cyclr/docs.git
```
4. Install [Ruby](https://www.ruby-lang.org/en/documentation/installation/){:target="_blank"}
5. Run bundle install to install all dependencies
6. Start up the application:
```Shell
$ docker-compose up
```

### CLI 
The most frequently used commends for local amends and development are:

* ``bundle install``: installs gems and plugins 
* ``bundle update``: updates installed gems and plugins
* ``bundle exec jekyll serve --livereload``: build and serve the site, with the option to rebuild on file change.

### Gems and plugins
See the ``Gemfile`` and ``_config.yml`` for plugins. 
 
</section>

<section class="card">

## Pages and front matter

All Cyclr Docs v2 pages are defined in the ``pages/v2`` folder.

The folder and subfolder structure reflects the menu organisation and provides logical grouping of the pages.

The menu front matter alone determines where the page is displayed in the menu.

See [Page templates](#page-templates) for details of front matter for all page types.

### Sidebar Menu

The sidebar menu is built the front matter used by ``jekyll-menus`` plugin. Pages without required front matter are omitted from the menu. 

The ``jekyll-menus`` plugin works on local sites, however it is not compatible with the GitHub Actions workflow. Custom functionality using the same front matter builds the menu. 

Connector pages are not included in the menu.

See  [jekyll-menus](https://github.com/forestryio/jekyll-menus){:target="_blank"} for details. However the plugin is not required for local, test or production sites and is commented out from the ``Gemfile`` and ``_config.yml``.

### Category page

The index.md file in each ``pages/v2`` folder provides the front matter and markdown for the each category page.

## Style and UX

### SCSS

The site is built with [MDB Pro](https://mdbootstrap.com/docs/standard/pro/){:target="_blank"}.

The source files are in the ``\_sass`` folder.

The scss files are compiled and included in the site css via ``assets/css/style.scss`` 

This is the one sass file that includes front matter, the two ``---`` lines direct jekyll to process the file using sass.

The ``assets/css/style.scss`` uses ``@import`` directives to include the required style files: this includes the google font files, the mdbootstrap files and the custom files. 

### JavaScript

</section>

<section class="card">

## Page templates

To add pages to the site, copy the appropriate template from  the ``_templates`` folder to the correct folder in ``pages/v2``.

Change the placeholder text in the front matter, and add the page content.

**NB: The kramdown HTML parsing option ``{::options parse_block_html="true" /}`` must be the first text after the front matter.**

### Front matter


| **Variable** | **Value** |
|---|---|
| title | replace ``Doc title`` with the page title |
| sidebar | ``cyclr_sidebar`` **do not change** |
| permalink | replace ``doc-permalink`` with page slug |
| tags | within the square brackets, replace ``doctags`` with one or more tags  |
| externalurl | include only if the link is to an external site , replace ``docexternalurl`` with the absolute full url |
| layout | ``page`` **do not change** |
| toc | ``_config.yml`` defaults include ``toc: true`` which is used for all pages where the variable is omitted from the front matter: add the variable with value ``false`` when the page does not need the table of contents  |
| categorylayout | ``_config.yml`` defaults include ``categorylayout: "category_default"``, add the  variable with value ``category-search`` for a category page which requires the search layout |
| introtitle | replace ``Category title`` |
| introtext | replace ``Category intro text`` , this will be displayed between the page title and the rest of the page content |
| menus | **do not change** |
| menus: parentmenuid | replace with the ``menuid`` of the parent menu, the top level menu id is ``mainmenu`` |
| menus: title | replace ``Menu title`` with the page title |
| menus: identifier | replace ``menuid`` with item's menu id, usually the same as the ``permalink``. If this is a category page, this is the ``parentmenuid`` for any pages in that category |
| menus: icon | replace ``menuicon`` with Cyclr 2 font icon name, e.g. ``navsettings`` |
| menus: weight | replace ``weight`` with numeric value , defines the ordincal position of the item in the menu |


The tags are not used in the site at present.

### Connector page

Template **template-connector**

Connector pages are not listed in the sidebar menu: do not add the ``menus:`` to the front matter.

Add the content, wrapped in one or more ``<section class="card">`` tags which renders the content in cards.

### Other doc page

Template **template-doc**

If a menu item links to another site, include this variable. The link is rendered with the ``target="_blank"`` attribute.

### Category page

Each index.md page in a subfolder is rendered as a category page, and must have the ``menus:`` front matter.

The `icon`` front matter variable is defined only for top level (``mainmenu``) category pages.

These front matter value are used to determine page layout or as content :
* categorylayout
* introtitle
* introtext

In the category page after the front matter, replace the ``doc-permalink`` strings, otherwise leave the Liquid statements as they are.

#### Default layout

Template **template-category-default**

This layout displays a list of links to all pages in the category. 

It is built from the front matter of all files assocaited with the category's ``menuid``. 

The process that builds the page list is recursive and outputs nested lists to match the category's structure.

#### Search layout

Template **template-category-search**

At present only the [Application connectors](https://docs.cyclr.com/connector-guides){:target="_blank"} category uses this layout. 

This layout displays a hero for the search, and tile style links to other pages.

The tile content is defined in  ``_data/categories/[doc-permalink].yml``. Use [_data/categories/connector-guides.yml](https://github.com/cyclr/docs/blob/master/_data/categories/connector-guides.yml){:target="_blank"} as a model. 

For links to external sites, use the ``externalurl`` variable.

</section>
