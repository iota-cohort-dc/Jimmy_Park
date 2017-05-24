class SecretsController < ApplicationController
  def index
    @secrets = Secret.all
    @user = User.find(session[:user_id])
  end

  def new
  end

  def create
    secret = Secret.create(secret: params[:secret], user: current_user)
    redirect_to :back
  end

  def show
  end

  def edit
  end

  def update
  end

  def destroy
    @secret = Secret.find(params[:id])
    @secret.destroy
    redirect_to :back
  end
end
