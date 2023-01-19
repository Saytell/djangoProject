from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def blog(request):
    return render(request, 'blog.html')
def product(request):
    return render(request, 'product.html')
def blog_single(request):
    return render(request, 'blog_single.html')
def cart(request):
    return render(request, 'cart.html')
def contact(request):
    return render(request, 'contact.html')
def regular(request):
    return render(request, 'regular.html')
def shop(request):
    return render(request, 'shop.html')