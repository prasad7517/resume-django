from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('temp1/',views.temp1,name='temp1'),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
    path('temp2/',views.temp2,name='temp2'),
    path('generate-pdf2/', views.generate_pdf2, name='generate_pdf2'),
    
]
