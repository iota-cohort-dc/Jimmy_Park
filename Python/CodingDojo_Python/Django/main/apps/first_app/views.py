from django.shortcuts import render, HttpResponse

def index(request):
    print ("*" * 100)
    return render(request, "first_app/index.html")








# Create your views here.
# def index(request):
#     response = "Hello, I am your first request!"
#     return HttpResponse(response)

# THIS IS OUR CONTROLLER !!!!! !!!! !!!! !!!!
