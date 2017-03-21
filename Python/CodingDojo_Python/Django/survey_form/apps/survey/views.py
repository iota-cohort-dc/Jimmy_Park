from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "index.html")

    if 'count' in session:
        pass
    else:
        session['count'] = 0
    return render("index.html")

def process(request):

    name = request.POST["name"]
    loc = request.POST["location"]
    fav = request.POST["favLang"]
    comment = request.POST["comment"]

    request.session["name"] = name
    request.session["location"] = loc
    request.session["favLang"] = fav
    request.session["comment"] = comment

    if 'count' in request.session:
        request.session['count'] += 1
    return render(request, "results.html")

def results(request):
    print request.session['data']
    return render(request, 'results.html') # dont need / infront of results.



    # request.session['data'] = {
    #     'name': request.POST['name'],
    #     'location': request.POST['location'],
    #     'favLang': request.POST['favorite_language'],
    #     'comment': request.POST['comment']
    # }

    # name1 = request.POST['name']
    # location1 = request.POST['location']
    # fav_lang1 = request.POST['favorite_language']
    # content1 = request.POST['content']
    #
    # context = {
    #     'nameitwhatever' :name1,
    #     'locationitwhatever' :location1,
    #     'favoritelanguageitwhatever' :fav_lang1,
    #     'contentitwhatever' :content1
    # }
    # return redirect( "/results", context)
