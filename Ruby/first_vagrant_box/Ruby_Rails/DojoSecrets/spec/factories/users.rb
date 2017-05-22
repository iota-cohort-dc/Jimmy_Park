# example
# FactoryGirl.define do
#   factory :user do
#     name "MyString"
#     email "MyString"
#     password ""
#   end
# end

FactoryGirl.define do
  factory :user do
    name "Oscar Vazquez"
    email "oscar@gmail.com"
    password "password"
    password_confirmation "password"
  end
end
