



# <------------------------ COMMENTING -------------------------->
# pound symbold is for one line

=begin
  equal begin starts a long multiline comment
  long comment
  another
  equal end, ends the long multiline comment
=end
# <--------------------------- PUTS ----------------------------->
# puts "hello"
# puts "coding"
# puts "dojo"
# print "hello"
# print "ah ha"

# BEGIN {
#   puts "This is AT the begin block"
# }
# END {
#   puts " This is AT the end block"
# }
# x = 5
# y = 10
# z = x + y
# puts z

# first_name = "Jimmy"
# last_name = "Park"
# puts "Your name is "
# puts first_name
# puts last_name
# puts "Your name is ", first_name, last_name
# puts "Your name is " + first_name + " " + last_name
# puts "Your first name is #{first_name} and last name is #{last_name}"
# puts "Your first name is %s and last name is %s" %[first_name,last_name]
# <------------------------ PUTS NUMBERS -------------------------->
# z = 50
# puts "Value of z is #{z}"
# puts "Value of z is %d" %[z]
# puts "Value of z is %d" % z

# %s  = string
# %d  = decimal
# %f  = float
# <------------------------------- \ ------------------------------>
# puts "I am 5'10\" tall" #use \ to display the " in a string
# puts "\t\t I am\n 5'10\" tall" #\t adds tab spacing, \n adds new line

# x = puts "hello world"
# puts x
# "I am an instance of ".class # run this line in irb

# x = "coding dojo"
# puts x[2]
# puts x.include?("dojo") # case sensitive function

# puts "This word has the word 'Dojo'" if x.include?("Dojo")
# puts "This word has the word 'Dojo'" if x.include? "Dojo"

# x = "john, charles, matt, joe"
# puts x.split(",") #put each name into its own array
# puts x.split(",").to_s #put each name into its own array and puts into array format

# x = "john, charles, matt, joe"
# y = ""
# puts "Y is empty" if y.empty?
# # if y is empty then print out the string "Y is empty"
# # <------------------------ FILTERS -------------------------->
# name = "frobe"
# puts name.capitalize
# puts name.upcase
# puts name.downcase
# puts name.titleize
#
# puts "hello".split
# puts "hello".split("")
# puts "oscar@gmail.com".split("@")
#
# str = "bar"
# str[0] = "c"
# puts str
# <------------------------ CONDITIONALS -------------------------->
# x = 1
# if x > 2
#   puts "x is greater than 2"
# elsif x < 2 and x > 0
#   puts "x is 1"
# else
#   puts "I can't guess the number"
# end

# (((OR)))

# x = 1
# if (x > 2)
#   puts "x is greater than 2"
# elsif (x < 2 and x > 0)
#   puts "x is 1"
# else
#   puts "I can't guess the number"
# end

# x = 5
# puts "x is not 2" if x != 2
# puts "x is greater than 2" if x > 2
#
# puts "x is not 2" unless x == 2
#<---------------------- SWITCH CASE -------------------------->
# age = 5
#
# case age
# when 0..2
#   puts "baby"
# when 3..6
#   puts "little child"
# when 7..12
#   puts "child"
# when 13..18
#   puts "youth"
# else
#   puts "adult"
# end
#<---------------------- SWITCH CASE -------------------------->
# age = 22
# if age >= 21
#   puts "Welcome to the party"
# else
#   puts "Not yet"
# end
#<-------------------- CONDITIONALS elif ---------------------->
# number = 15
# if number % 3 == 0 && % 5 == 0
#   puts "FizzBuzz"
# elsif number % 3 == 0
#   puts "Fizz"
# elsif number % 5 == 0
#   puts "Buzz"
# end
#<---------------------- CONDITIONALS ! not -------------------------->
# if !(age < 21)
#   puts "Welcome to the party"
# else
#   puts "Not yet"
# end
#<---------------------- CONDITIONALS unless -------------------------->
# unless age < 21
#   puts "Welcome to the party"
# else
#   puts "Not yet"
# end
#<---------------------- CONDITIONALS NIL -------------------------->
# in Ruby only 2 things are False: nil and false
# <------- positive energy -------|
# if ""
#   puts "I am positive"
# end
# if 0
#   puts "I am positive"
# end
# <------- negative energy -------|
# unless nil
#   puts "I am negative"
# end
# unless false
#   puts "I am negative"
# end
#<---------------------- inline CONDITIONALS -------------------------->
# puts "I am positive" if "hello"
# puts "I am positive" if 24
# puts "I am negative" unless nil
# puts "I am negative" unless false
#<---------------------------- LOOPS ---------------------------------->
#  $ infront of variable means global
# $i = 0
# $num = 5
# begin
#   puts ("Inside the loop i = #{$i}")
#   $i += 1
# end while $i < $num
#
# $i = 0
# $num = 5
# begin
#   puts "Inside the loop i = #{$i}"
#   $i += 1
#   puts "$i is now 3" if $i == 3
# end while $i < $num

