require "rails_helper"

feature "signing in" do
  scenario "successfully signs in an user" do
    create(:user)

    visit root_path

    fill_in "username", with: "codingdojo"
    click_button "Sign In"
    expect(page).to have_content("Welcome #{User.first.username}")
    expect(current_path).to eq(messages_path)
  end

  scenario "unsuccessfully sign in a user" do
    visit root_path

    fill_in "username", with: "no one"
    click_button "Sign In"
    expect(page).to have_content("Could not find username")
    expect(current_path).to eq(root_path)
  end
end
