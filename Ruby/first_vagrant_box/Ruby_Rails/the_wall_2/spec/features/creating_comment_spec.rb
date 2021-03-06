require "rails_helper"

feature "creating a comment" do
  before(:each) do
    # @user = create(:user)
    # @message = create(:message, user: @user)
    visit "/"

    fill_in "username", with: "codingdojo"
    click_button "Sign In"

    visit "/messages"

    fill_in "content", with: "This is my cool comment"
    click_button "Post a Message"

    visit "/messages"


  end

  scenario "successfully creating a comment" do
    fill_in "content", with: "This is a really cool comment"
    click_button "Post a Comment"
    expect(current_path).to eq("/messages")

    comment = Comment.first

    date = comment.created_at.strftime("%B #{comment.created_at.day.ordinalize}, %Y")
    expect(page).to have_content("#{User.first.username} - #{date}")
    expect(page).to have_content(Comment.first.content)
  end

  scenario "unsuccessfully creating a comment when is blank" do
    fill_in "content", with: ""
    click_button "Post a Comment"
    expect(current_path).to eq("/messages")
    expect(page).to have_content("Content can't be blank")
  end

  scenario "unsuccessfully creating a message when is shorter than 10 character" do
    fill_in "content", with: "hello"
    click_button "Post a Comment"
    expect(current_path).to eq("/messages")
    expect(page).to have_content("Content is too short (minimum is 10 characters)")
  end
end
