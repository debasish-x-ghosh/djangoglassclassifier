from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request, "home.html")

def result(request):
    cls = joblib.load('final_model.sav')

    lis=[]
    lis.append(request.GET['RI'])
    lis.append(request.GET['NA'])
    lis.append(request.GET['MG'])
    lis.append(request.GET['AI'])
    lis.append(request.GET['SI'])
    lis.append(request.GET['K'])
    lis.append(request.GET['CA'])
    lis.append(request.GET['BA'])
    lis.append(request.GET['FE'])
    print(lis)

    ans = cls.predict([lis])

    return render(request, "result.html", {'ans': ans, 'lis': lis})