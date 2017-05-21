FORMAT TO HUMANIZE HUMAN READABLE DATE -----------------------------------------
  - add at the end   .strftime("%B %d, %Y")
  
  <% @messages.each do |message| %>
    <h3> <%= message.user.username %> </h3>
    <p>  <%= message.content %> - <%= message.created_at.strftime("%B %d, %Y") %>  </p>
    <hr>
  <% end %>

ROUTES.RB ----------------------------------------------------------------------
  get 'users' => 'display#index'
  get 'users/new' => 'display#new'
  post "users" => "display#create"
  get 'users/:id' => 'display#show'
  get 'users/:id/edit' => 'display#edit'
  patch 'users/:id' => 'users#update'
  get 'users/:id' => 'display#delete'

FORMS --------------------------------------------------------------------------
  <form action='/products/' method='post'>
    <input type="hidden" name="authenticity_token" value="<%= form_authenticity_token %>">
    <input type='text' name='product[name]' placeholder='name' />
    <input type='text' name='product[description]' placeholder='description' />
    <input type='submit' value='Create' />
  </form>

  SEQUEL INJECTION -------------------------------------------------------------
    # inside the HTML, (ex.) inject in a table
  "  <%= @result['name'] %>       "

FORM UPDATE --------------------------------------------------------------------
  # form for updating
  <form action="/products/<%= @products.id %>" method="post">
    <input type="hidden" name="_method" value="patch">
    <input type="hidden" name="authenticity_token" value="<%= form_authenticity_token %>">
    <input type="text" name="name" value="<%= @product.name %> ">
    <input type="submit" value="Update Product">
  </form>

FORM DELETE --------------------------------------------------------------------

  <form action="/product/<%= @product.id %>" method="post">
    <input type="hidden" name="_method" value="delete">
    <input type="hidden" name="authenticity_token" value="form_authenticity_token">
    <input type="submit" value="Delete">
  </form>

TABLE --------------------------------------------------------------------------
  <table>
      <thead>
          <tr>
              <th>Name:</th>
          </tr>
      </thead>
      <tbody>
          <tr>
              <td></td>
          </tr>
      </tbody>
  </table>

  SEQUEL INJECTION -------------------------------------------------------------
  # inside the HTML, (ex.) inject in a table
    <%= @result['name'] %>

    <%= @result['name'] %>

FOR LOOP IN HTML ---------------------------------------------------------------
<% @messages.each do |message| %>
  <p> <%= message.content %> <%= message.created_at %> </p>

    <%= @comment.each do |item| %>
    <% if item.message_id == message.id%>
    <p> <%= item.comment_content %> <%= item.created_at %> </p>

    <% end %>
    <% end %>


A href IN HTML------------------------------------------------------------------
  <a href="users/<%=user.id%>"> <%= user.name %></a>
  <a href="users/<%=user.id%>"> <%= user.name %></a>

MARCO --------------------------------------------------------------------------
  <a href="users/<%=user.id%>" data-method="Delete">Delete Me!</a>
  data method is pointing to the action verb 'delete'


INDEX --------------------------------------------------------------------------
class UsersController < ApplicationController
  def index
    @users = User.all
  end

CREATE query to create person --------------------------------------------------
  def create
    User.create(name: params[:name], age: params[:age])
    redirect_to '/users'
  end
SHOW query to show info --------------------------------------------------------
  def show
    @user = User.find(params[:id])
  end

EDIT query to edit -------------------------------------------------------------
  def edit
    @user = User.find(params[:id])
  end

UPDATE query to update ---------------------------------------------------------
  def update
    User.find(params[:id]).update(name:params[:name], age:params[:age])
    redirect_to '/users'
  end

UPDATE query to update person --------------------------------------------------
def update
  User.find(params[:id]).update(name:params[:name], age: params[:age])
end
# another example
def update
  anime = Anime.find(params[:id])
  anime.name = params[:name]
  anime.save
end

DESTROY query to delete --------------------------------------------------------
  def destroy
    User.find(params[:id]).destroy
    redirect_to '/users'
  end
  # another example
  def destroy
    product = Product.find(params[:id])
    product.destroy
    redirect_to '/product'
  end

