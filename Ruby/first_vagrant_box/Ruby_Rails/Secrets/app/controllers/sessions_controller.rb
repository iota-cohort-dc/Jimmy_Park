class SessionsController < ApplicationController

  def new
  end
  #
  def create
    user = User.find_by_email(params[:email])

    if user && user.authenticate(params[:password])
      session[:user_id] = user.id
      redirect_to "/users/#{user.id}"
    else
      flash[:error] = "Invalid Credentials"
      redirect_to "/"
    end
  end

  # def show
  # end

  # def edit
  # end

  # def update
  # end

  def destroy
    session.clear
    redirect_to "/sessions/new"
  end
end
