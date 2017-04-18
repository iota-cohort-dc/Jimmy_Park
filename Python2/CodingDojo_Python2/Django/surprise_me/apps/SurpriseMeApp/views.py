from django.shortcuts import render, redirect
import random
VALUES = ["the","dog","is","running", "doing","in", "your", "my", "shoveling", "really", "jump", "computer", "javascript", "reading", "smoking", "big", "little"]

def index(request):

    return render(request,'SurpriseMeApp/index.html')

def process(request):

    x = request.POST['pick']

    # if x > 10:
    #     return render(request,'SurpriseMeApp/wrongNumber.html')
    context = {
    'word': [],
    }

    random.shuffle(VALUES)


    for i in range(0, int(x)):
        context['word'].append(VALUES[i])
        # word = random.choice(VALUES)
        # print word

    return render(request,'SurpriseMeApp/random.html', context)
