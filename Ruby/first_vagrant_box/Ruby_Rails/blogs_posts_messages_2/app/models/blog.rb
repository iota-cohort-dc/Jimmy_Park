class Blog < ActiveRecord::Base
  has_many :owners
  has_many :posts
  has_many :users, through: :owners
  has_many :user_posts, through: :posts, source: :user

  has_many :comments, as: :commentable

  validates :name, presence: true, length: { in: 2..50 }
  validates :description, presence: true, length: { in: 10..100 }

end
