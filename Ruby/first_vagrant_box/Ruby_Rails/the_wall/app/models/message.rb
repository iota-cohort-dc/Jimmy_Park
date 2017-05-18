class Message < ActiveRecord::Base
  belongs_to :user

  validates :content, presence: true, length: { in: 10..100 }

end
