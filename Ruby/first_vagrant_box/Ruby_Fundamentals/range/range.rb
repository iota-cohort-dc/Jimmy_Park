x = (1..5)
puts "Class Name: #{x.class}"
puts "It does include 3!" if x.include? 3

puts "The last number of this range is " + x.last.to_s
puts "The maximum number of this range is " + x.max.to_s
puts "The minimum number of this range is " + x.min.to_s

y = ('a'..'z')
puts y.to_a.shuffle.to_s


# include? (value) # either comes out true or false
puts (5..50).include?(40)
puts (1..100).include?(101)
puts (1..100).include?(0)
puts (1..100).include?(50)

# .last  # returns the last object in range
puts (1..100).last # this prints out 100
puts (1..500).last # this prints out 500
puts (50..2323).last # this prints out 2323
puts (245..14321).last # this prints out 14321

# .max  # returns the maximum value in range
puts (1..100).max  # this prints out 100
puts (50..500).max # this prints out 500
puts (1010..2020) # this prints out 2020

# .min  # returns the minimum value in range
puts (1..100).min # this prints out 1
puts (5..100).min # this prints out 5
