from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    homeProducts=[]
    product_one = '/media/rolex_daytona.jpeg'
    product_two = '/media/rolex_daytona.jpeg'
    product_three = '/media/rolex_daytona.jpeg'

    homeProducts.append(product_one)
    homeProducts.append(product_two)
    homeProducts.append(product_three)

    products = homeProducts.objects.all()

    template = 'home/index.html'
    context = {
        'products': products,
        'homeProducts':homeProducts,
    }

    return render(request, context, template)
