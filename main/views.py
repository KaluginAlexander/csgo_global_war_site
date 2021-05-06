from django.shortcuts import render
from main.models import MenuContent
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import hmac
import hashlib
import codecs
import json

# Константы
SECRET_KEY = 'eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6IjFnZnpjNC0wMCIsInVzZXJfaWQiOiI3OTAwMDIzOTUyMyIsInNlY3JldCI6ImFmYjFjNGRiYjllMGMwZGQ3OGFiYWIwOGJlZTBlZmUxZWMyZmU0OGYyZTc0YTk1NTY3MmFiNzgwMDAzNDY2NmUifX0='

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


@csrf_exempt
def notify(request):
    print('=================')
    if request.method == 'POST':
        
        bill = json.loads(request.body)['bill']
        
        # Получаем параметры
        amount = bill['amount']['value']
        billId = bill['billId']
        siteId = bill['siteId']
        status = bill['status']['value']
        
        invoice_parameters = f"RUB|{amount}|{billId}|{siteId}|{status}"
        accept = hmac.new(codecs.encode(SECRET_KEY), msg=codecs.encode(invoice_parameters), digestmod=hashlib.sha256).hexdigest()

        # проверка подлиности
        if request.headers['X-Api-Signature-SHA256'] == accept:

            # Получаем аккаунт
            nickname = bill['customer']['account']

    return HttpResponse(status=200)