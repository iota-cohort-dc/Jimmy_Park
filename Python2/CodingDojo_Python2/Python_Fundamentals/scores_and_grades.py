import random

# <------------------ random.randint(start,end) ---------->
def randomScore():
    # print "before"
    num =  random.randint(60,100)
    # print "after"
    if num > 59 and num < 70:
        print "Score: " , num , "; " , "Your grade is D"
    if num > 69 and num < 80:
        print "Score: " , num , "; " , "Your grade is C"
    if num > 79 and num < 90:
        print "Score: " , num , "; " , "Your grade is B"
    if num > 89 and num < 101:
        print "Score: " , num , "; " , "Your grade is A"
randomScore()

# <------------------ random.random() ------------------->
# def randomScore():
#     # print "before"
#     num =  int(random.random() * 100)
#     # int() converts random.random() from a decimal to whole interger
#     # print "after"
#     # print num
#     if num > 59 and num < 70:
#         print "Score: " , num , "; " , "Your grade is D"
#     if num > 69 and num < 80:
#         print "Score: " , num , "; " , "Your grade is C"
#     if num > 79 and num < 90:
#         print "Score: " , num , "; " , "Your grade is B"
#     if num > 89 and num < 101:
#         print "Score: " , num , "; " , "Your grade is A"
#     if num < 59:
#         print "Score: " , num , "; " , "Your grade is FFFFFFF"
# randomScore()

# <------------- random.randrange(start,end) ------------->
# def randomScore():
#     # print "before"
#     num =  random.randrange(60,100)
#     # print "after"
#     # print num
#     if num > 59 and num < 70:
#         print "Score: " , num , "; " , "Your grade is D"
#     if num > 69 and num < 80:
#         print "Score: " , num , "; " , "Your grade is C"
#     if num > 79 and num < 90:
#         print "Score: " , num , "; " , "Your grade is B"
#     if num > 89 and num < 101:
#         print "Score: " , num , "; " , "Your grade is A"
# randomScore()
