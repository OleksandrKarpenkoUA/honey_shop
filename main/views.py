from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string
from .forms import GoodsForm


categories = [
    {'id' : 1, 'goods' : 'Pure Honey', 'description' : '500g of pure, organic honey.', 'product_url' : 'main/images/honey1.jpg'},
    {'id' : 2, 'goods' : 'Flavored Honey', 'description' : '500g of honey with natural flavors.', 'product_url' : 'main/images/honey2.jpg'},
    {'id' : 3, 'goods' : 'Honeycomb', 'description' : '250g of fresh honeycomb.', 'product_url' : 'main/images/honey3.jpg'}
]



def index(request):
    return render(request, 'main/index.html')

def test(request, id):
    response = 'You\'re welcome! %d'
    return HttpResponse(response % id)


def page_not_found(request, exception):
    return render(request, 'main/404.html')

def products(request):
    return render(request, 'main/products.html')

def about_us(request):
    return render(request, 'main/about_us.html')

def add_goods(request):
    if request.method == 'POST':
        pass
    else:
        form = GoodsForm()
    
    return render(request, 'main/add_goods.html', {'form' : form})


    