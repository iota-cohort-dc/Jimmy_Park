

def typeOfList(thisList):
    sum = 0
    strg = " "
    for i in thisList:
        # print type(i)
        if isinstance(i,(int,float)) == True:
            sum = sum + i
        if type(i) == str:
            strg += i
    print sum
    print strg

typeOfList(['magical unicorns',19,'hello',98.98,'world'])
