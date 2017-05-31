class ProductsController < ApplicationController
  def index
    @products = Product.all
    @sold_items = Purchase.all

    @total_sold = 0
    @total_purchased = 0
    @total_not_sold = 0
    @purchases = Purchase.where('user_id=?', current_user.id)

    @myshoes = Product.where('user_id=?', current_user.id) # getting all unsold products for current_user
    @unsold = [] # getting all unsold products for current_user
    @myshoes.each do |shoe| # getting all unsold products for current_user
      if Purchase.all.where('product_id=?', shoe.id).length == 0
        @unsold << shoe
      end
    end
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

  def all_products # ALL PRODUCTS PAGE
    @shoes = Product.all
    @purchases = Purchase.all
  end

  def buy
    @user = User.find(session[:user_id])
    @product = Product.find(params[:id])
    # @product_id = Product.find(params[:id])

    if @user.id === @product.user_id
      redirect_to :back

    else
      Sell.create(user: @product.user, product: @product)
      # neep user: prodocut
      Purchase.create(user: @user, product: @product)
      if @product.valid?
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
