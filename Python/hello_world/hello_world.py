# x = "Hello Python"
# print x
# y = 42
# print y
#
# # this is how to do a comment line
# print "read below for more on multi-line comments in python!"
# # this line below would should not execute.
# '''
# Triple quotations allow us to commnet across mulitple lines as long as You can use doulbe or single quotes!
# '''# notice this inside the triple quotes did not print in the command line when you typed ..python hello_world.py
#
# # define a function that says hello to the name provided
# # this starts a new block
# def say_hello(name):
#   #these lines are indented therefore part of the function
#   if name:
#    print 'Hello, ' + name + 'from inside the function'
#   else:
#    print 'No name'
# # now we're unindented and have ended the previous block
# print 'Outside of the function'
#
# say_hello(jim):

# name = "Zen"
# print "My name is ", name
#
# print "My name is " + name
#
# print "number with comma", 55
#
# print "number with plus symbol" + 55 # cannot use this.  cannot concate str and int with ...+

# first_name = "jimmy"
# last_name = "park"
# print "My name is {}{}".format(first_name,last_name)

# string interpolation????

# hw = "hello %s" % 'world'
# print hw
# # the output would be:
# # hello world

# my_string = 'hello world'
# print my_string.capitalize()
# # the output would be:
# # Hello world

# fruits =['apple','banana','orange','strawberry']
# vegatables = ['lettuce','cucumber','carrots']
#
# fruits_and_vegatables = fruits + vegatables
# print fruits_and_vegatables
# salad = 3 * vegatables
# print salad

# drawer = ['documents', 'envelopes', 'pens']
# #access the drawer with index of 0 and print value
# print drawer[0]  #prints documents
# #access the drawer with index of 1 and print value
# print drawer[1] #prints envelopes
# #access the drawer with index of 2 and print value
# print drawer[2] #prints pens

# x = [1,2,3,4,5]
# x.append(99)
# print x
# #the output would be [1,2,3,4,5,99]

# names = ['jimmy','bob','tom','lisa','ann']
# print names.join

def add(a,b):
  x = a + b
  return x
  print x
# the return value gets assigned to the "result" variable
result = add(3,5)
print result # this should print 8










#
