source "https://rubygems.org"

gem "jekyll", "~> 4.0.0"
# gem 'github-pages', '~> 214', group: :jekyll_plugins

# If you want to use GitHub Pages, remove the "gem "jekyll"" above and
# uncomment the line below. To upgrade, run `bundle update github-pages`.
# gem "github-pages", group: :jekyll_plugins

gem "webrick", "~> 1.7"

gem "sorted_set", "~> 1.0"

gem 'jekyll-toc'

gem 'markdown_helper'

# jekyll-menus is not compatible with GitHub Actions workflow. 
# Custom functionality builds the sidebar menu from the md files' frontmatter: the jekyll-menus plugin is not required.
group :jekyll_plugins do
  gem "jekyll-seo-tag", "~> 2.7.1"
  gem 'jekyll-redirect-from', '~> 0.16.0'
  # gem "jekyll-menus", "~> 0.6.1"
end
