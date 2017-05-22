class User < ActiveRecord::Base
  has_secure_password

  EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i

  validates :name, presence: true
  validates :email, presence: true
  validates :email, uniqueness: { case_sensitive: false }
  validates :email, format: { with: EMAIL_REGEX }

  before_save :email_lowercase
  # prior to saving run this function

  def email_lowercase
    email.downcase!
    # make sure !, ! make is permanant
  end
end
# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
# |        THIS GETS TESTED BY          |
# -----------------------------------------
# |     spec/models/user_spec.rb        |
# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
