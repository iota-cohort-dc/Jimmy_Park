Rails.application.routes.draw do

  get '' => 'users#index'

  post 'users' => 'users#create'

  get 'users/logout' => 'users#logout'

# ---------------------------------------|

  get '/messages' => 'messages#index'
  #
  post 'messages/' => 'messages#create'   #create
  #
  post 'messages/:id/comment' => 'messages#comment'


end
