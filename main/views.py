from typing_extensions import ParamSpecKwargs
from django.shortcuts import render
from main import models as models


# Create your views here.
def index(request):

    context = {
        'menu': {
            'about': models.MenuContent.objects.get(id=2),
            'shop': models.MenuContent.objects.get(id=3),
            'faq': models.MenuContent.objects.get(id=4),
        },
        'page': {
            'about': models.AboutContent.objects.get(id=1)
        }
    }

    return render(request, 'main/index.html', context)