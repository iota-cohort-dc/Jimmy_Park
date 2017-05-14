Rails Footnotes

    Rails footnotes displays footnotes in your application for easy debugging, such as sessions, request parameters, cookies, filter chain, routes, queries, etc.
    Even more, it contains links to open files directly in your editor including your backtrace lines.
    Installation
    NOTE: Since this branch aims for Rails 3.2+ support, if you want to use footnotes with Rails 2.3 you should use this branch:
    github.com/josevalim/rails-footnotes/tree/rails2
    Installing Rails Footnotes is very easy.
    Rails 3.2.x/4.x
    NOTE# gem 'rails-footnotes', '~> 4.0'
    After you install RailsFootnotes and add it to your Gemfile, you need to run the generator:
    NOTE# rails generate rails_footnotes:install
    This will create an initializer with default config and some examples.

Hirb 0.7.3

    Hirb provides a mini view framework for console applications and uses it to improve ripl(irb)'s default inspect output. Given an object or array of objects, hirb renders a view based on the object's class and/or ancestry. Hirb offers reusable views in the form of helper classes. The two main helpers, Hirb::Helpers::Table and Hirb::Helpers::Tree, provide several options for generating ascii tables and trees. Using Hirb::Helpers::AutoTable, hirb has useful default views for at least ten popular database gems i.e. Rails' ActiveRecord::Base. Other than views, hirb offers a smart pager and a console menu. The smart pager only pages when the output exceeds the current screen size. The menu is used in conjunction with tables to offer two dimensional menus.
    Installation
    Add it to your Gemfile:
    NOTE# gem 'simple_form'

    Run the following command to install it:
    NOTE# bundle install
    Run the generator:
    NOTE# rails generate simple_form:install
    Bootstrap
    Simple Form can be easily integrated to the Bootstrap. To do that you have to use the bootstrap option in the install generator, like this:
    NOTE# rails generate simple_form:install --bootstrap
    You have to be sure that you added a copy of the Bootstrap assets on your application.
