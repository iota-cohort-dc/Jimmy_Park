# RSpec.describe User, type: :model do
#   context "with invald attributes " do
#     it "should not be valid if username field is left blank" do
#       user = User.create(username: "")
#       expect(user).to be_invalid
#     end
#     it "should not be valid if username is not unique" do
#       User.create(username: "harrypotter")
#       user = User.new(username: "harrypotter")
#       expect(user).to be_invalid
#     end
#   end
# end
