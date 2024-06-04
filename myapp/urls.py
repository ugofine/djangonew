
#from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact),
    path('createpage/',views.createpage),
    path('delete/<int:id>', views.delete),

]
