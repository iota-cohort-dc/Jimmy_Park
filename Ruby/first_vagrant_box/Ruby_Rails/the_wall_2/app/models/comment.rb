class Comment < ActiveRecord::Base
  belongs_to :user
  belongs_to :message

  validates :content, presence: true, length: { 10..500 }
  # length: { minmum 3 }
  
end
