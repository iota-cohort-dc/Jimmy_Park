class UsersController < ApplicationController
  def index # just loads Sign In index page
  end

  def create # is called when Sign In button is clicked
    # User.find_by, can pass in a paramater / # User.find, passes in an id #
    @users = User.find_by(username: params[:username]) # if username exists
    if @users # if user exists
      session[:user] = @users.id # then put user found in session
      redirect_to "/messages" # redirect_to / move onto messages platform
    else # else create new username
      @users = User.create(username: params[:username]) # create new username
      if @users.valid? # does it pass the validations
        session[:user] = @users.id
        redirect_to "/messages" # redirect_to / move onto messages platform
      else
        flash[:error] = @users.errors.full_messages # is an array of errors
        # redirect_to "/" # redirect_to index page
        redirect_to :back # back to previous page
      end
    end
  end
end # ------ make sure you have the proper number of ends ------ #
