from django.shortcuts import render, get_object_or_404
from goods.models import Categories, Products

def catalog(request):
    categories = Categories.objects.all()
    context = {
        'title': 'Honey Shop',
        'categories': categories,
    }
    return render(request, 'goods/catalog.html', context)

def category_products(request, category_slug):
    category = get_object_or_404(Categories, slug=category_slug)
    products = Products.objects.filter(category=category)
    context = {
        'title': f'Products in {category.name}',
        'category': category,
        'products': products,
    }
    return render(request, 'goods/category_products.html', context)

def product(request, product_id):
    product = Products.objects.get(id=product_id)

    context = {
        'product' : product
    }    
    return render(request, 'goods/product.html', context=context)