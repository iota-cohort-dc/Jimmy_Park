class Message < ActiveRecord::Base
  belongs_to :user
  has_many :comments

  validates :content, presence: true, length: { 10..500 }
  # length: { minmum 3 }
  
end
