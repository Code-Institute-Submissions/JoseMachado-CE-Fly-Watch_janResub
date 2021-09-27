from django.shortcuts import render

# Create your views here.
# functions go here

def index(request):
    return render(request, 'home/index.html')
