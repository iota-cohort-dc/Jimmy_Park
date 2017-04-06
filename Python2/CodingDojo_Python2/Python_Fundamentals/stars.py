#<-------------- ------------------>

# def draw_stars(a):
#     for i in a:
#         print "*" * i
#
# stars = [10,50,2,15,20,5,15,50]
# # print len(stars)
# draw_stars(stars)

#<-------------- ------------------>

# def draw_stars(a):
#     # while a < len(a): ## this line does not belong here##
#     for i in a:
#         # print "****************"
#         if type(i) == int:
#             stars = "*" * i
#             print stars
#         else:
#             # print "*****************"
#             i = i.lower()
#             stars = i[0]*len(i)
#             #        t  * len of tom
#             print stars
#
#         [0]
# x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
# draw_stars(x)

#<-------------- ------------------>

# def draw_stars(a):
#     # while i < len(a): ## this line does not belong here ##
#         for i in a:
#             if type(i) == int:
#                 stars = "*" * i
#                 print stars
#             else:
#                 i = i.lower()
#                 stars = i[0]*len(i)
#                 print stars
#
# x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
# draw_stars(x)

#<-------------- ------------------>

def draw_stars(a):
    for i in a:
        if type(i)==int:
            stars = "*" * i
            print stars
        else:
            i = i.lower()
            stars = i[0]*len(i)
            print stars

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)
