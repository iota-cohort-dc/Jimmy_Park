class LikesController < ApplicationController
  def index
  end

  def new
  end

  def create
    Like.create(user: current_user, secret: Secret.find(params[:id]))
    redirect_to :back
  end

  def show
  end

  def edit
  end

  def update
  end

  def destroy
    Like.find_by(user: current_user, secret: Secret.find(params[:id])).destroy
    redirect_to :back
  end
end
