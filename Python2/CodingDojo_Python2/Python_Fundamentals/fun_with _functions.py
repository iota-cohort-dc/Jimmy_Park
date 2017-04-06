# def oddEven(a,b):  #<--- this function does NOT work.--->
#     while (a < b):
#         if a % b == 1:
#             print "Number is " + a + " This is an odd number."
#         else:
#             print "Number is " + a + " This is an even number."
# print oddEven(1,2000)   #<--- this function does NOT work.--->

# <--------------- Odd/Even --------------->
def odd_even(a,b):
    for i in range(a,b):
        if i % 2 != 0:
            print "this number", i, "an odd number"
        else:
            print "this number", i, "an even number"
print odd_even (1,2001)

# <--------------- Multiply --------------->
def mulitply(a,b):
    for i in a:
        print i * b

c = [2,4,10,16]
d = [5,10,20,100,500]
print mulitply(d, 5)
#
