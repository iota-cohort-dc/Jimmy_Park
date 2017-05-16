class DojoDojo < ActiveRecord::Base
  validates :branch, :street, :city, :state, presence: true

  validates :state, length: { minimum: 2 }
end
