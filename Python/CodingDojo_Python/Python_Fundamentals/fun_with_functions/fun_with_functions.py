# Assignment: Fun with Functions
# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.


# def odd_even (a,b):
#     for i in range(a,b):
#         if i % 2 != 0:
#             print "this number", i, "an odd number"
#         else:
#             print "this number", i, "an even number"
# print odd_even (1,2000)

# Multiply:
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
# The function should multiply each value in the list by the second argument. For example, let's say:

# a = [2,4,10,16]

# def mulitply (a,b):
#     park = [i * b for i in a]
#     print park
# mulitply([2,4,10,16],5)

# def mulitply (a,b): #this is not printing out an array format
#     a = []
#     for i in a:
#         print i * b
# mulitply([2,4,10,16],5)

# debugging***********************
def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
# output:
# >>>[2,4,10,16]




















#
