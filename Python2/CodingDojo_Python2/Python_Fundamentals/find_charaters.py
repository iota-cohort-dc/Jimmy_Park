# Find Characters

l = ['hello','world','my','name','is','Anna']
char = 'o'
newList = []
# words = l.split()

def findCharacters (a,b):
    for i in a:
        for m in i:
            if m == b:
                print i
findCharacters(l,char)