# $i = 0
# $num = 5
# begin
#   puts "Inside the loop i = #{$i}"
#   puts "$i is now 3" unless $i == 3
#   $i += 1
# end while $i < $num

i = 1
num = 256
while i < num do
   puts "#{i}"
   i +=1
end

# i = 0
# num = 5
# while i < num do
#   puts "Inside the loop i = #{i}"
#   i += 1
#   break if i == 2
# end

#<---------------------------- LOOP Range ---------------------------------->
# for i in 0..5
#   puts "Value of local variable is #{i}"
# end
#
# for i in 0..5
#   puts "Value of local variable is #{i}"
#   break if i == 2
# end
# for i in 0..5
#   puts "Value of local variable is #{i}"
# end

# for i in 0..5
#   puts "Value of local variable is #{i}"
#   puts "i is now 3!!" if i == 3
# end

# for i in 0..5
#   next if i == 2
#   puts "Value of local variable is #{i}"
# end
#<---------------------------- RUBY METHODS ---------------------------------->
# def hello_world
#   puts "hello world"
# end
# hello_world          # this line invoked the method
# <-------------input-----------|
# def say_hello name1, name2
#   puts "hello, #{name1} and #{name2}"
# end
# say_hello "oscar", "eduardo" # => "hello, oscar and eduardo"

# def say_hello(name1, name2)
#   puts "hello, #{name1} and #{name2}"
# end
# say_hello("oscar", "eduardo") # => "hello, oscar and eduardo"
# <-------------default-----------|
# def say_hello name1="oscar", name2="shane"
#   puts "hello, #{name1} and #{name2}"
# end
# say_hello "oscar"    # => "hello, oscar and shane"
# <-------------ouput-----------|
# <---------default return-----------|
# def say_hello name1="oscar", name2="shane"
#   "hello, #{name1} and #{name2}"
# end
# puts say_hello "oscar", "eduardo"   # => "hello, oscar and eduardo"
# <---------default return-----------|
# def say_hello name1, name2
#   if name1.empty? or name2.empty?
#     return "Who are you?!"
#   end
#   # Doesn't reach the last line because we used return
#   "hello, #{name1} and #{name2}"
# end
# puts say_hello "", ""
# #<---------------------------- QUIZ ---------------------------------->
# puts "RUBY!" * 2
# puts "Chunky" << "Bacon"
# puts "Chunky"[2..3]
# puts "ruBy".capitalize
# puts "".empty?
# puts "team".include?("i")
# puts "matz".length
# #<-----------------------GUESS THE NUMBER------------------------------>
# def guess_number guess
#     number = 25
#     if guess == number
#       puts "You got it!"
#     elsif guess > number
#       puts "Guess was too high!"
#     else
#       puts "Guess was too low!"
#     end
# end
# puts guess_number 15
# puts guess_number 132
# puts guess_number 12
# puts guess_number 1
# puts guess_number 25
# #<----------------------- ARRAYS ------------------------------>
