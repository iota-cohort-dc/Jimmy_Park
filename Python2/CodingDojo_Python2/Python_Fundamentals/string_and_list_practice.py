# Find and Replace
# In this string: str = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".

str = "It's thanksgiving day. It's my birthday,too!"
print str
print str.find("day")# find the word "day"
str = str.replace("day", "month")# 1st argumnt find word,2nd argumnt replace with..
print str

# Min and Max
# Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.

x = [2,54,-2,7,12,98]
print x
print min(x)
print max(x)
print min/len(x) #avg

# First and Last
# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x) - 1]

# New List
# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!

x = [19,2,54,-2,7,12,98,32,10,-3,6]
# print x
x.sort() #sorts lowest to highest
# print x
first_list = x[0:len(x)/2] #from the begining to the mid point
second_list = x[len(x)/2:len(x)] #from the mid point the the end.. len(x)is same as arr.length
print "first_list", first_list
print "second_list", second_list

second_list.insert(0,first_list) #at 0 index insert first_list

print second_list #print everything
