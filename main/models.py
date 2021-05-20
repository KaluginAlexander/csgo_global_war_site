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
        verbose_name_plural = 'контент секции "Меню"'
        ordering = ['pk']


class AboutContent(models.Model):
    key = models.CharField('ключ', max_length=150)
    value = models.TextField('значение', max_length=2300)

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = 'контент'
        verbose_name_plural = 'контент секции "О нас"'
        ordering = ['pk']


class Question(models.Model):
    question = models.TextField('вопрос', max_length=500)
    answer = models.TextField('ответ', max_length=500)

    def __str__(self) -> str:
        return self.question

    class Meta:
        ordering = ['pk']
        verbose_name = 'вопрос'
        verbose_name_plural = 'контент секции "FAQ"'