from django.shortcuts import render, HttpResponse, redirect
from random import randint
import datetime

def index(request):

    if 'activity' not in request.session:
        request.session['activity'] = [] # empty bucket for append..

    if 't_gold' not in request.session:
        request.session['t_gold'] = 0

    return render(request, ('index.html'))

def process(request):

    if request.POST['building'] == "farm":
        gold = randint(12,20)
        print gold
        request.session['t_gold'] += gold ## taking gold in above and adding the gold from randint
        prnt_farm_actvty = "You got " + str(gold) + " gold coins from the farm." + "  " +  str(datetime.datetime.now().strftime('(%Y/%m/%d %H:%M)'))

        request.session['activity'].append(prnt_farm_actvty) # append ...to activity i think
        print request.session['activity']


    if request.POST['building'] == "cave":
        gold = randint(5,10)
        print gold
        request.session['t_gold'] += gold ## taking gold in above and adding the gold from randint
        prnt_cave_actvty = "You got " + str(gold) + " gold coins from the farm." + "  " +  str(datetime.datetime.now().strftime('(%Y/%m/%d %H:%M)'))
        request.session['activity'].append(prnt_cave_actvty)

    if request.POST['building'] == "house":
        gold = randint(2,5)
        print gold
        request.session['t_gold'] += gold ## taking gold in above and adding the gold from randint
        prnt_house_actvty = "You got " + str(gold) + " gold coins from the farm." + "  " +  str(datetime.datetime.now().strftime('(%Y/%m/%d %H:%M)'))
        request.session['activity'].append(prnt_house_actvty)

    if request.POST['building'] == "casino":
        gold = randint(-50,50)
        print gold
        request.session['t_gold'] += gold ## taking gold in above and adding the gold from randint
        prnt_casino_actvty = "You got " + str(gold) + " gold coins from the farm." + "  " +  str(datetime.datetime.now().strftime('(%Y/%m/%d %H:%M)'))
        request.session['activity'].append(prnt_casino_actvty)

    return redirect( ("/"))

def reset(request):
    request.session.clear()
    print "Your session has been terminated"

    return redirect( ("/"))

# NOTES:*********************************************************************

# think of request as a big bucket
# session and post are smaller buckets inside of request

# 2 ways you can get values to print to html
        #    use -->name variable context = {
        #                             'key': value,
        #                         }
        #    inside html: {{ key }}
        #    just put the key inside {{ }} to get the value printed
                    #       or
            # the other way is to
            # in views.py use
            # request.session['whatevervalueorvariable']
            # in html use {{ request.session.whatevervalueorvariable }}
