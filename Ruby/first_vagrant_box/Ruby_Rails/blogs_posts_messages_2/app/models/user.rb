class User < ActiveRecord::Base
  has_many :owners
  has_many :messages
  has_many :posts, dependent: :destroy
  has_many :blogs, through: :owners, dependent: :destroy
  has_many :blog_posts, through: :posts, source: :blog

  has_many :comments, as: :commentable

  EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i
  validates :first_name, :last_name, presence: true, length: { in:2..20 }
  validates :email, presence: true, uniqueness: { case_sensitive: false }, format: { with: EMAIL_REGEX }

end
