class Post < ActiveRecord::Base
  belongs_to :user
  belongs_to :blog
  has_many :messages

  has_many :comments, as: :commentable

  validates :title, :content, presence: true, length: { in: 5..1000 }


end
