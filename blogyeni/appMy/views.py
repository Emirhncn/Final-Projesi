from django.shortcuts import render, redirect
from appMy.models import *
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def indexPage(request):
    
    blog_list = Blog.objects.all()
    
    context = {
        "blog_list":blog_list,
        
    }
    return render(request,"index.html",context)

def categoryPage(request, slug=None):
    if slug:
        blog_list = Blog.objects.filter(category__slug = slug).order_by("-id") #order_by() sıralamayı en son eklenenden itibaren yapmak için kullandık
    else:
        blog_list = Blog.objects.all().order_by("-id")


    query = request.GET.get("query")
    if query:
        blog_list = blog_list.filter(Q(title__icontains=query) | 
                                    Q(text__icontains=query) | 
                                    Q(author__icontains=query) |
                                    Q(category__title__icontains=query)
                                    )
    

    category_list = Category.objects.all()
    
    context = {
        "blog_list":blog_list,
        "category_list":category_list,
    }
    return render(request,"category.html",context)

def aboutPage(request):
    
    blog_list = Blog.objects.all() # all liste mantığında çalışır [1.blog, 2.blog, 3.blog]
    blog_isactive = Blog.objects.filter(isactive=True) # liste mantığında çalışır içerisinde hiçbir şey yoksa [] bu şekilde kalır.
    blog2 = Blog.objects.get(id=2) # tek bir tane çeker not: eğer çekilen blog yoksa hata verir.
    denemeler = Deneme.objects.all()
    
    context = {
        "blog_list":blog_list,
        "blog_isactive":blog_isactive,
        "blog2":blog2,
        "denemeler":denemeler,
    }
    return render(request,"about.html",context)

# DENEME DETAY START
def denemePage(request, slug):
    deneme = Deneme.objects.get(baslik=slug)
    context = {
        "deneme":deneme,
    }
    return render(request,"deneme.html",context)
# DENEME DETAY END

def contactPage(request):
    
    if request.method == "POST":
        fname = request.POST.get("fullname") 
        title = request.POST.get("title")
        email = request.POST.get("email")
        text = request.POST.get("text")
        
        contact = Contact(fullname=fname, title=title, email=email, text=text) # obje oluşturuldu değişkene gönderildi
        contact.save() # değişken SQL DATABASE e kaydedildi
        return redirect("contactPage")
    context = {}
    return render(request,"contact.html",context)

def detailPage(request, bid):
    # kullanıcı ya da frontend den bilgi alabilmenin iki yöntemi vardır.
    # 1) url adresinden
    # 2) formlardan
    
    if bid.isnumeric():
        blog = Blog.objects.get(id=bid) # getiremediği durumda ValueError hatasını verir
    else:
        blog = Blog.objects.get(slug=bid) # getiremediği durumda ValueError hatasını verir


    comment_list = Comment.objects.filter(blog=blog)
    blog_list = Blog.objects.filter(slug=bid)


    if request.method == "POST":
        fullname = request.POST.get("fullname")
        text = request.POST.get("comment")
        if fullname and text:
            comment = Comment(fullname=fullname, text=text, blog=blog)
            comment.save()
            return redirect("detailPage", bid)

    context = {
        "blog":blog,
        "blog_list":blog_list,
        "comment_list":comment_list,
    }
    return render(request,"detail.html",context)

    # USER PAGE

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("indexPage")
            else:
                messages.error(request, "Kullanıcı adı veya şifre yanlış!")
                messages.success(request, "SDASDASDASDSASD")
    context = {}
    return render(request, "user/login.html", context)


def registerPage(request):
    
    if request.method =="POST":
        fname = request.POST.get("fname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
    
        if password1 == password2:
            if not User.objects.filter(username=username).exists(): # hiçbir kullanıcı bulamaması gerekiyor.
                if not User.objects.filter(email=email).exists():  # hiçbir email bulamaması gerekiyor.
                    # KAYIT ET
                    user = User.objects.create_user(first_name=fname,last_name=lastname,email=email,username=username,password=password1)
                    user.save()
                    return redirect("indexPage")
    context = {}
    return render(request, "user/register.html", context )

def logoutUser(request):
    logout(request)
    return redirect("loginPage")

def passwordChange(request):
    
    
    
    if request.method == "POST":
        username = request.POST.get("username")
        hp = request.POST.get("hiddenpassword")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        try:
            user = User.objects.get(username=username)
            if password1 == password2:
                if user.userinfo.hidden_password == hp: # onetoone : "user.userinfo" bir modelden başka bir modeli çağırmamıza yarar.
                    user.set_password(password1)
                    user.save()
                    messages.success(request, "Şifreniz başarıyla değiştirildi!")
                    return redirect("loginPage")
                else:
                    messages.error(request, "Gizli yanıtınız yanlış!")
                    
            else:
                messages.error(request, "Şifreler uyuşmuyor!")
        except:
            messages.error(request, "Kullanıcı kayıtlı değil!")
    
    context = {}
    return render(request, "user/password.html",context)


















