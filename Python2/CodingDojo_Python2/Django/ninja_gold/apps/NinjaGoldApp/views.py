from django.shortcuts import render, redirect
from random import randint, randrange
import datetime

# Create your views here.
def index(request):

    if 'activity' not in request.session:
        request.session['activity'] = []
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0

    return render(request,"ninja_gold/index.html")

def process(request):

    if request.POST['building'] == 'farm':
        gold = randrange(10,20)
        print gold
        request.session['total_gold'] += gold
        activityVariable = "You've got " + str(gold) + " gold coins from the Farm." + " " + str(datetime.datetime.now().strftime('(%Y/%m/%d %H:%M)'))
        request.session['activity'].insert(0,activityVariable)

    if request.POST['building'] == 'cave':
        gold = randrange(5,10)
        print gold
        request.session['total_gold'] += gold
        activityVariable = "You've got " + str(gold) + " gold coins from the Cave." + " " + str(datetime.datetime.now().strftime('(%Y/%m/%d %H:%M)'))
        request.session['activity'].insert(0,activityVariable)

    if request.POST['building'] == 'house':
        gold = randrange(2,5)
        print gold
        print "here"
        request.session['total_gold'] += gold
        activityVariable = "You've got " + str(gold) + " gold coins from the House." + " " + str(datetime.datetime.now().strftime('(%Y/%m/%d %H:%M)'))
        request.session['activity'].insert(0,activityVariable)

    if request.POST['building'] == 'casino':
        gold = randrange(-50,50)
        print gold
        request.session['total_gold'] += gold
        activityVariable = "You've got " + str(gold) + " gold coins from the Casino." + " " + str(datetime.datetime.now().strftime('(%Y/%m/%d %H:%M)'))
        request.session['activity'].insert(0,activityVariable)


    return redirect("/")

def reset(request):
    request.session.clear()
    print "*" * 40
    print "Your session has been cleared!"
    print "*" * 40
    return redirect("/")
