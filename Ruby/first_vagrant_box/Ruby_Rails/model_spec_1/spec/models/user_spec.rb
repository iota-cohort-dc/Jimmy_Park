require 'rails_helper'
RSpec.describe User do
  # This is our control
  context "With valid attributes" do
    it "should save" do
      user = User.new(
        first_name: 'shane',
        last_name: 'chang',
        email: 'schang@codingdojo.com'
      )
      expect(user).to be_valid
    end
  end

  context "With invalid attributes" do
    it "should not save if first_name field is blank" do
      user = User.new(
            first_name: '',
            last_name: 'chang',
            email: 'schang@codingdojo.com'
        )
      expect(user).to be_invalid
    end

    it "should not save if last_name field is blank" do
      user = User.new(
            first_name: 'Tom',
            last_name: '',
            email: 'tom@email.com'
        )
      expect(user).to be_invalid
    end

    it "should not save if email already exists" do
      user = User.new(
            first_name: 'Larry',
            last_name: 'Smith',
            email: 'tom@email.com'
        )
      user2 = User.new(
            first_name: 'Gretchen',
            last_name: 'Reese',
            email: 'tom@email.com'
       )
    end

    it "should not save if invalid email format" do
      user = User.new(
            first_name: 'Jane',
            last_name: 'Smith',
            email: 'jsmith.com'
      )
    end

  end
end
# above was a test from the platform
