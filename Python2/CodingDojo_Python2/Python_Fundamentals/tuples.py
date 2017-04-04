# tuples are immutable

# '''A Tuple is a container for a fixed sequence of data objects. The name comes from the Latin suffix for multiples: double, triple, quadruple, quintuple. Tuples are sequences, just like lists. The only difference is that tuples can't be changed -- that is, tuples are immutable. Also, while lists are defined using square brackets, tuples use parentheses. Creating a tuple is as simple as declaring different comma-separated values. Optionally you can put these values between parentheses.'''

tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5 )
tuple_letters = "a", "b", "c", "d"

dog = ("Canis Familiaris", "dog", "carnivore", 12)
print dog[2]
#result is: carnivore

value = ("Michael", "Instructor", "Coding Dojo")
(name, position, company) = value #tuple unpacking
print name
print position
print company

'''Built-in Tuple Functions '''
''' len() '''
tuple_data = ('physics', 'chemistry', 1997, 2000)
print len(tuple_data)
#result: 4

''' max() '''
tuple_data = ('physics', 'chemistry', 'x-ray', 'python')
tuple_num = (67, 89, 31, 15)
print max(tuple_data)
print max(tuple_num)
#result is..
#x-ray
#89

''' min() '''
tuple_data = ('physics', 'chemistry', 'x-ray', 'python')
tuple_num = (67, 89, 31, 15)
print min(tuple_data)
print min(tuple_num)
#result is...
#chemistry
#15

''' sum() '''
tuple_num = (67, 89, 31, 15)
print sum(tuple_num)
#result: 202

''' any() '''
# return True if there exists any item in the tuple which is True.
#
# If a tuple contained (0, False, '', 0.0, []), all of which have boolean values of False, then any(tuple) would be False. If a tuple contained [-1, -2, 10, -4, 20], all of which evaluate to True, then any(tuple) would be True.
tuple_num = (67, 89, 31, False, 0, None)
print any(tuple_num)
#result: True

''' all() '''
# return True if all items are True.
tuple_num = (67, 89, 31, False, 0, None)
print all(tuple_num)
#result: False

''' enumerate() '''

num = (1, 5, 7, 3, 8)
for index, item in enumerate(num):
    print(str(index)+" = "+str(item))
#result is...
#0 = 1
#1 = 5
#2 = 7
#3 = 3
#4 = 8

''' sorted() '''
# iterate through the tuple in sorted order. Note: the returned collection is a sorted list, not a tuple.
num = (1, 5, 7, 3, 8)
print sorted(num)
#result: [1,3,5,7,8]

''' reversed() '''
# iterate through the tuple in reverse order. Note that the return value from reversed() is generic <reversed object> and must be fed into the tuple() or list() constructor to create one of those objects.
num = (9, 1, 8, 2, 7, 3)
print tuple(reversed(num))
#result: (3, 7, 2, 8, 1, 9)

''' Tuple as return Values '''
# For example, we could write a function that returns both the circumference and the area of a circle of radius r:
def get_circle_area(r):
    #Return (circumference, area) of a circle of radius r
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)
