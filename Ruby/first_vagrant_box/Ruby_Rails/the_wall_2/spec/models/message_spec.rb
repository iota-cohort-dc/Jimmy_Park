require 'rails_helper'

RSpec.describe Message, type: :model do
  before(:each) do
    @user = build(:user)
  end

  context "With valid attributes" do
    it "should save" do
      expect(build(:message, user: @user)).to be_valid
    end
  end

  context "With invalid attributes" do
    it "should not save if message field is blank" do
      expect(build(:message, message: "", user: @user)).to be_invalid
    end

    it "should not save if message filed is less than 10 characters" do
      expect(build(:message, message: "Hello", user: @user)).to be_invalid
    end

    it "should not save if there is no user references" do
      expect(build(:message)).to be_invalid
    end
  end
end
