

def typeOfList(thisList):
    sum = 0
    strg = ""
    for i in thisList:
        # print type(i)
        if isinstance(i,(int,float)) == True:
            sum = sum + i
            print sum
        if type(i) == str:
            strg += i
            print strg
#need to print the string

typeOfList(['magical unicorns',19,'hello',98.98,'world'])
