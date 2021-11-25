from django.shortcuts import render
from products.models import Product

# Create your views here.


def index(request):
    """ A view to return the index page """

    # homeProducts = []
    # product_one = '/media/rolex_daytona.jpeg'
    # product_two = '/media/rolex_daytona.jpeg'
    # product_three = '/media/rolex_daytona.jpeg'

    # homeProducts.append(product_one)
    # homeProducts.append(product_two)
    # homeProducts.append(product_three)
    # products = Product.objects.all()[:3]

    template = 'home/index.html'
    # context = {
        
    #     'homeProducts': products,
    # }

    return render(request, template)
