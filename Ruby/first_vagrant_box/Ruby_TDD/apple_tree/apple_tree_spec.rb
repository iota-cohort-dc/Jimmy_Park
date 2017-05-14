require_relative 'apple_tree'

RSpec.describe AppleTree do
  before(:each) do
    @apple1 = AppleTree.new
  end

  it 'age has a getter and setter for age' do
    expect(@apple1.age).to eq(0)
  end

  it "height has a getter attribute" do
    expect(@apple1.height).to eq(10)
  end

  it "apple_count has getter attribute" do
    expect(@apple1.apple_count).to eq(0)
  end

  it "year_gone_by add 1 year to age" do
    @apple1.year_gone_by
    expect(@apple1.age).to eq(1)
  end

  it "height increase ten percent" do
    @apple1.year_gone_by
    expect(@apple1.height.floor).to eq(11)
  end

  it "increases apple count by 2 if apple is betweeen 4-10" do
    5.times{@apple1.year_gone_by}
    expect(@apple1.apple_count).to eq(4)
  end

  it "does not grow apples if tree is under 3 years " do
    2.times{@apple1.year_gone_by}
    expect(@apple1.apple_count).to eq(0)
  end

  it "does not grow apples if tree is over 10" do
    11.times{@apple1.year_gone_by}
    expect(@apple1.apple_count).to eq(14)
  end

  it "changes apple count to zero with pick_apples method" do
    5.times{@apple1.year_gone_by}
    @apple1.pick_apples
    expect(@apple1.apple_count).to eq(0)
  end

puts"*"*60
end
