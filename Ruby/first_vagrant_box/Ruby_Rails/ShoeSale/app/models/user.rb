class User < ActiveRecord::Base
  has_secure_password

  belongs_to :product
  has_many :products

  EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i

  validates :first_name, presence: true, length: { minimum: 2}
  validates :last_name, presence: true, length: { minimum: 2}
  validates :email, presence: true, uniqueness: { case_sesitive: false }, format: { with: EMAIL_REGEX }
  validates :password, presence: true, length: { minimum: 6 }, :on => :create

  before_save :email_downcase

  def email_downcase
    self.email.downcase
  end


end
