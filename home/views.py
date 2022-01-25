from django.shortcuts import render
from .models import Faq


def index(request):
    """ A view to return the index page """

    template = 'home/index.html'

    return render(request, template)


def faq(request):
    """ Page that returns with all posts """
    faqs = Faq.objects.all()

    context = {
        'faqs': faqs,
    }

    return render(request, 'home/faq.html', context)
