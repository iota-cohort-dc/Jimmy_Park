# Find and Replace
#
# In this string: str = "If monkeys like bananas, then I must be a monkey!" print the position of the first instance of the word "monkey". Then create a new string where the word "monkey" is replaced with the word "alligator".

str = "If monkeys like bananas, then I must be a monkey!"
print str.find("monkeys")
print str.replace("monkey","alligator")

# Min and Max
#
# Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.

x = [2,54,-2,7,12,98]
print max(x)
print min(x)

# First and Last
#
# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.

x = ["hello",2,54,-2,7,12,98,"world"]
print x.pop(0)
print x.pop()

# New List
#
# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!

x = [19,2,54,-2,7,12,98,32,10,-3,6]

new_sort = x.sort()
print x # or print new_sort

first = x[:5]
print first

last = x[5:]
print last


last.insert(0,first)
print last



# x.insert(0,new_sort_half)
# print x





















#
