class ProductsController < ApplicationController
  def index
    @products = Product.all
  end

  def new
  end

  def create
    @user = User.find(session[:user_id])
    @product = Product.create(product: params[:product], amount: params[:amount], user: @user)
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
    @product_id = Product.find(params[:id])

    if @user.id === @product.user_id
      puts "*"*80
      puts "Can't purchase your own stuff"
      puts "*"*80
      redirect_to :back

    else
      puts "@"*80
      puts "Ohh yes I can buy that"
      puts "@"*80
      @products  = Product.find(params[:id])
      @products.update_attributes(user: @user, product: @product.product, amount: @product.amount)
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
    params
  end
end
