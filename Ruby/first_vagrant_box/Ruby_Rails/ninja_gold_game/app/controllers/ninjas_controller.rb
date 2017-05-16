class NinjasController < ApplicationController
  def index
    session[:gold] ||= 0
    session[:activity] ||= []
    render :index
  end

  def handle
    curr_time = Time.now

    if params[:building] == 'farm'
      currentAmt = rand(10..20)
      # session[:gold] += currentAmt
      session[:activity] << "Earned #{currentAmt} from Farm @ #{curr_time}"
    elsif params[:building] == 'cave'
      currentAmt = rand(5..10)
      # session[:gold] += currentAmt
      session[:activity] << "Earned #{currentAmt} from Cave @ #{curr_time}"
    elsif params[:building] == 'casino'
      currentAmt = rand(-50..50)
      # session[:gold] += currentAmt
      session[:activity] << "Earned #{currentAmt} from Casino @ #{curr_time}"
    elsif params[:building] == 'house'
      currentAmt = rand(10..20)
      # session[:gold] += currentAmt
      session[:activity] << "Earned #{currentAmt} from House @ #{curr_time}"
    end


    session[:gold] += currentAmt
    redirect_to "/ninjas"

  end

    def reset
      session[:gold] = nil
      session[:activity] = nil
      redirect_to "/ninjas"
    end
end


  # def farm
  #   curr_time = Time.now
  #   currentAmt = rand(10..20)
  #   session[:gold] += currentAmt
  #   session[:activity] << "Earned #{currentAmt} from Farm @ #{curr_time}"
  #   redirect_to "/ninjas"
  # end
  #
  # def cave
  #   curr_time = Time.now
  #   currentAmt = rand(5..10)
  #   session[:gold] += currentAmt
  #   session[:activity] << "Earned #{currentAmt} from Cave @ #{curr_time}"
  #   redirect_to "/ninjas"
  # end
  #
  # def casino
  #   curr_time = Time.now
  #   currentAmt = rand(-50..50)
  #   session[:gold] += currentAmt
  #   session[:activity] << "Earned #{currentAmt} from Casino @ #{curr_time}"
  #   redirect_to "/ninjas"
  # end
  #
  # def house
  #   curr_time = Time.now
  #   currentAmt = rand(10..20)
  #   session[:gold] += currentAmt
  #   session[:activity] << "Earned #{currentAmt} from House @ #{curr_time}"
  #   redirect_to "/ninjas"






  # def new
  # end
  #
  # def create
  # end
  #
  # def show
  # end
  #
  # def edit
  # end
  #
  # def update
  # end
  #
  # def delete
  # end