JSON API -----------------------------------------------------------------------
  json: User.find(params[:id])

QUERY get all users ------------------------------------------------------------
  @user = User.find(params[:id])

SESSION ------------------------------------------------------------------------
  # set session to 0
  session['count'] = 0
  # increment session count
  session['count'] = session['count'] + 1
  # save the post data (params[:survey])
  session['count'] = params[:survey] # :survey is in the form

FLASH MESSAGES -----------------------------------------------------------------
# in the surveys.rb
flash[:success] = "Thanks for submitting this form! You have submitted this form #{session[:views]} time(s) now."

# in the HTML
  <% if flash[:success] %>
  		<div id="success">
  			<p><%= flash[:success] %></p>
		</div>
	<% end %>


STRING INTERPOLATION -----------------------------------------------------------
  "#{session[:views]}"
  "#{ }"

  <% session[:activity].reverse.each do |item| %>
  <%= item %>
  <% end %>


EMAIL_REGEX --------------------------------------------------------------------
  EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i

RUBY MODELS --------------------------------------------------------------------
class User < ActiveRecord::Base
  EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i
  validates :first_name, :last_name, presence: true, length: { in: 2..20 }
  validates :email, presence: true, uniqueness: { case_sensitive: false }, format: { with: EMAIL_REGEX }
end

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
TDD ----------------------------------------------------------------------------
TDD ----------------------------------------------------------------------------
TDD ----------------------------------------------------------------------------

 rake db:migrate RAILS_ENV=test
 test files in spec folder

 models folder
  open user_spec

    RSpec.describe User, type: :model do
      #pending "add some examples to (or delete) #{__file__}"
      context "With valid atrributes" do
        it "should be valid" do
          user = User.create(username: "harrypotter")
          expect(user).to be_valid
        end
      end
    end

    #user .rb  in the models
    RSpec.describe User, type: :model do
      context "with invald attributes " do
        it "should not be valid if username field is left blank" do
          user = User.create(username: "")
          expect(user).to be_invalid
        end
        it "should not be valid if username is not unique" do
          User.create(username: "harrypotter")
          user = User.new(username: "harrypotter")
          expect(user).to be_invalid
        end
      end
    end

    # MESSAGES .rb in the models
    RSpec.describe User, type: :model do
      context "with valid attributes" do
        it "it should be valid" do
          message = Message.create(content: "this is a message", user: User.create(username: "harrypotter"))
          expect(message).to be_invalid

        end
      end
    end

    # FactoryGirl
    FactoryGirl.define do
      factory :user do
        first_name "shane"
        last_name "chang"
      end
    end
    FactoryGirl.define do
      factory :product do
        name "MyString"
        user nil
      end
    end

    it "should be a valid product" do
      expect(build(:product, user: build(:user))).to be_valid
      # expect(build(:product,user: build(:user)))
      # is the same as Product.create
      # is the same as User.create
      # it builds Product and User from the FactoryGirl above
    end
    run: rspec spec/models/user_spec.rb

    # Features ----------------------------------------------------
    # features test for the method
    # have to manuelly create

    # in capybara on platform
    requires 'rails_helper'
      feature 'when a user creates message' do
        before(:each) do
        #before each of the test, do this first, then run the test
          visit '/'
          # 'the actual route'
          fill_in 'username', with: 'harrypotter'
          click_button 'Create New Username'
        end
        secenario 'successfully creates a message' do
          fill_in 'content', with: 'This is a test message'
        # same as context
          click_button 'Post a Message'
          expect(page).to have_content 'This is a test message'
          expect(current_path).to eq('/messages')

        end
      end
    end
    run: rspec spec/features/message_spec.rb

--------------------------------------------------------------------------------
solution -----------------------------------------------------------------------
correct way --------------------------------------------------------------------
this should be in the
 /spec/models/user_spec.rb   file ----------------------------------------------

require 'rails_helper'

