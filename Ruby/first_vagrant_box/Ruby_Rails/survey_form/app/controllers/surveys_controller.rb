class SurveysController < ApplicationController
  def index
    # Set session count to zero if it doesnt exist yet
    session['count'] ||=0
  end

  def process_money
    # increment the session count upon submission of the form
    session['count'] = session['count'] + 1

    # save the post data (params[:survey])
    session[:result] = params[:survey]

    # save success message to flash to show it once
    flash[:success] = "Thanks for submitting this form! You have submitted this form #{session[:count]} time(s) now."

    # To prevent submission of FORM withpage reload
    redirect_to '/surveys/result'
  end

  def result
    # Save the data variable accessble in the count
    @result = session[:result]
  end
end

#   def new
#   end
#
#   def create
#     @dojo_survey = Dojo.create(params[:id]).update(name:params[:name], age: params[:age])
#   end
#
#   def show
#   end
#
#   def edit
#   end
#
#   def update
#   end
#
#   def destroy
#   end
# end
