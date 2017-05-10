# print   puts

# declare variable
x = 3

# string interpolation
puts "my value is #{x + 2}"

# false and nil are false
# check if false
puts "it is false!" if !false
puts "it is false!" if !nil
puts "it is false!" unless nil
puts "it is false!" unless false

unless false
  puts "this is weiard"
end

unless 0
  puts "this is weird"
end

puts 3.to_s

puts 3.class

puts a = [1,2,3,4,5,6]
puts a.shuffle
puts a
puts a.shuffle!

p a  # puts into looks like array, on 1 line
print a.shuffle
puts

puts a
puts

for i in 0..5 #inclusive
  puts i
end

for i in 0...5 #exclusive
  puts i
end

puts "*" * 20

a = [8,5,3,4,5]
 for i in a
   puts i
 end

 puts "*" * 20

 a = [8,5,3,4,5]
  for i in a
    puts a[i]
  end

 # methods

def some_method a
  puts a
end
some_method a

def some_method (a)
  puts a
end
some_method (a)

puts "*" * 20
puts a.reject{|i| i < 2}

puts a.reject{|i| i % 2 == 0}

# objects
# class
puts "*" * 20


class Apple
  def initialize
    @color = "Red"
    # this is a setter
    # this is an attribute, @ global to this class
    @taste = "Delicious"
  end
  def get_color # this is a getter
    @color
  end
end

myApple = Apple.new
puts myApple
puts myApple.get_color
puts myApple

class Apple
  @@color = "Red"
    # this is a setter
    # this is an attribute, @ global to this class
  @@taste = "Delicious"

  def get_color # this is a getter
    @@color
  end
end

puts "*" * 20

class Apple
  attr_accessor :color
  def initialize(color)
    @color = color
  # this is a setter
  # this is an attribute,
  end
end
myApple = Apple.new "red"
puts myApple.color

myApple.color = "green"
puts myApple.color
