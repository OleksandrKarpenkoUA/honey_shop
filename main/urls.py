from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='home_page'),
    path('products/', views.products, name='products'),
    path('about_us/', views.about_us, name='about_us'),
    path('add/', views.add_goods, name='add'),
]