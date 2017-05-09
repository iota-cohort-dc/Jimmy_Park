# <---------------------------basic 13 --------------------------->

# <---------------------------print 1-255--------------------------->
# def all_num
#   i = 1
#   num = 256
#   while i < num do
#      puts "#{i}"
#      i +=1
#   end  # ends the while loop
# end  # ends the function
# all_num  # this line invokes the function to run

# works!
# (1..255).each { |i| puts i }


# <---------------------------odd 1-255--------------------------->
# works!!
# print "odd 1-255"
#  (1..255).each {|value| puts value if value.to_f%2==0}

 # <---------------------------find sum--------------------------->
# print "sum"
# def find_sum
#   sum = 0
#   puts (1..255).inject { |sum, n| sum + n }
# end
# find_sum

# sum = 0
# def find_sum
#   (0..255).each { |i| puts sum+=i }
# end
# find_sum

# (((or)))

# sum = 0
# def find_sum
#   (0..255).each { |i| puts "#{sum += i}"}
# end
# find_sum

# (((or)))

# sum = 0
# (0..255).each { |i| puts "New Number: #{i} Sum: #{sum += i}"}

# (((or)))

# sum = 0
# (0..255).each { |i| puts "New Number: #{i} Sum: #{sum += i}"}

# <----------------------interating thru array--------------------->
# print each item in the array
# x = [1,3,5,7,9,13]
# x.each { |i| puts i }

# <--------------------------- find max --------------------------->
# find max and print it
# x = [1,3,5,7,9,13]
# # x = [-3, -5, -7]
# def find_max
#   max = []
#   x.each { |i| max = i if i > max} # this is not working
# end
# find_max

# (((or)))

# def find_max
#   puts [-3,-5,-7].max
# end
# find_max

# <-------------------------- get average ------------------------->

# arr = [2, 10, 3]
# puts arr.inject{ |sum,el| sum + el } / arr.size

#(((or)))

# arr = [2,10,3]
# puts arr.reduce(:+) / arr.length.to_f

# <---------------------- array with odd numbers -------------------->

# y = []
# puts (1..255).each {|i| y << i  if i.odd?}

# (((or)))

# i =1
# num = 255
# while i < num
#   if i.odd?
#     puts i
#     i += 1
#   else
#     i += 1
#   end
# end

# <-------------------------- greater than Y ------------------------->

# array = [1,3,5,7]
# y = 3
# arr = []
#
# array.each { |i| puts arr = i if i > y }

# <------------------------- square the values ------------------------>

# array = [1, 5, 10, -2]
# array.each { |i| puts i * i }

# <--------------------- eliminate Negative numbers -------------------->

# arr = [1, 5, 10, -2]
# puts arr.each_index { |index| arr[index] = 0 if arr[index] < 0 }

# <-------------------------- max min average -------------------------->

# arr = [1, 5, 10, -2]
# { max: arr.max, min: arr.min, average: arr.reduce(:+) / arr.length.to_f }

# <------------------------ shifting array values ----------------------->

# arr = [1, 5, 10, 7, -2]
# puts arr.rotate!(1)[arr.length-1] = 0

# <--------------------------- number to string -------------------------->

# arr = [-1, -3, 2]
# puts arr.each_index { |index| arr[index] = "Dojo" if arr[index] < 0 }
