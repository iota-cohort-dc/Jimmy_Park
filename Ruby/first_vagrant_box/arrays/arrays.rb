a = ["Matz", "Guido", "Dojo", "Choi", "John"]
b = [5, 6, 9, 3, 1, 2, 4, 7, 8, 10]
c = ["Dojo", 9]
# a = [Matz Guido Dojo Choi John]
# puts a
# puts b
# puts c
# returns the first value or 0th index of the arrays
# puts a[0]
# puts a[1]

# .class
# puts b.class

# .shuffle and .join
# puts b.shuffle.join("-")

# .to_s  to string
# puts a.to_s

# add 2 strings together
# puts a+b
# x = a+b

# .to_s to string
# puts x.to_s

# add a and b together and minus index of c, then convert x to_s to string
# x = (a + b) - c
# puts x.to_s

# .delete
# a.delete("Choi")
# puts a

# .push
# puts a.push("*****", "?????", "%%%%%%")
# [1, 2, 3,].push(4).push(5)

# .pop
# puts a.pop
# puts a.pop(2)

# .length
# puts a.length
# puts "Length of a is #{a.length}"

# .join
# puts [ "a", "b", "c" ].join        #=> "abc"
# puts [ "a", "b", "c" ].join("-")   #=> "a-b-c"

# .reverse
# puts a.reverse!
# puts [1].reverse
# a.reverse_each {|x| print x, " " }  #reverse_each { |item| block } → ary

# .shuffle
# puts a.shuffle

# .at
# puts a.at(0)
# puts a.at(-1)

# .fetch
# puts a.fetch(0)
# puts a.fetch(-1)
# puts a.fetch(4,'cat')
# puts a.fetch(100) { |i| puts "#{i} is out of bounds" }

# .sort
# puts a.sort
# puts a.sort{ |x,y| y <=> x }
# puts a.sort{ |x,y| y <=> x }.reverse

# .insert
# puts a.insert(2,99)
# puts a.insert(-2,1,2,3)

# Alternative way of creating an array %w{}
# %w(foo bar) is a shortcut for ["foo", "bar"]
