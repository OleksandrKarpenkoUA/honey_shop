from django.shortcuts import redirect, render


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def page_not_found(request, exception):
    return render(request, 'main/404.html')


