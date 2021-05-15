from django.db import models
from django.core.validators import MinValueValidator

PUBLIC_KEY = '48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iP3EYJiPrgY9L9hTisRHtPRnbUTgw7FKt58sZoJ6Lp2GkMvVudi8zu3hfdPpRFLG6FpBxJ4WCf7WDBboRs3W9ir2ywtfUU9rsVGY5KexvQ2'

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
        
        return f'https://oplata.qiwi.com/create?publicKey={PUBLIC_KEY}&account={account}&amount={amount}&successUrl={successUrl}&customFields[productId]={productId}'

    
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['cost']