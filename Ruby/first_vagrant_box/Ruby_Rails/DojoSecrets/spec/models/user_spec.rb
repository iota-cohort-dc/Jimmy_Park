
# require 'rails_helper'
#
# RSpec.describe User, type: :model do
#   pending "add some examples to (or delete) #{__FILE__}"
# end
# This top portions was autogeneratied
# ---------------------------------------------
# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
# |       THIS TEST USER MODEL          |
# -----------------------------------------
# |       app/models/user.rb            |
# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
require 'rails_helper'
RSpec.describe User, type: :model do
  context "with valid attributes" do

    it "should save" do
      expect(build(:user)).to be_valid
    end

    it "automatically encrypts the password into the password_digest attributes" do
      expect(build(:user).password_digest.present?).to eq(true)
    end

    it "email as lowercase" do
      expect(create(:user, email: 'EMAIL@GMAIL.COM').email).to eq('email@gmail.com')
    end

  context "with invalid attributes should not save if" do

    it "name is blank" do
      expect(build(:user, name:"")).to be_invalid
    end

    it "email is blank" do
      expect(build(:user, email: "")).to be_invalid
    end

    it "email format is wrong" do
      emails = %w[@ user@ @example.com]
      emails.each do |email|
        expect(build(:user, email: email)).to be_invalid
      end
    end

    it "email is not unique" do
      create(:user)
      expect(build(:user)).to be_invalid
    end

    it "password is blank" do
      expect(build(:user, password: "")).to be_invalid
    end

    it "password doesn't match password_confirmation" do
      expect(build(:user, password_confirmation: 'notpassword')).to be_invalid
    end
  end
end
end
