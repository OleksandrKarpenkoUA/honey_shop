from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import GoodsForm
from django.views.generic import ListView
from .models import Goods

categories = [
    {'id': 1, 'goods': 'Pure Honey', 'description': '500g of pure, organic honey.', 'product_url': 'main/images/honey1.jpg'},
    {'id': 2, 'goods': 'Flavored Honey', 'description': '500g of honey with natural flavors.', 'product_url': 'main/images/honey2.jpg'},
    {'id': 3, 'goods': 'Honeycomb', 'description': '250g of fresh honeycomb.', 'product_url': 'main/images/honey3.jpg'}
]

class HomeGoods(ListView):
    model = Goods
    template_name = 'main/index.html'
    context_object_name = 'goods'

def index(request):
    return render(request, 'main/index.html')

def page_not_found(request, exception):
    return render(request, 'main/404.html')

def products(request):
    goods = Goods.objects.all()
    return render(request, 'main/products.html', {'goods': goods})

def about_us(request):
    return render(request, 'main/about_us.html')

def add_goods(request):
    if request.method == 'POST':
        form = GoodsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')  # Redirect to the home page after successful submission
    else:
        form = GoodsForm()
    
    return render(request, 'main/add_goods.html', {'form': form})
