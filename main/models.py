from django.db import models

# Create your models here.
class MenuContent(models.Model):
    key = models.CharField('ключ', max_length=150)
    value = models.TextField('значение', max_length=500)
    picture = models.ImageField('картинка', upload_to = 'pictures/icons/menu')

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = 'контент'
        verbose_name_plural = 'контент меню'
        ordering = ['pk']