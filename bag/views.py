from django.shortcuts import render

# Create your views here.
# functions go here


def view_bag(request):
    """ return the bag page"""
    return render(request, 'bag/bag.html')


