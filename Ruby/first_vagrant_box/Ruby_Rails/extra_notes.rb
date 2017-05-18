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

FLASH MESSAGES
# in the surveys.rb
flash[:success] = "Thanks for submitting this form! You have submitted this form #{session[:views]} time(s) now."

# in the HTML
  <% if flash[:success] %>
  		<div id="success">
  			<p><%= flash[:success] %></p>
		</div>
	<% end %>


STRING INTERPOLATION
  "#{session[:views]}"
  "#{ }"

  <% session[:activity].reverse.each do |item| %>
  <%= item %>
  <% end %>

EMAIL_REGEX
  EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i

RUBY MODELS   
class User < ActiveRecord::Base
  EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i
  validates :first_name, :last_name, presence: true, length: { in: 2..20 }
  validates :email, presence: true, uniqueness: { case_sensitive: false }, format: { with: EMAIL_REGEX }
end
