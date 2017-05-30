class Event < ActiveRecord::Base
  belongs_to :user

  has_many :comments
  has_many :participates
  has_many :user_participate, through: :participates, source: :user
  has_many :user_comment, through: :comments, source: :user

  validates :name, presence: true, length: { minimum: 2 }
  validates :location, presence: true, length: { minimum: 2 }
  validates :state, presence: true
  validates :date, presence: true
end
