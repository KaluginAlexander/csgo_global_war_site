from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Product(models.Model):
    title = models.CharField('название', max_length=150)
    subscription = models.CharField('описание', max_length=500)
    picture = models.ImageField('иконка', upload_to='icons/product')
    cost = models.IntegerField('цена', validators=[MinValueValidator(0)])
    amount = models.IntegerField('количество выдаваемого золота', validators=[MinValueValidator(0)])


    def __str__(self):
        return f"{self.title} ({self.amount})"

    
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['id']