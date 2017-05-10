
class Human
  attr_accessor :strength, :intelligence, :health, :stealth #getter and setter
  def initialize  # these are the default values when new Human is created *
    @health = 100  # these are the default values when new Human is created *
    @strength = 3  # these are the default values when new Human is created *
    @intelligence = 3  # these are the default values when new Human is created *
    @stealth = 3  # these are the default values when new Human is created *
  end
  def attack(obj)
    # check ~ if ~ the attacked object's class is Human or inherits from the Human class
    if obj.class.ancestors.include?(Human)
      obj.health -= 10
      # remember that we don't need to write "return" in ruby
      # stating true below will automatically return the boolean true
      true
    else
      false
    end
  end
end

class Wizard < Human
  def initialize
    super
    @health = 50
    @initialize = 25
  end
  def heal
    @health += 10
  end
  def fireball(obj)
    if obj.class.ancestors.include?(Human)
      obj.health -= 20
      true
    else
      false
    end
  end
end

class Ninja
  def initialize
    super
    @health = 175
  end
  def steal(victim) ##
    attack(victim) ##
    @health += 10
    self
  end
  def get_away
    @health -= 15
    self
  end
end

class Samurai
  @@count = 0
  def initialize
    @health = 200
    @@count += 0
  end
  def death_blow(obj) #
    if obj.class.ancestors.include?(Human)
      obj.health = 0
      true
    else
      false
    end
  end
  def meditate
    @health = 200
  end
  def how_many
    @@count
  end
end
