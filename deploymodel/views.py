from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import numpy as np
import joblib

def home(request):
    return render(request, "home.html")

def classifyglass(request):
    return render(request, "classifyglass.html")

def predictcarprice(request):
    return render(request, "predictcarprice.html")

def resultclassifyglass(request):
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

    return render(request, "resultclassifyglass.html", {'ans': ans, 'lis': lis})

def resultpredictcarprice(request):
    cls2 = joblib.load('car_price_predictor.sav')

    data_new = pd.DataFrame({
        'Present_Price':float(request.GET['Present_Price']),
        'Kms_Driven':int(request.GET['Kms_Driven']),
        'Fuel_Type':int(request.GET['Fuel_Type']),
        'Seller_Type':int(request.GET['Seller_Type']),
        'Transmission':int(request.GET['Transmission']),
        'Owner':int(request.GET['Owner']),
        'Age':int(request.GET['Age'])
    },index=[0])

    ans = cls2.predict(data_new)
    return render(request, "resultpredictcarprice.html", {'ans': ans, 'lis': data_new})