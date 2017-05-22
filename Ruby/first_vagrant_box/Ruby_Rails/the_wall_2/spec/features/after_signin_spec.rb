# require "rails_helper"
#
# feature "after sign in" do
#   before(:each) do
#     # @user = create(:user)
#     # # @comment = create(:message, user: @user)
#     # @message = create(:message, user: @user)
#     # @comment = create(:comment,message: @message, user: @user)
#
#
#     visit messages_path
#     fill_in "username", with: "codingdojo"
#     click_button "Sign In"
#   end
#
#   scenario "there should be a logout feature" do
#     expect(page).to have_link("Log out")
#     click_link("Log out")
#     expect(current_path).to eq(user_path)
#   end
#
#   scenario "there should be a form to create a message" do
#     expect(page).to have_field("content")
#     expect(page).to have_button("Post a Message")
#   end
#
#   scenario "there should be a form to create a comment if there's a message" do
#     expect(page).to have_field("content")
#     expect(page).to have_button("Post a Comment")
#   end
# end
