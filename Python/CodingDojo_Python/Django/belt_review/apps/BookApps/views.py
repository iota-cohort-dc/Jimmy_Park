from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Books, Authors, Reviews, User

def index(request):
    # use these prints to see if objects are created.
    # print Books.objects.all()
    # print Authors.objects.all()
    # print Reviews.objects.all()
    # if nothing gets created in the query it comes back like: <QuerySet []>
    # if something does get created it will look like this:
    # <QuerySet [<Books: Books object>, <Books: Books object>, <Books: Books object>]>
    # <QuerySet [<Authors: Authors object>]>
    # <QuerySet [<Reviews: Reviews object>]>


    return render(request, ("BookApps/index.html"))

def addbook(request):
    return render(request, ("BookApps/addbook.html"))

def create(request):

    # #getting this from login registration setting this to variable and equaling to user in  Reviews.objects...
    # user = request.session['user_id']
    #
    # if request.method == "POST":# use this if you get MultValueDickError at /addbook
    #
    #     book = Books.objects.create(title = request.POST['title']) #1 creates object to books database
    # #2create variable book to input into other tables
    #
    #     Authors.objects.create(name = request.POST['or_new_author'], books = book)
    # # 3books is set to book to be able to access 'book'

    #     Reviews.objects.create(comments = request.POST['text'], ratings = request.POST['rating'], book = book, user = user)
    # # rating...s relates to models.py class#
    # # rating relates to the name="rating" in the html

    if request.method == "POST":

        book_title = request.POST['title']
        author_name = request.POST['or_new_author']

        # if author_name == '':
        #     author_name = request.POST['select_authors']

        Books.objects.create(title = book_title)


        if not Authors.objects.filter(name = author_name).exists():
            Authors.objects.create(name = author_name)

        this_book = Books.objects.get(title=book_title)
        this_author = Authors.objects.get(name=author_name)
        this_author.books.add(this_book)

        user_id = request.session['user_id']

        Reviews.objects.create(
            comments = request.POST['text'],
            ratings = int(request.POST['rating']),
            user = User.objects.get(id=user_id),
            book = this_book
        )

        return redirect(reverse("books:index"))

def reviews(request):

    return render(request, ("BookApps/reviews.html"))

def userpage(request):

    return render(request,("BookApps/user.html"))

# def create(request):
#     # use the ORM..............
#     Courses.objects.create(name=request.POST['name'],description=request.POST['description'])
#     # above is saying insert the Courses, (name, description.. created_at,updated_at ) values of (name, description, now(), now())
#     return redirect('/')
#
# def remove(request, id): # have to put id, next request bc you are going to use it below
#
#     context = {
#     'remv' : Courses.objects.get(id=id) # any variable name is ok.. this case was 'remv'.. remove was used in the a-href in the index.html and also in the form action="/..... /{{ remv.id }}"
#     }
#
#     return render(request, "CoursesApp/delete.html", context)
#
#
# def destroy(request, id):
#
#     Courses.objects.get(id=id).delete()
#
#     return redirect("/")
