from django.shortcuts import render
from main.models import MenuContent

# Create your views here.
def index(request):
    
    context = {
        'menu': {
            'info': MenuContent.objects.get(id=1),
            'about': MenuContent.objects.get(id=2),
            'shop': MenuContent.objects.get(id=3),
            'faq': MenuContent.objects.get(id=4),
        },
    }

    return render(request, 'main/index.html', context)