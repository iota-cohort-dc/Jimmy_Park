class TimesController < ApplicationController

  def main
    @time = (DateTime.now).strftime "%m/%d/%Y %I:%M %p"
       render "times/index.html.erb"
  end

  # HTML, could have done it this way
  # @time = Time.new
  #   <!-- <h3><%= @time.strftime("%b %d, %Y") %></h3>
  # <h3><%= @time.strftime("%I:%M %p") %></h3> -->



  # def index
  # end
  #
  # def new
  # end
  #
  # def create
  # end

  # def show
  # end
  #
  # def edit
  # end
  #
  # def update
  # end
  #
  # def destroy
  # end
end
