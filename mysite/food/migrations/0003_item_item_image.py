# Generated by Django 2.2.7 on 2019-11-30 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20191125_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://cdn.dribbble.com/users/1012566/screenshots/4187820/topic-2.jpg', max_length=500),
        ),
    ]