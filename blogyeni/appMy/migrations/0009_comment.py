# Generated by Django 4.2.13 on 2024-06-05 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0008_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, verbose_name='Ad - Soyad')),
                ('text', models.TextField(verbose_name='Yorum')),
                ('date_now', models.DateTimeField(verbose_name='Tarih - Saat')),
            ],
        ),
    ]
