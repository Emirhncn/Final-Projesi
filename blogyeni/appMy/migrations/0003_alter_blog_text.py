# Generated by Django 4.2.13 on 2024-06-04 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0002_deneme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(verbose_name='İçerik'),
        ),
    ]
