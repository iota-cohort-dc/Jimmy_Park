class User < ActiveRecord::Base
  has_many :messages
  has_many :comments

  validates :username, presence: true, length: { in: 6..20 }

end
