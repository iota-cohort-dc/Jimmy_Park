# <---------- dictionaries ------------->
jimmy = {"name": "Jimmy", "age": "41", "country": "Korea", "favLang": "Python"}
danial = {"name": "Danial", "age": "29", "country": "USA", "favLang": "Python"}
kaemon = {"name": "kaemon", "age": "15", "country": "USA", "favLang": "English"}
def person(poo): #args?
    print "My name is ", poo["name"]
    print "My age is ", poo["age"]
    print "Country of birth is the ", poo["country"]
    print "My favorite language is ", poo["favLang"]

person(kaemon)
person(jimmy)

# <---------- print out keys ------------->
for data in personal:
    print data
# outputs:
# favLang
# country
# age
# name

# <---------- print out keys ------------->
for key in personal.iterkeys():
    print key
# outputs:
# favLang
# country
# age
# name

# <---------- print out values ------------->
for val in personal.itervalues():
    print val
# outputs:
# Python
# Korea
# 41
# Jimmy

# <---------- print out keys AND values ------------->
for key,data in personal.iteritems():
    print key, "=", data
# outputs:
# favLang = Python
# country = Korea
# age = 41
# name = Jimmy
