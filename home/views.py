from django.shortcuts import render

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

    template = 'home/index.html'
    # context = {
        
    #     'homeProducts': homeProducts,
    # }

    return render(request, template)
