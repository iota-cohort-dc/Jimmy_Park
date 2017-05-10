
class Project
  attr_accessor :name, :description
  def initialize
    @name = name
    @description = description
  end
  def elevator_pitch
    "#{@name}, #{@description}"
  end
end

# class Project
#   def name=(name)
#     @name = name
#   end
#   def name
#     @name
#   end
# end

# ----------------------------------------------------------------

# class Project
#   attr_accessor :name, :description,:owner   # added owner,task
#   def initialize name, description, owner   # added owner, task
#     @name = name
#     @description = description
#     @owner = owner # added owner
#     @task = [] # added task
#   end
#   def elevator_pitch
#     "#{@name}, #{@description}" # added owner,task
#   end
# end
