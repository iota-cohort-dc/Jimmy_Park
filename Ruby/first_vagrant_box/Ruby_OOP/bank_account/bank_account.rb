# We are going to create a BankAccount class.
# This class will recreate some of the common account transactions that normally occur for a bank account
# such as displaying your account number,
# checking and savings amount,
# total amount. Of course,
# there are also methods to invoke such as depositing a check, checking your balance, withdrawing money

class BankAccount
  attr_reader :checking_balance, :savings_balance, :account_number, :total_balance

  @@bank_accounts = 0

  def self.show_total_accounts
    puts @@bank_accounts
  end

  def initialize(initial_checking, initial_savings) # will only run when new instance created...
                # initial_checking=0,initial_savings=0 . this creates default balance
    puts "Successfully created a new account"
    @account_number = generate_account_number
    @checking_balance = initial_checking
    @savings_balance = initial_savings
    # @total_balance = @checking_balance + @savings_balance
    @interest_rate = 0.01
    @@bank_accounts += 1
  end

  def show_all_balance
    puts "Checking Balance: #{@checking_balance}"
    puts "Savings Balance: #{@savings_balance}"
    puts "Total Balance: #{@checking_balance + @savings_balance}"
  end

  def account_info
    puts "Account Number: #{@account_number}"
    puts "Interest Rate: #{@interest_rate}"
    show_all_balance
  end

  def deposit(account, amount)
    if account.downcase == "checking"
      @checking_balance += amount
      puts "Successfully deposited into Checking Account"
    elsif account.downcase == "savings"
      @savings_balance += amount
      puts "Successfully deposited into Savings Account"
    else
      puts "Please specify which account (checking or savings)"
    end
  end

  def withdrawl(account, amount)
    if account.downcase == "checking"
      if amount > @checking_balance
        puts "You broke"
      else
        @checking_balance -= amount
      end
    elsif account.downcase == "savings"
      if amount > @savings_balance
        puts "not Today!!"
      else
        @savings_balance -= amount
      end
    else
      puts "You didnt put the right account name, fool (checking or savings)"
    end
  end

  private
    def generate_account_number
      rand(1000..9999)
    end
end
daniel = BankAccount.new(500,10)
daniel.show_all_balance
# puts "*"*60
# daniel.account_info
daniel.deposit("checking", 10)
# daniel.account_info
# daniel.withdrawl("checking", 100)
# daniel.show_all_balance
# daniel.show_total_accounts
# judy = BankAccount.new(500, 30)
# barbara = BankAccount.new(1000,500)
BankAccount.show_total_accounts
