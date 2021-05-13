from typing_extensions import ParamSpecKwargs
from django.shortcuts import render
from main.models import AboutContent, MenuContent
from shop.models import Product

# Create your views here.
def index(request):

    context = {
        'menu': {
            'about': MenuContent.objects.get(id=2),
            'shop': MenuContent.objects.get(id=3),
            'faq': MenuContent.objects.get(id=4),
        },
        'page': {
            'about': AboutContent.objects.get(id=1)
        },
        'products': Product.objects.all()
    }

    return render(request, 'main/index.html', context)