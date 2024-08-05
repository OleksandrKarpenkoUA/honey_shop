from django.shortcuts import render

from goods.models import Categories, Products

def index(request):
    return render(request, 'main/index.html')

def about_us_page(request):
    return render(request, 'main/about.html')

def contact_page(request):
    return render(request, 'main/contact.html')

def page_not_found(request, exception):
    return render(request, 'main/404.html')
