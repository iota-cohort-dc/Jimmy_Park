class ProductsController < ApplicationController
  def index
    @products = Product.all
    # @sold = Sell.where(user_id: current_user.id)
    @sold = Sell.where.not(user_id: current_user.id)
    # @sold = Sell.all
    # @purchase = Purchase.where(user: current_user.id)
    @purchase = Purchase.where.not(user: current_user.id)
    # @purchase = Purchase.all
  end

  def create
    @user = User.find(session[:user_id])
    @product = Product.create(name: params[:name], amount: params[:amount], user: @user)
    if @product.valid?
      redirect_to "/products/index"
    else
      flash[:errors] = @product.errors.full_messages
      redirect_to :back
    end
  end

  def all_products
    @all_products = Product.all

  end

  def buy
    @user = User.find(session[:user_id])
    @product = Product.find(params[:id])
    # @product_id = Product.find(params[:id])

    if @user.id === @product.user_id
      redirect_to :back

    else
      @products  = Product.find(params[:id])
      Sell.create(user_id: @product.user.id, product_id: @product.id)
      # Sell.create(user_id: current_user.id, product_id: @product.id)
      # Purchase.create(user_id: current_user.id, product_id: @product.id)
      # Purchase.create(user_id: current_user., product_id: @product.id)
      Purchase.create(user_id: @product.user.id, product_id: @product.id)
      @products.update_attributes(user: @user, name: @product.name, amount: @product.amount)

      if @products.valid?
        redirect_to :back
      else
        flash[:errors] = @event.errors.full_messages
        redirect_to :back
      end

    end

  end

  def show
  end

  def edit
  end

  def update
  end

  def destroy
    @product = Product.find(params[:id])
    @product.destroy
    redirect_to :back
  end
end
