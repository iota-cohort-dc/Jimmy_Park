class SessionsController < ApplicationController
  def new # render login page
  end

  def create
    @user = User.find_by_email(params[:email])

    if @user && @user.authenticate(params[:password])
      session[:user_id] = @user_id
      redirect_to "/users/#{@user.id}"
    else
      # flash[error] = @user.errors.full_messages
      flash[:errors] = ["Invalid Combination"]
      redirect_to "/session/new"
      # redirect_to "/"
      # redirect_to :back
    end
  end

  def destroy
    reset_session
    # session[:user] = nil
    redirect_to "/session/new"
  end
end
