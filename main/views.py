from django.shortcuts import render
from .models import Post
import joblib


def home(request):
    return render(request, 'index.html')
        

def result(request):

    cls = joblib.load('bdcrime_model.sav')

    if request.method == 'POST':
        if request.POST.get('unit_name') and request.POST.get('year') and request.POST.get('dacoity') and request.POST.get('robbery') and request.POST.get('murder') and request.POST.get('speedy_trial') and request.POST.get('riot') and request.POST.get('wcrepresion') and request.POST.get('kidnapping') and request.POST.get('policeassult') and request.POST.get('burglary') and request.POST.get('theft') and request.POST.get('othercases') and request.POST.get('armsact') and request.POST.get('explosive') and request.POST.get('nacrotics') and request.POST.get('smuggling'):
            post = Post()
            post.unit_name = request.POST.get('unit_name')
            post.year = request.POST.get('year')
            post.dacoity = request.POST.get('dacoity')
            post.robbery = request.POST.get('robbery')
            post.murder = request.POST.get('murder')
            post.speedy_trial = request.POST.get('speedy_trial')
            post.riot = request.POST.get('riot')
            post.wcrepresion = request.POST.get('wcrepresion')
            post.kidnapping = request.POST.get('kidnapping')
            post.policeassult = request.POST.get('policeassult')
            post.burglary = request.POST.get('burglary')
            post.theft = request.POST.get('theft')
            post.othercases = request.POST.get('othercases')
            post.armsact = request.POST.get('armsact')
            post.explosive = request.POST.get('explosive')
            post.nacrotics = request.POST.get('nacrotics')
            post.smuggling = request.POST.get('smuggling')
            post.save()

    lis = []
    lis.append(request.POST['unit_name'])
    lis.append(request.POST['year'])
    lis.append(request.POST['dacoity'])
    lis.append(request.POST['robbery'])
    lis.append(request.POST['murder'])
    lis.append(request.POST['speedy_trial'])
    lis.append(request.POST['riot'])
    lis.append(request.POST['wcrepresion'])
    lis.append(request.POST['kidnapping'])
    lis.append(request.POST['policeassult'])
    lis.append(request.POST['burglary'])
    lis.append(request.POST['theft'])
    lis.append(request.POST['othercases'])
    lis.append(request.POST['armsact'])
    lis.append(request.POST['explosive'])
    lis.append(request.POST['nacrotics'])
    lis.append(request.POST['smuggling'])
    print(lis)

    pred = cls.predict([lis])

    print(pred)

    return render(request, 'result.html',{'pred':pred})



        
        