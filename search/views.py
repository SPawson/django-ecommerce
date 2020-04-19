from django.shortcuts import render
from products.models import Product

# Create your views here.

def do_Search(request):
    """ Retrieves the product based on the search query"""
    products = Product.objects.filter(name_icontains=request.GET['q'])
    return render(request, "products.html", {'products': products})

