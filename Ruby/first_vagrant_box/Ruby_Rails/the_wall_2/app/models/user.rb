class User < ActiveRecord::Base
  has_many :messages
  has_many :comments

  validates :username, presence: true, length: { 3..20 }
  # length: { minmum 3 }
  validates :username, uniqueness: { case_sensitive: false }

end
