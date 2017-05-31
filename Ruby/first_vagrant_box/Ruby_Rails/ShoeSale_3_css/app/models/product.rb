class Product < ActiveRecord::Base
  belongs_to :user

  validates :name, presence: true, length: { minimum: 2 }
  validates :amount, presence: true


  def total_spent
    sum(:amount)
  end


end
