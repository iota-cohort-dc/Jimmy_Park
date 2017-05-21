class MessagesController < ApplicationController
  def index # show messages index page
    @user = User.find(session[:user])
    @messages = Message.all
    @comments = Comment.all
  end

  def create # create new message
    @user = User.find(session[:user])
    @messages = Message.create(content: params[:content], user: @user)
    redirect_to :back
  end

  def comment # create new comment
    user = User.find(session[:user])
    message = Message.find(params[:message_id])
    comment = Comment.create(content: params[:content], user: user, message: message)
    redirect_to :back
  end

end
