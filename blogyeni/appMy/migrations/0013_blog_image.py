# Generated by Django 4.2.13 on 2024-06-06 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0012_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(max_length=300, null=True, upload_to='', verbose_name='Blog Resmi'),
        ),
    ]
