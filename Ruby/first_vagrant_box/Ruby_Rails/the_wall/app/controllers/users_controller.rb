class UsersController < ApplicationController
  def index

  end

  def create
    # User.find_by, can pass in a paramater
    # User.find, passes in an id

    # if user exists

    # else

    @users = User.find_by(username: params[:username])
    if @users.valid?
      redirect_to "messages/index"

    else
      @users = User.create(username: params[:username])
      if @users.valid?
        redirect_to "messages/index"

      else
        flash[:error]=@users.errors.full_messages # is an array of errors
        redirect_to "/"
      end
    end
  end
end
