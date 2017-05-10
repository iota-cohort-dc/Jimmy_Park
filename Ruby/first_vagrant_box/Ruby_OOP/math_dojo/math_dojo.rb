#
# class MathDojo
#   attr_reader :answer
#
#   def initialize
#     @answer = 0
#   end
#
#   def add(*numbers)
#     @answer += numbers.flatten.reduce(0, :+) # flatten takes multidimesional arrays into a single dimension array  # reduce
#     self
#   end
#
#   def subtract(*numbers)
#     @answer -= numbers.flatten.reduce(0, :+)
#     self
#   end
# end
#
# challenge1 = MathDojo.new.add(2).add(2, 5).subtract(3, 2).answer
# challenge2 = MathDojo.new.add(1).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract([2,3], [1.1, 2.3]).answer
# puts challenge1
# puts challenge2


# xx = [1,2,3,[4,5,6,7],8,9,10,11,[12,13,[14,15,[16,17,18],19,20],21],22,23,24]
# p xx.flatten
#
# class MathDojo
#   attr_reader :answer
#   def initialize
#     @answer = 0
#   end
#   def addNumber(*numbers)
#     @answer += numbers.flatten.reduce(0,:+)
#     self
#   end
#   def subNumber(*numbers)
#     @answer -= numbers.flatten.reduce(0,:+)
#     self
#   end
# end
# puts "*"*60
# newMathProblem = MathDojo.new.addNumber(10).addNumber(10).subNumber(10).answer
# puts newMathProblem

class MathDojo
  attr_reader :answer

  def initialize
    @answer = 0
  end

  def addNum(*numbers)
    @answer += numbers.flatten.reduce(0,:+)
    self
  end

  def subNum(*numbers)
    @answer -= numbers.flatten.reduce(0,:+)
    self
  end
end

testMath = MathDojo.new.addNum(10).addNum(20).answer
puts testMath
