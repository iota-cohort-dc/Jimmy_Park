class User < ActiveRecord::Base
  has_secure_password

  has_many :comments
  has_many :events
  has_many :participates
  has_many :participate_event, through: :participates, source: :event
  has_many :event_comment, through: :comments, source: :user

  EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i

  validates :first_name, presence: true, length: { minimum: 2}
  validates :last_name, presence: true, length: { minimum: 2}
  validates :email, presence: true, uniqueness: { case_sesitive: false }, format: { with: EMAIL_REGEX }
  validates :password, presence: true, length: { minimum: 6 }, :on => :create
  validates :location, presence: true, length: { minimum: 2 }
  validates :state, presence: true

  before_save :email_downcase

  def email_downcase
    self.email.downcase
  end
end
