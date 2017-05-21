class MessagesController < ApplicationController
  def index
    @user = User.find(session[:user])
    @messages = Message.all
    @comment = Comment.all
  end
  # def new
  # end
  def create
    @user = User.find(session[:user])
    @messages = Message.create(content: params[:content], user: @user)
    redirect_to :back
  end

  def comment

    user = User.find(session[:user])
    message = Message.find(params[:message_id])
    comment = Comment.create(comment_content: params[:comment_content], message: message, user: user)

    redirect_to :back
  end
end
