Rails.application.routes.draw do

  get '' => 'dojos#index'

  get 'new' => 'dojos#new'

  post 'create' => 'dojos#create'

  get 'edit/:id' => 'dojos#edit'

  patch 'update/:id' => 'dojos#update'

  get 'show/:id' => 'dojos#show'

  delete 'delete/:id' => 'dojos#delete'

# --------------------------------------|
# proper way @@ url convention @@

  get ':dojo_id/student' => 'student_controllers#index'
# @@  dojo/:dojo_id/student
  get ':dojo_id/student/new' => 'student_controllers#new'
# @@  dojo/:dojo_id/student/new
  post ':dojo_id/student/create' => 'student_controllers#create'
# @@  dojo/:dojo_id/student/create
  get ':dojo_id/student/show/:id' => 'student_controllers#show'
# @@  dojo/:dojo_id/student/:id/show
  get ':dojo_id/student/:id/edit' => 'student_controllers#edit'
# @@  dojo/:dojo_id/student/:id/edit
  delete ':dojo_id/student/:id' => 'student_controllers#delete'
# @@  dojo/:dojo_id/student/:id
  patch '/:dojo_id/student/:id' => 'student_controllers#update'
# @@  dojo/dojo_id/student/:id
# --------------------------------------|




  # The priority is based upon order of creation: first created -> highest priority.
  # See how all your routes lay out with "rake routes".

  # You can have the root of your site routed with "root"
  # root 'welcome#index'

  # Example of regular route:
  #   get 'products/:id' => 'catalog#view'

  # Example of named route that can be invoked with purchase_url(id: product.id)
  #   get 'products/:id/purchase' => 'catalog#purchase', as: :purchase

  # Example resource route (maps HTTP verbs to controller actions automatically):
  #   resources :products

  # Example resource route with options:
  #   resources :products do
  #     member do
  #       get 'short'
  #       post 'toggle'
  #     end
  #
  #     collection do
  #       get 'sold'
  #     end
  #   end

  # Example resource route with sub-resources:
  #   resources :products do
  #     resources :comments, :sales
  #     resource :seller
  #   end

  # Example resource route with more complex sub-resources:
  #   resources :products do
  #     resources :comments
  #     resources :sales do
  #       get 'recent', on: :collection
  #     end
  #   end

  # Example resource route with concerns:
  #   concern :toggleable do
  #     post 'toggle'
  #   end
  #   resources :posts, concerns: :toggleable
  #   resources :photos, concerns: :toggleable

  # Example resource route within a namespace:
  #   namespace :admin do
  #     # Directs /admin/products/* to Admin::ProductsController
  #     # (app/controllers/admin/products_controller.rb)
  #     resources :products
  #   end
end
