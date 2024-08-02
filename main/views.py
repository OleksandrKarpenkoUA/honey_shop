from django.shortcuts import redirect, render
from .forms import GoodsForm
from django.views.generic import ListView
from .models import Goods
from utils import MyMixin


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
