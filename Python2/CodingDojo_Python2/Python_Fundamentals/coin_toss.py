import random

def coinToss():
    heads = 0
    tails = 0
    count = 0
    while count < 5000:
        randToss = round(random.random())
        # print randToss
        if randToss == 1:
            heads = heads + 1
            count = count + 1
            print "Attempt #",count,": Throwing a coin.. It's a head! .. Got ",heads,"head(s) so far and ",tails,"tail(s) so far"
        if randToss == 0:
            tails = tails + 1
            count = count + 1
            print "Attempt #",count,": Throwing a coin.. It's a tail! .. Got ",tails,"tail(s) so far and ",tails,"tail(s) so far"

coinToss()
