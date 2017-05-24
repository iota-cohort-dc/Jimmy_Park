# this is testing LOGIN AND REGISTRATION
# in: SESSION CONTROLLER


require 'rails_helper'
feature 'User features' do
  before do
    # calling factory girl create method
    # @user = create(:user)


  end
  feature 'user sign-up' do
    before(:each) do
      visit '/users/new'
    end # end before

    # scenario 'visits sign-up page' do
    #   expect(page).to have_field('Name')
    #   expect(page).to have_field('Email')
    #   expect(page).to have_field('Password')
    #   expect(page).to have_field('Password_Confirmation')
    # end # end scenario

    scenario 'with improper inputs, redirects back to sign in and shows validations' do
      fill_in "Name", with: ""
      click_button 'Join'
      expect(current_pat).to eq('/users/new')
      expect(page).to have_text("can't be blank")
    end # end scenario

  #   scenario 'with proper inputs, create user and redirects to login page' do
  #     fill_in 'Email', with: 'curry@warriors.com'
  #     fill_in 'Name', with: 'curry'
  #     fill_in 'Password_Confirmation', with: 'password'
  #     click_button 'Join'
  #     expect(current_path).to eq('/sessions/new')
  #   end # end scenario
  # end # end feature
  #
  # feature 'user dashboard' do
  #   before do
  #     log_in
  #   end # end before
  #
  #   scenario 'displays user information' do
  #     expect(page).to have_text('#@user.name')
  #     expect(page).to have_link('Edit Profile')
  #   end # end scenario
  end # end feature


end # end all
