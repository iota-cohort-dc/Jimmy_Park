class Post < ActiveRecord::Base
  has_many :messages, dependent: :destroy
  # dependent: :destroy, if we delete a post, all the messages linked to that Post are dependent on that Post
  # if you don't put. dependent: :destroy, if you delete a Post, the messages will stay in database
  belongs_to :blog
  validates :title, :content, presence: true
  validates :title, length: { in: 7..100 }
end
