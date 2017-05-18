class DojosController < ApplicationController
  def index
    @dojos = DojoDojo.all
  end

  def new
  end

  def create
    @check = DojoDojo.create(branch:params[:branch], street:params[:street], city:params[:city], state:params[:state] )


    if @check.valid?

      # redirect_to root_url, notic: "you creaTED DOJO!"
    redirect_to "/"
    else
      flash[:errors] = @check.errors.full_messages
      redirect_to :back
    end
  end

  def show
    @dojo = DojoDojo.find(params[:id])
    @students = Student.where(dojo_dojo_id: @dojo)
    # render 'dojos/show'
  end

  def delete
    DojoDojo.find(params[:id]).delete
    redirect_to "/"
  end

  def edit
    @dojo = DojoDojo.find(params[:id])
    render "dojos/edit"
  end

  def update
    @dojo = DojoDojo.find(params[:id])
    @dojo.update(dojo_params)
    redirect_to "/"
  end

  private
    def dojo_params
      params.require(:dojos).permit(:branch, :street, :city, :state)
    end

end
