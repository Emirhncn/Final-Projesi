# Generated by Django 4.2.13 on 2024-06-05 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, verbose_name='Ad - Soyad')),
            ],
        ),
    ]