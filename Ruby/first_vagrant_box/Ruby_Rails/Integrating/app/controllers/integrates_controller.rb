class UsersController < ApplicationController
  def index
    @users = User.all
  end

  def create
    User.create(name: params[:name], age: params[:age])
    redirect_to '/users'
  end

  def show
    @user = User.find(params[:id])
  end

  def edit
    @user = User.find(params[:id])
  end

  def update
    User.find(params[:id]).update(name:params[:name], age:params[:age])
    redirect_to '/users'
  end

  def destroy
    User.find(params[:id]).destroy
    redirect_to '/users'
  end
end
