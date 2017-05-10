require_relative 'bank_account'
RSpec.describe BankAccount do
  before(:each) do
    @account1 = BankAccount.new(500,500)
    @account2 = BankAccount.new(1000,1000)
  end

  it 'has a getter method for checking balance' do
# IT has a getter method for checking balance, now DO ...
    expect(@account1.checking_balance).to eq(500)
# we EXPECT account1 checking balance to EQual 500
  end

  it 'has a getter method for total account balance' do
    expect(@account1.total).to eq("1000")
  end

  it 'has a method that allows user to withdrawal cash' do
    @account1.withdrawal("checking", 100)
# we first do account1 WITHDRAWAL in checking of 100, then....
    expect(@account1.checking_balance).to eq(400)
# we EXPECT account1 checking balance to EQual 400
  end

  it 'raises an error if a user tries to withdraw more money than in account' do
    expect{@account1.withdrawal("checking",1000)}.to raise_error("You broke")
# we EXPECT\when we WITHDRAWAL from checking of 1000 TO RAISE ERROR string "You broke"
  end

  it 'raises an error when the user attempts to retrieve the total number of bank accounts' do
    expect{@account1.num_accounts}.to raise_error(NoMethodError)
# we EXPECT/when we look for num_accounts TO RAISE ERROR NoMethodError
  end

  it 'raises an error when user attemps to set interest rate' do
    expect{@account1.interest_rate = 0.5}.to raise_error(NoMethodError)
  end

end
