class Product < ActiveRecord::Base
  belongs_to :user
  has_many :users

  validates :product, presence: true, length: { minimum: 2 }
  validates :amount, presence: true

end
