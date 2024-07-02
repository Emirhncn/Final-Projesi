from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

# model tablosu oluşturmak için
# python3 manage.py makemigrations
# python3 manage.py migrate
# SQL DATABASE içerisine tablo oluşturur.



class Category(models.Model):
    title = models.CharField(("Kategori Başlığı"), max_length=50)
    slug = models.SlugField(("Slug"))
    
    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(("Başlık"), max_length=50) # html input text ten hiçbir farkı yok
    text = models.TextField(verbose_name="İçerik") # html üzerindeki textarea
    date_now = models.DateTimeField(("Tarih - Saat"), auto_now=False, auto_now_add=False) # html input datetime 
    author = models.CharField(("Yazar"), max_length=50)
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE,null=True)
    image = models.ImageField(("Blog Resmi"), upload_to="", max_length=300,null=True)
    # null değerlere None değer gönderir
    # default başlangıç değeri gönder
    # blank = True ise doldurulması zorunlu değil, zorunlu alanları zorunlu olmaktan çıkarır.
    subtitle = models.CharField(("Alt Başlık"), max_length=50 ,null=True,blank=True)
    isactive = models.BooleanField(("Sayfada Göster"),default=False)
    slug = models.SlugField(("Slug"),blank=True)
    def __str__(self):
        return self.title
    
    def save(self):
        self.slug = slugify(self.title)
        super().save()

class Comment(models.Model):
    blog = models.ForeignKey(Blog,verbose_name=("Blog"), on_delete=models.CASCADE,null=True) # {}
    fullname = models.CharField(("Ad - Soyad"), max_length=50)
    text = models.TextField(("Yorum")) 
    date_now = models.DateTimeField(("Tarih - Saat"), auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.blog.title


class Deneme(models.Model):
    baslik = models.CharField(("Başlık Deneme"), max_length=50)
    def __str__(self):
        return self.baslik

class Contact(models.Model):
    fullname = models.CharField(("Ad Soyad"), max_length=50)
    title = models.CharField(("Konu"), max_length=50)
    email = models.EmailField(("Email"), max_length=254)
    text = models.TextField(("İletişim Mesajı"))
    def __str__(self):
        return self.title

class Userinfo(models.Model):
    user = models.OneToOneField(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    hidden_password = models.CharField(("Gizli Yanıt"), max_length=50)
    # tel =
    # address =
    
    def __str__(self):
        return self.user.username
