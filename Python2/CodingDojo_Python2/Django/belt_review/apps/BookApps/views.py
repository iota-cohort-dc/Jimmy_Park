from django.shortcuts import render, redirect
from .models import User, Books, Authors, Reviews
from django.db.models import Count
from django.core.urlresolvers import reverse

def index(request):
	three = Reviews.objects.all().order_by('-created_at')[:3]

	context = {
	'user': User.objects.get(id=request.session['user']),
	'reviews': Reviews.objects.all().order_by('-created_at')[:3],
	'otherRevs': Reviews.objects.exclude(pk__in=three)
	}
	return render(request, 'beltRev/index.html', context)

def add(request):
	data = {
	'authors': Authors.objects.all()
	}
	return render(request, 'beltRev/addBook.html', data)

def review(request):
    if request.method == "POST":

        book_title = request.POST['title']
        author_name = request.POST['addauthor']
        if author_name == '':
            author_name = request.POST['authorselect']
        Books.objects.create(title = book_title)

        if not Authors.objects.filter(name=author_name).exists():
            Authors.objects.create(name = author_name)

        this_book = Books.objects.get(title=book_title)
        this_author = Authors.objects.get(name=author_name)
        this_author.books.add(this_book)
        user_id = request.session['user']
        Reviews.objects.create(
            content = request.POST['review'],
            rating = int(request.POST['rating']),
            user = User.objects.get(id=user_id),
            book = this_book
        )
	return redirect(reverse('books:index'))

def displayRev(request, id):
	if request.method == "POST":
		user_id = request.session['user']
		reviews = Reviews.objects.create(
		content = request.POST['rev'],
		rating = int(request.POST['rating']),
		user = User.objects.get(id=user_id),
		book = Books.objects.get(id=id)
        )

	data = {
	'reviews': Reviews.objects.filter(book=id),
	'book': Books.objects.get(id=id),
	'author': Authors.objects.get(books=id)
	}
	return render(request, 'beltRev/bookRev.html', data)

def userPage(request, id):
	data = {
	'user': User.objects.filter(id=id).annotate(num_reviews=Count('posted_reviews')),
	'revUser': Reviews.objects.filter(user = id)
	}
	return render(request, 'beltRev/userInfo.html', data)
