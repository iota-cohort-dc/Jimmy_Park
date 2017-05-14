class User < ActiveRecord::Base
  EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i
  validates :first_name, :last_name, presence: true, length: { in: 2..20 }
  validates :email, presence: true, uniqueness: { case_sensitive: false }, format: { with: EMAIL_REGEX }
  validates :age, numericality:{ only_integer: true}, presence: true, inclusion:{ in: 10..150 }
  # validates_numericality_of :age, less_than_or_equal_to: 100, greater_than: 0
end
