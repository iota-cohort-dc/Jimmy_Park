class RubiesController < ApplicationController

  def index
    render text: "def index"
    # or you can route this to the views fold   /rubies/index
  end

  def hello
    render text: "def hello"
  end

  def joe
    render text: "def joe"
  end

  def say
    unless params[:name]
      render text: "Saying Hello!"
    else
      if params[:name] == "michael"
        redirect_to "/say/hello/joe"
      else
        render text: "Saying Hello #{params[:name]}!"
      end
    end
  end

    # def none
    #   render text: "What do you want me to say?"
    # end

  def times
    session[:count] ||= 0
    render text: "you have visited this url #{session[:count] += 1} time(s)"
  end

  def restart
    session[:count] = 0
    render text: 'Destroyed the session'
  end


end
