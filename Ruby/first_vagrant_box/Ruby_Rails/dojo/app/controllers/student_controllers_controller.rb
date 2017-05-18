class StudentControllersController < ApplicationController
  def index
  end

  def new
    @dojo = DojoDojo.find(params[:dojo_id])
    @dojos = DojoDojo.all
  end

  def create
    dojo = DojoDojo.find(params[:dojo])
    puts "*"*40
    puts dojo
    # params[:dojo] is from <select name="dojo"> in new.html
    Student.create(first_name:params[:first_name], last_name:params[:last_name],email:params[:email], dojo_dojo_id: params[:dojo])
    # passing in the instance into the branch.

    redirect_to "/show/" + params[:dojo]
  end

  def edit
    @dojo = DojoDojo.find(params[:dojo_id])
    @student = Student.find(params[:id])
    puts "1-"*30
    # redirect_to
  end

  def show
    # puts params[:dojo_id] test this
    @dojo = DojoDojo.find(params[:dojo_id])
    # dojo_id is from the url
    # puts @dojo test this
    @student = Student.find(params[:id])
    # this is coming from the url that will find the student

  end

  def delete
    Student.find(params[:id]).delete
    redirect_to :back
  end

  def update
    puts "*"*50
    @student = Student.find(params[:id])
    @dojo = DojoDojo.find(params[:dojo_id])
    @student.update(first_name: params[:first_name], last_name: params[:last_name], email: params[:email])
    puts "*"*50
    # .update(:first_name params[:name], :last_name params[:last_name], :email params[:email],dojo_dojo_id: params[:dojo])
    # redirect_to "/"
    redirect_to "/" + "#{@dojo.id}" + "/student/show/" + "#{@student.id}"


  end
end
