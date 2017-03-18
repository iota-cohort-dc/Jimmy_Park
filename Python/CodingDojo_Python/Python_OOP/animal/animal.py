# Create a class called Animal with the following attributes: name, and health
# Give a new animal a health of 100 when it gets created.
# Give the animal the following three methods: walk, run, and displayHealth.
# When a walk() method is invoked, have the health decrease by 1
# When a run() method is invoked, have the health decrease by 5
# When a displayHealth() method is invoked, display on screen the name of the Animal and the health.
# Create an instance of the animal called 'animal' and have this animal walk three times, run twice, and have it display its health.

class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = 100

    def walk(self):
        self.health = self.health - 1
        return self

    def run(self):
        self.health = self.health - 5
        return self

    def displayHealth(self):
        print self.health

animal = Animal('tiger', 100)
animal.walk().walk().walk().run().displayHealth()

# Now, create another class called Dog that inherits everything that the Animal does and has, but
# 1) have the default health be 150 and
# 2) add a new method called pet, which when invoked, increase the health by 5.
# 3) Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().

class Dog(Animal):
    def __init__(self, name):
        super(Animal, self).__init__()
        self.health = 150

    def pet(self):
        self.health = self.health + 5
        return self

dog = Dog('elvis')
dog.walk().walk().walk().run().run().pet().displayHealth()

# Now, create another class called Dragon that also inherits everything from Animal, but
# 1) have the default health be 170 and
# 2) add a new method called fly, which when invoked, decreased the health by 10.
# 3) Have the Dragon walk() three times, run() twice, fly() twice, and have it displayHealth().
# 4) When the Dragon's displayHealth function is called, have it say 'this is a dragon!' before it displays the default information (by calling the parent's displayHealth function).

class Dragon(Animal):
    def __init__(self, name):
        super(Animal, self).__init__()
        self.health = 170

    def fly(self):
        self.health = self.health - 10
        return self

    def displayHealth(self):
        print 'This is a dragon'
        print self.health
        return self

dragon = Dragon('Pete')
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()




































#
