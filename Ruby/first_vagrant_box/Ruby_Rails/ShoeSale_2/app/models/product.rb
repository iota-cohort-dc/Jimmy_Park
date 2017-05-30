class Product < ActiveRecord::Base
  belongs_to :user
  belongs_to :product
  # has_many :users

  validates :name, presence: true, length: { minimum: 2 }
  validates :amount, presence: true

end
