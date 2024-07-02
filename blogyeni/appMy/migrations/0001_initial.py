# Generated by Django 4.2.13 on 2024-06-04 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('text', models.TextField(verbose_name='')),
                ('date_now', models.DateTimeField(verbose_name='Tarih - Saat')),
                ('author', models.CharField(max_length=50, verbose_name='Yazar')),
            ],
        ),
    ]
