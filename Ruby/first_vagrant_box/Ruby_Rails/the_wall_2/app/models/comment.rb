class Comment < ActiveRecord::Base
  belongs_to :user
  belongs_to :message

  validates :content, presence: true, length: { minimum: 10 }
  # length: { minmum 3 }




  # validates :content, :user, :message, presence: true
  # validates :content, length: { minimum: 10 }

  # def self.with_users message_id
  #   Comment.joins(:user).where("message_id = ?", message_id).select(:id, :content, :created_at, :username)
  # end


end
