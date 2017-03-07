import random

flips = 0
heads = 0
tails = 0

while flips<5000:
    coin = random.randint(1,2)
    if coin == 1:
        heads += 1
        flips +=1
        print "Attempt #", flips, " : Throwing a coin... It's a head! ... Got ", heads, "heads so far and ", tails, "tails so far ..."
    elif coin == 2:
        tails += 1
        flips +=1
        print "Attempt #", flips, " : Throwing a coin... It's a tails! ... Got ", heads, "heads so far and ", tails, "tails so far ..."
        # tails += 1
        # flips +=1

# print("You got " + str(heads) +  " heads and " + str(tails) + " tails!")

# ********** above is from stackoverflow.com****
