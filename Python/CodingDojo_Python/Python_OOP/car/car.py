# python

class Car(object):
    def __init__(self, price, speed, fuel, milage):
        print "New CAR"
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milage = milage


        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12

    def display_all(self)
        print [self.price, self.speed, self.fuel, self.milage]

ford = Car(9000, 200, 10, 50)
benz = Car (40000, 200, 15, 50)
toyota = Car(15000, 200, 15, 50)
nissan = Car(5000, 200, 15, 50)
audi = Car(40000, 200, 15, 50)

print display_all(ford)

# print ford.speed
# print ford.price
# print nissan.price
# print benz.milage
#
# print benz.tax
# print nissan.tax
# print toyota.tax

# display_all(ford)
