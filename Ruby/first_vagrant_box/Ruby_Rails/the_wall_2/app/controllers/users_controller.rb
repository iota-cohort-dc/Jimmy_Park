class UsersController < ApplicationController
  def index # show index page
  end

  def create # create new username, then redirect to messages#index
    @user = User.find_by(username: params[:username])

    if @user
      session[:user] = @user.id
      redirect_to '/messages'
    else
      @user = User.create(username: params[:username])
      if @user.valid?
        session[:user] = @user.id
        redirect_to '/messages'
      else
        flash[:error] = @user.errors.full_messages
        redirect_to :back
      end
    end
  end

  def logout
    session.clear
    # session[:user] = nil
    reset_session
    redirect_to "/"
  end

end