RSpec.describe User, type: :model do
  context "With valid attributes" do
    it "should save" do
      user = User.new(
        first_name: 'shane',
        last_name: 'chang',
        email: 'schang@codingdojo.com'
      )
      expect(user).to be_valid
    end
  end

  context "with invalid attributes" do
    it "should not save if first_name field is blank." do
     user = User.new(
      first_name: '',
      last_name: 'chang',
      email: 'schang@codingdojo.com'
     )
     expect(user).to be_invalid
    end
    it "should not save if last_name field is blank." do
     user = User.new(
      first_name: 'shane',
      last_name: '',
      email: 'schang@codingdojo.com'
     )
     expect(user).to be_invalid
    end
    it "should not save if email already exists." do
     User.create(
      first_name: "Jane",
      last_name: "Doe",
      email: "janethebest@codingdojo.com"
     )
     user = User.new(
      first_name: "Jane",
      last_name: "Smith",
      email: "janethebest@codingdojo.com"
     )
     expect(user).to be_invalid
    end
    it "should contain a valid email" do
     user = User.new(
      first_name: 'Roald',
      last_name: 'Dahl',
      email: 'roalddahl'
     )
     expect(user).to be_invalid
    end
  end
end

# This is for the cod above
# need to have your models validations prior to running test
app/models/user.rb

class User < ActiveRecord::Base
  validates :first_name, :presence => true
end

--------------------------------------------------------------------------------
TDD FACTORY GIRL ---------------------------------------------------------------
TDD FACTORY GIRL ---------------------------------------------------------------

group :development, :test do
  gem 'rspec-rails'
  gem 'factory_girl_rails'
end

# spec/rails_helper.rb
require 'factory_girl_rails'
RSpec.configure do |config|
  config.include FactoryGirl::Syntax::Methods
  ...
end

rails g model User first_name:string last_name:string email:string

# spec/factories/users.rb
FactoryGirl.define do
  factory :user do
    first_name "John"
    last_name "Doe"
    email "john@doe.com"
  end
end

# spec/models/user_spec.rb
require 'rails_helper'
RSpec.describe User, type: :model do
  context "With valid attributes" do
    it "should save" do
      expect(build(:user)).to be_valid
    end
  end
  context "With invalid attributes" do
    it "should not save if first_name field is blank" do
      expect(build(:user, first_name: "")).to be_invalid
    end
    it "should not save if last_name field is blank" do
      expect(build(:user, last_name: "")).to be_invalid
    end
    it "should not save if email already exists" do
      create(:user)
      expect(build(:user)).to be_invalid
    end
    it "should not save if invalid email format" do
      expect(build(:user, email: "invalidEmail")).to be_invalid
    end
  end
end

# spec/factories/users.rb
FactoryGirl.define do
  factory :user do
    first_name "shane"
    last_name "chang"
  end
end

# spec/factories/products.rb
FactoryGirl.define do
  factory :product do
    name "MyString"
    user nil
  end
end

# spec/models/product_spec.rb
it "should be a valid product" do
  expect(build(:product, user: build(:user))).to be_valid
end

# spec/factories/products.rb
FactoryGirl.define do
  factory :product do
    name "MyString"
    user # nil value removed
  end
end

# spec/models/product_spec.rb
it "should be a valid product" do
  expect(build(:product)).to be_valid # build(:product) simplified
end

# spec/factories/users.rb
FactoryGirl.define do
  factory :user do
    last_name "Doe"
    admin false
    trait :male do
      first_name "John"
      email "john@doe.com"
    end
    trait :female do
      first_name "Jane"
      email "jane@doe.com"
    end
    trait :admin do
      admin true
    end
  end
end

# spec/models/user_spec.rb
it "should also be valid" do
  expect(build(:user, :male).first_name).to eq("John")
  expect(build(:user, :female).first_name).to eq("Jane")
end

# We can also use multiple traits on the same instance:
male_admin = build(:user, :male, :admin)

# spec/factories/users.rb
FactoryGirl.define do
  factory :user do
    first_name "John"
    last_name "Doe"
    full_name { "#{first_name} #{last_name}" }
    age {rand(21..60)}
  end
end

--------------------------------------------------------------------------------

RUNNING RSpec TESTS
Different ways to run RSpec tests
Lets' take a look at some different ways run our RSpec tests. We will use the Model Spec assignment you just completed.'

