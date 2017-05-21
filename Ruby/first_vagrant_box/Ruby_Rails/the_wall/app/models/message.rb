class Message < ActiveRecord::Base
  belongs_to :user
  has_many :comments

  validates :content, presence: true, length: { in: 10..100 }

  validates :user, presence: true

end
