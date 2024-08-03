# main/urls.py
from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_us_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
]
