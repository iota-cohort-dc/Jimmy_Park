class User < ActiveRecord::Base
  has_secure_password

  has_many :secrets
  has_many :likes

  has_many :secrets_liked, through: :likes, source: :secret

  EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i
  validates :name, presence: true, length: { in: 2..20}
  validates :email, presence: true, uniqueness: { case_sesitive: false }, format: { with: EMAIL_REGEX }
  validates :password, presence: true, length: { minimum: 6 }

  before_save :email_downcase
  def email_downcase
    self.email.downcase
  end
end
