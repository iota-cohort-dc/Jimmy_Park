# .any? { |obj| block } => true or false
# e.g. ["ant", "bear", "cat"].any? { |word| word.length >= 3 } # => true
if ANY of the words in the arr greater or equal to 3
#
# .each => calls block once for each element in ruby self, passing that element as a block parameter.
# e.g. ["ant", "bear", "cat"].each { |word| print word, "--" } # => ant--bear--cat--
print out each word with -- to it
#
# .collect { |obj| block } => returns a new array with the results of running block once for every element in enum
# e.g. (1..4).collect { |i| i*i } # => [1, 4, 9, 16]
range 1 thru 4:
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
# e.g. (1..4).collect { "cat" } # => ["cat", "cat", "cat", "cat"]
range 1 thru 4:
print out cat 4 times
#
# .detect/.find => returns the first for which block is not false.
# e.g. (1..10).detect { |i| i %5 == 0 and i % 7 == 0 } # => nil
range 1 thru 10:    if any of the remainder is == 0

# e.g. (1..100).detect { |i| i %5 == 0 and i % 7 == 0 } # => 35 
range 1 thr 10:     if any of the reminders is == 0
#
# .find_all { |obj| block } or .select { |obj| block } => returns an array containing all elements of enum for which block is not false
# e.g. (1..10).find_all { |i| i % 3 == 0 } # => [3, 6, 9]
#
# .reject { |obj| block } => opposite of find_all
# e.g. (1..10).reject { |i| i % 3 == 0 } # => [1, 2, 4, 5, 7, 8, 10]
#
# .upto(limit) => iterates block up to the int number
# e.g. 5.upto(10) { |i| print i, " " } # => 5 6 7 8 9 10


# puts %w[ant bear cat].all? { |word| word.length >= 3 } # => true
