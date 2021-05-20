from typing_extensions import ParamSpecKwargs
from django.shortcuts import redirect, render
from django.urls import reverse
from main.models import AboutContent, MenuContent, Question
from shop.models import Product

# Create your views here.
def index(request):

    if request.method == "POST":
        
        data = request.POST

        if 'nickname' in data.keys() and 'productId' in data.keys():
            pay_url = Product.get_pay_url(data['nickname'], data['productId'])

            return redirect(pay_url)

        else:
            return redirect(reverse('home'))

    else:

        context = {
            'menu': {
                'about': MenuContent.objects.get(id=2),
                'shop': MenuContent.objects.get(id=3),
                'faq': MenuContent.objects.get(id=4),
                'game': MenuContent.objects.get(id=5),
            },
            
            'page': {
                'about': AboutContent.objects.get(id=1)
            },

            'products': Product.objects.all(),
            'questions': Question.objects.all(),
        }

        return render(request, 'main/index.html', context)