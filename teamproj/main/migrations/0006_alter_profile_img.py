# Generated by Django 4.1.7 on 2023-05-10 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='main/static/main/img/profile.png', upload_to='main/static/img'),
        ),
    ]