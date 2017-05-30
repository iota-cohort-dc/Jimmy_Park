class UsersController < ApplicationController
  def index
  end

  def new
  end

  def create
    @users = User.create(
      first_name: params[:first_name],
      last_name: params[:last_name],
      email: params[:email],
      location: params[:location],
      state: params[:state],
      password: params[:password],
      password_confirmation: params[:password_confirmation]
      )

      if @users.valid?
        session[:user_id] = @users.id
        redirect_to "/events/index"
      else
        flash[:errors] = @users.errors.full_messages
        redirect_to :back
      end
  end

  def login
    @user = User.find_by_email(params[:email])
    if @user && @user.authenticate(params[:password])
      session[:user_id] = @user.id
      redirect_to "/events/index"
    else
      flash[:error] = "Invalid Credentials"
      redirect_to "/"
    end
  end

  def show
  end

  def edit
  end

  def update
    @user = User.find(params[:id])
    @user.update_attributes(
      first_name: params[:first_name],
      last_name: params[:last_name],
      email: params[:email],
      location: params[:location],
      state: params[:state]
      )
    redirect_to "/events/index"

  end

  def destroy
    session.clear
    redirect_to "/"
  end
end
