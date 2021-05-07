from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from shop.models import Product
import hashlib, codecs, hmac
import json, sys, os


slash = ('/', '\\')['\\' in os.path.dirname(__file__)]
botPath = slash.join(os.path.dirname(__file__).split(slash)[0:-2]) + slash + 'CSGO_vk_bot'
invoicesPath = botPath + '/core/bot/database/data'
sys.path.insert(0, botPath)

from core.bot.database import main as botDB

# Константы
SECRET_KEY = 'eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6IjFnZnpjNC0wMCIsInVzZXJfaWQiOiI3OTAwMDIzOTUyMyIsInNlY3JldCI6ImFmYjFjNGRiYjllMGMwZGQ3OGFiYWIwOGJlZTBlZmUxZWMyZmU0OGYyZTc0YTk1NTY3MmFiNzgwMDAzNDY2NmUifX0='
makedBills = []


@csrf_exempt
def notify(request):
    if request.method == 'POST':
        
        bill = json.loads(request.body)['bill']
        
        # Получаем параметры
        amount = bill['amount']['value']
        billId = bill['billId']
        siteId = bill['siteId']
        
        invoice_parameters = f"RUB|{amount}|{billId}|{siteId}|PAID"
        accept = hmac.new(codecs.encode(SECRET_KEY), msg=codecs.encode(invoice_parameters), digestmod=hashlib.sha256).hexdigest()

        # проверка подлиности
        if request.headers['X-Api-Signature-SHA256'] == accept and billId not in makedBills:

            # Получаем остальные данные
            nickname = bill['customer']['account']
            productId = bill['customFields']['productId']
            product = Product.objects.get(id = int(productId))
            
            # Проверка, есть ли игрок с таким ником
            result = botDB.fetchone('users', f"SELECT id FROM Users WHERE nickname = '{nickname}'", invoicesPath)

            if result:
                userId = result[0]

                # Добавляем в бд записи
                botDB.request('delay', f"INSERT INTO Invoices VALUES('{nickname}', {product.amount})", invoicesPath)
                botDB.request('delay', f"INSERT INTO Actions VALUES(NULL, 'donate-gold', {userId}, 1)", invoicesPath)

            # Помечаем заказ выполненым
            makedBills.append(billId)

    return HttpResponse(status = 200)