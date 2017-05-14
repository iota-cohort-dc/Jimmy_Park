class Message < ActiveRecord::Base
  belongs_to :user
  belongs_to :post

  has_many :comments, as: :commentable

  validates :author, presence: true
  validates :message, presence: true, length: { in: 5..1000 }


end
