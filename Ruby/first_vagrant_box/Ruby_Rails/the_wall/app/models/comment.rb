class Comment < ActiveRecord::Base
  belongs_to :user
  belongs_to :message

  validates :comment_content, presence: true


end
