class UsersController < ApplicationController
  def index
  end

  def create
    @users = User.create(
      first_name: params[:first_name],
      last_name: params[:last_name],
      email: params[:email],
      password: params[:password],
      )

      if @users.valid?
        session[:user_id] = @users.id
        redirect_to "/products/index"
      else
        flash[:errors] = @users.errors.full_messages
        redirect_to :back
      end
  end

  def login
    @user = User.find_by_email(params[:email])
    if @user && @user.authenticate(params[:password])
      session[:user_id] = @user.id
      redirect_to "/products/index"
    else
      flash[:error] = "Invalid Credentials"
      redirect_to "/"
    end
  end

  def destroy
    session.clear
    redirect_to "/"
  end

end
