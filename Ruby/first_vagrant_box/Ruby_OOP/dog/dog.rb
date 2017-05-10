# (dog.rb) create a class called Dog that inherits from the Mammal class and do the following:
# Default health of 150 (inherited)
# A method called pet, which when invoked, increases the health by 5
# A method called walk, which when invoked, decreases the health by 1
# A method called run, which when invoked, decreases the health by 10
# A method called display_health (inherited)
# Have an instance of the Dog class walk 3 times, run twice, pet once and then display its health

require_relative 'mammal'

class Dog < Mammal  #  < Mammal  this make Dog class inherit Mammal
  def pet
    @health += 5  # this comes from mammal.rb
    self
  end
  def walk
    @health -= 1
    self
  end
  def run
    @health -= 10
    self
  end
end

class Lion < Mammal
  def initialize
    @health = 170
    self
  end
  def fly
    @health -= 10
    self
  end
  def attack_town
    @health -= 50
    self
  end
  def eat_humans
    @health += 20
    self
  end
  def display_health # this from mammals.rb-display_health,this inherits its attributes
                     # it should puts @health from mammals.rb
    super
    puts "this is lion roar"
  end
end

simba = Lion.new
simba.attack_town.attack_town.attack_town.eat_humans.eat_humans.fly.fly.display_health

# shaggy = Dog.new
# shaggy.display_health
# shaggy.walk.walk.walk.display_health
# shaggy.walk.walk.walk.run.run.pet.display_health
