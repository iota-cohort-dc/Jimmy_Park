require "rails_helper"

feature "creating a message" do
  before(:each) do
    # @user = create(:user)
    # @message = create(:message, user: @user)
    visit "/"

    fill_in "username", with: "codingdojo"
    click_button "Sign In"

    visit "/messages"

  end

  scenario "successfully creating a message" do
    fill_in "content", with: "This is my cool message"
    click_button "Post a Message"
    expect(current_path).to eq("/messages")

    message = Message.first

    date = message.created_at.strftime("%B #{message.created_at.day.ordinalize}, %Y")
    expect(page).to have_content("#{User.first.username} - #{date}")
    expect(page).to have_content(Message.first.content)
  end

  scenario "unsuccessfully creating a message when is blank" do
    fill_in "content", with: ""
    click_button "Post a Message"
    expect(current_path).to eq("/messages")
    expect(page).to have_content("")
  end

  scenario "unsuccessfully creating a message when is shorter than 10 character" do
    fill_in "content", with: "hello"
    click_button "Post a Message"
    expect(current_path).to eq("/messages")
    expect(page).to have_content("")
  end
end
