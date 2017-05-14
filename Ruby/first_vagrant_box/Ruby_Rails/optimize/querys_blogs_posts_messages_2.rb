#  Queries for blogs_posts_messages_2 Assignment


2.3.1 :038 > Owner.create(user:User.first, blog:Blog.first)
#                        (user: dont use actual id integer)

#                        variablename = User.find(5)

User.where("users.id= 4")

User.where("users.id = ?", User.fourth)























#
