#1 Create an array with the following values: 3,5,1,2,7,9,8,13,25,32. Print the sum of all numbers in the array. Also have the function return an array that only include numbers that are greater than 10 (e.g. when you pass the array above, it should return an array with the values of 13,25,32 - hint: use reject or find_all method)

# array = [3,5,1,2,7,9,8,13,25,32]
# sum = 0
# array.each { |i| puts "#{sum += i}" } # prints out everytime addition
# # (((or)))
# puts array.reduce(:+) # prints out at the end
# puts array.reject { |i| i < 10 } # prints out the opposite of all

# ----------------------------------------------------------------------------------------------------------

#2 Create an array with the following values: John, KB, Oliver, Cory, Matthew, Christopher. Shuffle the array and print the name of each person. Have the program also return an array with names that are longer than 5 characters.

# anotherArray = ["John", "KB", "Oliver", "Cory", "Mathew", "Christopher"]
# anotherArray.shuffle.each { |i| puts i}
# puts anotherArray.select { |i| i.length > 5  }

# ----------------------------------------------------------------------------------------------------------

#2 Create an array that contains all 26 letters in the alphabet (this array must have 26 values). Shuffle the array and display the last letter of the array. Have it also display the first letter of the array. If the first letter in the array is a vowel, have it display a message.

# newArr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","w","v","x","y","z"]
# puts newArr
# puts newArr.shuffle.select { |i| i }
# (((or)))
# letters_array = ("a".."z").to_a
# puts letters_array
# puts letters_array.shuffle
# puts letters_array.shuffle.last  # prints last letter in the Shuffle
# puts letters_array.shuffle.first  # prints last letter in the Shuffle
# shuffled = letters_array.shuffle
# puts "#{shuffled.first} is a vowel" if ["a","e","i","o","u"].include? shuffled.first
# this says print the first letter  if          aeiou       is includeed in begining is of shuffled

# ----------------------------------------------------------------------------------------------------------

#3 Generate an array with 10 random numbers between 55-100.
# def genArr
#   arr = []
#   for i in 0..9
#     arr.push(rand(55..100))
#   end
#   puts arr
# end
# genArr

# (((or)))

# ranArray = []
# 10.times { ranArray << rand(55..100) }
# print ranArray

# ----------------------------------------------------------------------------------------------------------

#4 Generate an array with 10 random numbers between 55-100 and have it be sorted (showing the smallest number in the beginning). Display all the numbers in the array. Next, display the minimum value in the array as well as the maximum value

# ranArray = []
# 10.times { ranArray << rand(55..100) }
# puts ranArray
# puts ranArray.sort # sorts the array lowest to highest

# ----------------------------------------------------------------------------------------------------------

#5 Create a random string that is 5 characters long (hint: (65+rand(26)).chr returns a random character)
# puts (0..4).map { (65 + rand(26)).chr }.join

# ----------------------------------------------------------------------------------------------------------

#6 Generate an array with 10 random strings that are each 5 characters long
# rand_string_array = []
# 10.times do
#   str = ""
#   5.times { str << rand(65..90).chr }
#   rand_string_array << str
# end
# puts rand_string_array
