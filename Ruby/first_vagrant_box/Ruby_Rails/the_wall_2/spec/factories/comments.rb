# FactoryGirl.define do
#   factory :comment do
#     content "MyString"
#     user nil
#     message nil
#   end
# end


FactoryGirl.define do
  factory :comment do
    content "This text is longer than 10 characters"
    user nil
    message nil
  end
end
