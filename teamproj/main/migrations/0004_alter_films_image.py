# Generated by Django 4.1.7 on 2023-05-03 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_films_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='image',
            field=models.ImageField(default='', upload_to='main\\static\\main\\img', verbose_name='image'),
        ),
    ]