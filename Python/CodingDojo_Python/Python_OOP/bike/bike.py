class bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print [self.price, self.max_speed, self.miles]

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self


# print dir(bike)

mongoose = bike(400, 55, 75)
# print mongoose
# print mongoose.ride()
# print mongoose.ride()
# print mongoose.ride()
# print mongoose.reverse()
# print mongoose.ride()

mongoose.ride().ride()
































#
