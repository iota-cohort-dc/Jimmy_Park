class SessionsController < ApplicationController
  def new # render login page
  end

  def create
    @user = User.find_by_email(params[:Email])

    if @user && @user.authenticate(params[:Password])
      session[:user_id] = @user_id
      redirect_to "/users/#{@user.id}"
    else
      # flash[error] = @user.errors.full_messages
      flash[:errors] = ["Invalid Combination"]
      redirect_to "/sessions/new"
      # redirect_to "/"
      # redirect_to :back
    end
  end

  def destroy
    reset_session
    # session[:user] = nil
    redirect_to "/sessions/new"
  end
end
