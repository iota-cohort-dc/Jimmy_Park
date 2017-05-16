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
    <%= @result['name'] %>

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

UPDATE query to update person --------------------------------------------------
  def update
    User.find(params[:id]).update(name:params[:name], age: params[:age])

JSON API -----------------------------------------------------------------------
  json: User.find(params[:id])

QUERY get all users ------------------------------------------------------------
  @user = User.find(params[:id])

SESSION ----------------------------------------------------------------------
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
