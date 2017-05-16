class DisplayController < ApplicationController

  def index
    @users = User.all
    render json: @users
  end

  def new
    render 'display/index'
  end

  def create
    User.create(name: params[:name])
    redirect_to "/users"
  end

  def show
    # @users = User.find(params[:id])
    # render json: @users
    # ((or))
    render json: User.find(params[:id])
  end

  def edit
    @user = User.find(params[:id])
  end

  def update
    User.find(params[:id]).update(name:params[:name], age: params[:age])
  end

  def destroy
    User.find(params[:id]).destroy
    redirect_to '/users'
  end

  def total
    # render json: { total: User.count }

    render text: "This is just a jsontext"
  end

end



# def users
# end
