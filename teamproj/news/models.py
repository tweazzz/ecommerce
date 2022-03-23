from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField('Name',max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Statya')
    date = models.DateTimeField('Date of established')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'