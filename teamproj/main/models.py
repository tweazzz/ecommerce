from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = CharField(default='asd', max_length=200, null=True)
    email=models.EmailField('User Email')
    img = models.ImageField(default='main/static/main/img/profile.png', upload_to='main/static/img')

    def __str__(self):
        return f"{self.user.username}'s profile"




class Genre(models.Model):
    name = models.CharField("Genre", max_length=150)
    description = models.TextField("Description")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Zhanr"
        verbose_name_plural = "Zhanry"


class Films(models.Model):
    title = models.CharField('Nazvanie', max_length=100)
    description = models.CharField('Description', max_length=250)
    image = models.ImageField("image", upload_to="main\static\main\img",default='')
    genres = models.ManyToManyField(Genre, verbose_name='Zhanr')

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'