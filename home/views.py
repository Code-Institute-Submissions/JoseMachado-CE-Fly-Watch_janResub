from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def home_products(request):
    """3 products from home page"""
    homeProducts = []
    product_one = '/media/rolex_daytona.jpeg'
    product_two = '/media/rolex_skydweller.jpeg'
    product_three = '/media/rolex_gmtmasterpepsi.jpeg'

    homeProducts.append(product_one,product_two,product_three)

    ThreeProducts = homeProducts.objects.all()

    template = 'home/index.html'
    context = {
        'ThreeProducts': ThreeProducts,
    }
    return render(request, template, context)