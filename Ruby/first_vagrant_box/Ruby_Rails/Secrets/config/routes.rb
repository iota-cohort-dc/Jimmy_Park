Rails.application.routes.draw do

  get '' => 'sessions#new' # homepage LOG IN

  get 'sessions/new' => 'sessions#new'

  post 'sessions/' => 'sessions#create'

  delete 'sessions/:id' => 'sessions#destroy'

  # ---------------------------------------

  get 'users/new' => 'users#new'  # sent from sessions/index
  get 'users/:id' => 'users#index' # users homepage not index
  post 'users' => 'users#create' # create new user

# ---------------------------------------

  get 'secrets' => 'secrets#index'

  post 'secrets' => 'secrets#create'

  delete 'secrets/:id' => 'secrets#destroy'

  # ---------------------------------------

  post 'likes/:id' => 'likes#create'

  delete 'likes/:id' => 'likes#destroy'

end
