from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeGoods.as_view(), name='home_page'),
    path('products/', products, name='products'),
    path('about_us/', about_us, name='about_us'),
    path('add/', add_goods, name='add'),
]

handler404 = 'main.views.page_not_found'
