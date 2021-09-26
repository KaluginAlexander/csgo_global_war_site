from django.db import models
from django.core.validators import MinValueValidator

from csgo_global_war_site import settings
# Create your models here.
class Product(models.Model):
    title = models.CharField('название', max_length=150)
    subscription = models.CharField('описание', max_length=500)
    picture = models.ImageField('иконка', upload_to='icons/product')
    cost = models.IntegerField('цена', validators=[MinValueValidator(0)])
    amount = models.IntegerField('количество выдаваемого золота', validators=[MinValueValidator(0)])


    def payUrl(self, nickname):
        return Product.get_pay_url(nickname, self.pk)
    
    def __str__(self):
        return f"{self.title} ({self.amount})"

    @staticmethod
    def get_pay_url(account: str, productId: int, successUrl = 'https://global-war-csgo.ru/'):
        global PUBLIC_KEY
        amount = Product.objects.get(id = int(productId)).cost
        
        return f'https://oplata.qiwi.com/create?publicKey={settings.QIWI_PUBLIC_KEY}&account={account}&amount={amount}&successUrl={successUrl}&customFields[productId]={productId}&customFields[themeCode]=Aleksandr-KWK5mSrChu'

    
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['cost']