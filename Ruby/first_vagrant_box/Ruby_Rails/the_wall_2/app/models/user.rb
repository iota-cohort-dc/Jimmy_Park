class User < ActiveRecord::Base
  has_many :messages
  has_many :comments

  # length: { minmum 3 }

  validates :username, presence: true, length: { minimum: 5 }, uniqueness: { case_sensitive: false }


end
