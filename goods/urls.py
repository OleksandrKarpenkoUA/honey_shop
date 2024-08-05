from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('category/<slug:category_slug>/', views.category_products, name='category_products'),
    path('product/', views.product, name='product'),
]

