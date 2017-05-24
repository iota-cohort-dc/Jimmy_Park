class UsersController < ApplicationController
  def index
    @secrets = Secret.all
  end

  def new
  end

  def create
    @users = User.create(name: params[:name], email: params[:email], password: params[:password], password_confirmation: params[:password_confirmation])

    if @users.valid?
      session[:user_id] = @users.id
      redirect_to "/users/#{@users.id}"
    else
      flash[:errors] = @users.errors.full_messages
      redirect_to :back
    end

  end

  def show
  end

  def edit
  end

  def update
  end

  def destroy
  end
end
