# Store

class Store(object):
    def __init__(self, products, location, owner):
        # print "New STORE!"
        self.products = products
        self.location = location
        self.owner = owner

    def add_product(self):
        print "adding new products"
        self.products += 1
        return self

    def remove_product(self):
        print "removing products"
        self.products -= 1
        return self

    def inventory(self):
        print [self.books]

JimStore = Store(1312, "tysons_corner", "jim")

JimStore.add_product().add_product().remove_product()
