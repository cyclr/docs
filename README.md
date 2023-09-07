---
title: Cyclr Documentation README
permalink: README
sidebar: cyclr_sidebar
---

{::options parse_block_html="true" /}
<section class="card">

## Doc amends

Use the [editor on GitHub](https://github.com/cyclr/docs/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

The docs repo runs the GitHub Actions workflow when you push commits to the master branch. The workflow rebuilds and deploys the master branch to the live site.

Part of this workflow involves checks. If not successful, the commits page shows a red cross symbol next to the commit. You can select the cross and then select **details** in order to find more details/re-run the failed jobs.

</section>

<section class="card">

## Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing.

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).


### Kramdown

Kramdown is the default Markdown renderer for Jekyll.

See the [Kramdown documentation for more info](https://kramdown.gettalong.org/index.html).


#### HTML parsing

Add this option to the first line in the md file after the header content to enable HTML parsing.  
``
{::options parse_block_html="true" /}
``

See the [Kramdown documentation for more info](https://kramdown.gettalong.org/parser/kramdown.html).

By default, the Kramdown parser does not convert HTML tags to native representation. Enabling this option means we can use HTML tags in the md. This is useful to provide container or content elements with attributes (class,id) in order to implement the required style and UX.

Amend v1 markdown to include the relevant html eg:
- The 'Required' sections : green left border, grey background with drop shadow, exclamation mark icon 
- The code sections : dark grey left border, grey background with drop shadow, 'C' icon 

</section>

<section class="card">

## Local site 

To set up for a local site:

1. If you don't have Docker installed, install [Docker](https://docs.docker.com/install/)
    - Docker is optional
    - You can use Git Bash for the jekyll cli
2. Open the terminal or Git Bash window
3. On your local computer, clone the Git repository for Cyclr Documentation:
```Shell
$ git clone https://github.com/cyclr/docs.git
```
4. Install [Ruby](https://www.ruby-lang.org/en/documentation/installation/)
    *  For Windows users download the latest `Ruby+Devkit` x64 installer from [RubyInstaller for Windows](https://rubyinstaller.org/downloads/)
    *  Use the following [step by step tutorial](https://www.geeksforgeeks.org/how-to-install-rubygems-in-windows/) to guide you through the installation process for Windows
6. Open the command line at the root of your Github repository and run `bundle install` to install all dependencies.
    *  If `bundle install` is unsuccessful, you can delete the `gemfile.lock` file and retry.

To build the local site:

1. Open  the command line at the root of your Github repository.
2. Run `bundle exec jekyll serve`
3. Go to http://127.0.0.1:4000/ in order to view your local site.
    *  You can also go to a specific file in the `...GitHub\docs\_site` folder to view it as a webpage.

> **Note**: If there is an error, append `--trace` to the serve command to provide more information. Check the formatting of the documents changed.


### Gems and plugins

See the Gemfile and \_config.yml for plugins.


### Build errors

If your build fails, this may be the result of:
- missing gem or gem version: use gem install [gemfile] -v [version]
- Gemfile.lock discrepancies: delete the lock file and run `bundle install` again for a fresh install
 
</section>

<section class="card">

## Pages and front matter

All Cyclr Docs v2 pages are defined in the pages/v2 folder.

The folder and subfolder structure reflects the menu organisation and provides logical grouping of the pages.

> **Note**: The menu front matter alone determines where the page is displayed in the menu.

This allows for the displayed menu options to be managed via front matter:
- menu text
- menu option behaviour: toggle submenu or page link
- link type: same browser window or new window
- order the file appears in the sidebar


The numeric value for `weight` in the front matter determines the order that the page appears within that sidebar category (1 being the highest position).

> **Note**: Connector docs don't require the second section of front matter (see the `\GitHub\docs\_templates` folder for examples).


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

</section>

<section class="card">

## Markdown templates

The **_templates** folder includes templates for:
- category page
- category page with search box
- connector page with authentication details
- connector page with other information
- any other doc page

Each template includes the front matter required for that type of page:
- Kramdown HTML parsing option
- sample card section HTML tags
- sample markdown for h2 and h3 headings

The Cyclr docs layout standard uses a card for each h2 heading and its associated content: to implement this, add the HTML element <section class="card"> for each h2 in your copy, and the closing </section> after the relevant content.

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

The **js** folder includes:
- **bootstrap** folder with various UI scripts 
- **mdb** folder for mdb component UI scripts
- scripts to provide custom functionality , e.g. preventing scroll chaining, back to top 

</section>
