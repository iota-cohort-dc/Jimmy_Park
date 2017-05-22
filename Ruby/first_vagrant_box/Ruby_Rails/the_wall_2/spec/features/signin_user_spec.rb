require "rails_helper"

feature "signing in" do
  scenario "successfully signs in an user" do
    # create(:user)

    visit "/"

    fill_in "username", with: "codingdojo"
    click_button "Sign In"
    expect(page).to have_content("Welcome #{User.first.username}")
    expect(current_path).to eq("/messages")
  end

  scenario "unsuccessfully sign in a user" do

    visit "/"
    fill_in "username", with: ""
    click_button "Sign In"
    expect(page).to have_content("Username can't be blank")
    expect(page).to have_content("Username is too short (minimum is 5 characters)")
    expect(current_path).to eq("/")
  end
end
