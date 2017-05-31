class ApplicationController < ActionController::Base
  # Prevent CSRF attacks by raising an exception.
  # For APIs, you may want to use :null_session instead.
  protect_from_forgery with: :exception

  def current_user # makes it available in the controller
    User.find(session[:user_id]) if session[:user_id]
  end

  helper_method :current_user
  # helper_method makes current_user available in the views
end
