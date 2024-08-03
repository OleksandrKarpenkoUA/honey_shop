from django.urls import path

from main import views


urlpatterns = [
    path('', views.index, name='index'),
]

handler404 = 'main.views.page_not_found'
