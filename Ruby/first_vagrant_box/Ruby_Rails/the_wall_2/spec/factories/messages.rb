# FactoryGirl.define do
#   factory :message do
#     content "MyString"
#     user nil
#   end
# end


FactoryGirl.define do
  factory :message do
    message "This message is very long"
    user nil
  end
end