Run all the spec tests: rspec spec
Run all the spec tests in a specific file: rspec spec/<FOLDER>/<FILENAME>
i.e. rspec spec/models/user_spec.rb
Run a specific spec test: rspec spec/<FOLDER>/<FILENAME>:<LINE_NUMBER>
i.e. rspec spec/models/user_spec.rb:4
This will run the spec test on line 4.
Also, keep in mind that to run a RSpec test you must run it from the root of your directory. If you cd into spec/models and then run the command rspec user_spec.rbit will not work.

--------------------------------------------------------------------------------

# You can override any of the defined attributes by passing a hash into either function call.
build(:user, first_name: 'oscar')
create(:user, last_name: 'vazquez', email: 'ovazquez@codingdojo.com')

--------------------------------------------------------------------------------
CAPYBARA -----------------------------------------------------------------------
CAPYBARA ----------------------------------------------------------------------

group :development, :test do
  gem 'rspec-rails'
  gem 'factory_girl_rails'
  gem 'capybara'
end

rails g controller Users new

# config/routes.rb
resources :users

# Now let's create a folder where we can put our feature specs. From the root of your rails project run the following.
dojo$ mkdir spec/features
dojo$ touch spec/features/register_user_spec.rb

# spec/features/register_user_spec.rb
require 'rails_helper'
feature "guest user creates an account" do
  scenario "successfully creates a new user account" do
    visit new_user_path
    fill_in "user_first_name", with: "shane"
    fill_in "user_last_name", with: "chang"
    fill_in "user_email", with: "schang@codingdojo.com"
    click_button "Create User"
    expect(page).to have_content "User successfully created"
  end
end

Lets run our capybara test
Terminal
rspec spec/features/register_user_spec.rb

# /app/controllers/users_controller.rb
def create
  @user = User.new(params.require(:user).permit(:first_name, :last_name, :email))
  if @user.save
    flash[:notice] = ['User successfully created']
    redirect_to new_user_path
  else
    #errors we need to code later
  end
end

--------------------------------------------------------------------------------

# spec/factories/users.rb
FactoryGirl.define do
  factory :user do
    first_name "MyString"
    last_name "MyString"
    email "MyString"
  end
end

# spec/features/register_user_spec.rb
FactoryGirl.define do
  factory :user do
    first_name "MyString"
    last_name "MyString"
    email "MyString"
  end
end

# spec/helpers/users_helper_spec.rb
require 'rails_helper'

# Specs in this file have access to a helper object that includes
# the UsersHelper. For example:
#
# describe UsersHelper do
#   describe "string concat" do
#     it "concats two strings with spaces" do
#       expect(helper.concat_strings("this","that")).to eq("this that")
#     end
#   end
# end
RSpec.describe UsersHelper, type: :helper do
  pending "add some examples to (or delete) #{__FILE__}"
end

# spec/models/user_spec.rb
require 'rails_helper'

RSpec.describe User, type: :model do
  context "With valid attributes" do
    it "should save" do
      user = User.new(
        first_name: 'shane',
        last_name: 'chang',
        email: 'schang@codingdojo.com'
      )
      expect(user).to be_valid
    end
  end

  context "with invalid attributes" do
    it "should not save if first_name field is blank." do
     user = User.new(
      first_name: '',
      last_name: 'chang',
      email: 'schang@codingdojo.com'
     )
     expect(user).to be_invalid
    end
    it "should not save if last_name field is blank." do
     user = User.new(
      first_name: 'shane',
      last_name: '',
      email: 'schang@codingdojo.com'
     )
     expect(user).to be_invalid
    end
    it "should not save if email already exists." do
     User.create(
      first_name: "Jane",
      last_name: "Doe",
      email: "janethebest@codingdojo.com"
     )
     user = User.new(
      first_name: "Jane",
      last_name: "Smith",
      email: "janethebest@codingdojo.com"
     )
     expect(user).to be_invalid
    end
    it "should contain a valid email" do
     user = User.new(
      first_name: 'Roald',
      last_name: 'Dahl',
      email: 'roalddahl'
     )
     expect(user).to be_invalid
    end
  end
end

--------------------------------------------------------------------------------
run: rspec spec
run:  rspec spec/models/message_spec.rb

factory
test login feature
go into
--------------------------------------------------------------------------------
