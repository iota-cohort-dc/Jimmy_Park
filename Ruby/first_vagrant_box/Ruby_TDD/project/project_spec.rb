require_relative 'project'
RSpec.describe Project do
  it "has a getter and setter for name attribute" do
    project = Project.new # creates new instance from the other file Project
    project.name = "Project Name" # giving it a 'name' to the 'name' attribute
    expect(project.name).to eq("Project Name") # when we run this line code ......
  # we EXPECT the project name TO EQual "Project Name"
  end
end

# -----------------------------most recent-----------------------------------
# require_relative 'project'
# RSpec.describe Project do
#   before(:each) do
#     # updated this block to create two projects
#     @project1 = Project.new('Project 1', 'description 1','owner 1') # added owner 1
#     @project2 = Project.new('Project 2', 'description 2', 'owner 2') # added owner 2
#   end
#   # ...  the three dots gave an error, had to comment this out
#     # Code from the previous tab removed for brevity. Leave it in.
#   # ...  the three dots gave an error, had to comment this out
#   it 'has a method elevator_pitch to explain name and description' do
#     expect(@project1.elevator_pitch).to eq("Project 1, description 1") # added owner 1
#     expect(@project2.elevator_pitch).to eq("Project 2, description 2") # added owner 2
#   end
# end
# ----------------------------------------------------------------
# require_relative 'project' # include our Project class in our spec file
# RSpec.describe Project do
#   before(:each) do
#     @project1 = Project.new('Project 1', 'description 1') # create a new project and make sure we can set the name attribute
#   end
#   it 'has a getter and setter for name attribute' do
#     @project1.name = "Changed Name" # this line would fail if our class did not have a setter method
#     expect(@project1.name).to eq("Changed Name") # this line would fail if we did not have a getter or if it did not change the name successfully in the previous line.
#   end
# end
# ----------------------------------------------------------------
