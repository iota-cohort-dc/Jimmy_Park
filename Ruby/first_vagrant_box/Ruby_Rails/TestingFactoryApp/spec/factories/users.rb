FactoryGirl.define do
  factory :user do
    last_name "Doe"
    admin false
    trait :male do
      first_name "John"
      email "john@doe.com"
    end
    trait :female do
      first_name "Jane"
      email "jane@doe.com"
    end
    trait :admin do
      admin true
    end
  end
end
