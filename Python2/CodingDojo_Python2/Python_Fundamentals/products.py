# products

class Product(object):
    def __init__(self, price, item_weight, brand, cost, status="For Sale"):
        self.price = price
        self.item_weight = item_weight
        self.brand = brand
        self.cost = cost
        self.status = "For Sale"

    def sell(self):
        self.status = "sold"
        return self

    def addtax(self, tax):
        self.tax = tax
        # self.price = price
        self.price = self.price + (self.price * float(tax))
        return self

    def returns(self,reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "returned in a box":
            self.status = "for sale"
        else:
            reason == "opened"
            self.status = "used"
            self.cost = self.price - (self.price * .20)

    def display_all(self):
        print "Price: " + str(self.price)
        print "Item weight: " + str(self.item_weight)
        print "Brand: " + str(self.brand)
        print "Cost: " + str(self.cost)
        print "Status: " + str(self.status)


Atom = Product(200, 10, "mac",100,"status")

# Atom.display_all()
# Atom.addtax(.06)
Atom.returns("defective")
Atom.display_all()
Atom.returns("opened")
Atom.display_all()
