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

# animal = Animal('tiger', 100)
# animal.walk().walk().walk().run().displayHealth()

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150

    def pet(self):
        self.health = self.health + 5
        return self

# dog = Dog('elvis')
# dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170

    def fly(self):
        self.health = self.health - 10
        return self.health


    def displayHealth(self):
        print 'This is a dragon'
        print self.health
        return self

dragon = Dragon('Pete', 100)
# dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
# dragon.displayHealth()
print dragon.fly()




# class Wizard(Human):
#     def __init__(self):
#         super(Wizard, self).__init__(name)   # use super to call the Human __init__ method
#         self.intelligence = 10           # every wizard starts off with 10 intelligence
#     def heal(self):
#         self.health += 10
# class Ninja(Human):
#     def __init__(self):
#         super(Ninja, self).__init__()    # use super to call the Human __init__ method
#         self.stealth = 10                # every Ninja starts off with 10 stealth
#     def steal(self):
#         self.stealth += 5
# class Samurai(Human):
#     def __init__(self):
#         super(Samurai, self).__init__()  # use super to call the Human __init__ method
#         self.strength = 10               # every Samurai starts off with 10 strength
#     def sacrifice(self):
#         self.health -= 5
