
class Bike(object):
    def __init__(self,price,max_speed,miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
        # return self
    def ride(self):
        print "Riding my bike"
        self.miles += 1343
        print self.miles
        return self

    def reverse(self):
        print "What out, I'm reversing"
        self.miles -= 1
        print self.miles
        return self

    def displayInfo(self):
        print [self.price, self.max_speed, self.miles]
        return self

    def longRun(self):
        print "Going the Distance"
        self.miles += 18027340981
        print self.miles
        return self

mongoose = Bike(300, 200)

print mongoose.ride()
# print mongoose.reverse()
# print mongoose.displayInfo()
# print mongoose.longRun()
