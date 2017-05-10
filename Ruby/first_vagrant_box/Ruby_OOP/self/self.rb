
class Fixnum
  def who_am_i
    puts self
  end
end
class String
  def who_am_i
    puts self
  end
  def print_me
    p self
  end
end
puts"*"*60
4.who_am_i # => 4
15.who_am_i # => 15
"string".who_am_i # => "string"
"hello_world".who_am_i # => "hello_world"
"I am a new object".print_me
puts"*"*60

# -----------------------------------------------

class Mammal
  def initialize
    puts "I am alive"
  end
  def breath
    puts "Inhale and exhale"
  end

  def who_am_i
    # printing the current object
    puts self
  end
end
my_mammal = Mammal.new # => "I am alive"
my_mammal.who_am_i # => #<Mammal:0x007f9e86025dd8>
my_mammal.who_am_i.breath # => undefined method `breath' for nil:NilClass (NoMethodError)

# -----------------------------------------------

class Mammal
  def initialize
    puts "I am alive"
    self
  end
  def breath
    puts "Inhale and exhale"
    self
  end

  def who_am_i
    puts self
    self
  end
end
my_mammal = Mammal.new.who_am_i.breath
