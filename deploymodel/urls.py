from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('classifyglass/', views.classifyglass, name="classifyglass"),
    path('predictcarprice/', views.predictcarprice, name="predictcarprice"),
    path('resultclassifyglass/', views.resultclassifyglass, name="resultclassifyglass"),
    path('resultpredictcarprice/', views.resultpredictcarprice, name="resultpredictcarprice"),
    path('lcreadpdf/', views.lcreadpdf, name="lcreadpdf"),
    path('loadpdfopnai/', views.loadpdfopnai, name="loadpdfopnai"),
    path('resultlcreadpdf/', views.resultlcreadpdf, name="resultlcreadpdf")
]
