from django.shortcuts import render, redirect
from .models import Thema, SubThema
from .forms import FormThema, FormSubThema
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def index(request):
    return render(request,"blog/index.html" )

@login_required
def blog(request):
    themas = Thema.objects.filter(owner=request.user).order_by("date")
    themas.order_by("date")
    data = {"themas":themas}
    return render(request,"blog/blog.html",data )

@login_required
def new_thema(request):
    if request.method != 'POST':
        form_thema = FormThema()
    else:
        form_thema = FormThema(data=request.POST)
        if form_thema.is_valid():
            thema = form_thema.save(commit=False)
            thema.owner = request.user
            thema.save()
            return redirect("blog_app:blog")
    
    data = {"form_thema":form_thema}
    return render(request,"blog/new_thema.html", data)

@login_required
def thema(request, id_thema):
    thema = Thema.objects.get(id=id_thema)
   

    subthema = thema.subthema_set.order_by("-date")
    data = {"subthema":subthema,"thema":thema}
    return render(request,"blog/thema.html",data)

@login_required
def new_subthema(request,id_thema):
    thema = Thema.objects.get(id=id_thema)
    check_owner(request.user,thema.owner)
    if request.method != 'POST':
        form = FormSubThema()
    else:
        form = FormSubThema(data=request.POST)
        if form.is_valid():
            subthema = form.save(commit=False)
            subthema.thema = thema
            subthema.save()
            return redirect("blog_app:thema", id_thema=id_thema)
    data = {"form":form,"thema":thema}
    return render(request,"blog/new_subthema.html", data)

@login_required
def edit_subthema(request, id_subthema):
    subthema = SubThema.objects.get(id=id_subthema)
    thema = subthema.thema
    check_owner(request.user,thema.owner)
    if request.method != "POST":
            form = FormSubThema(instance=subthema)
    else:
        form = FormSubThema(instance=subthema,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog_app:thema", id_thema=thema.id)
    data = {"form":form,"subthema":subthema,"thema":thema}
    return render(request,"blog/edit_subthema.html", data)

def showuser(request):
    users = User.objects.all()
    usersDic = {}

    for u in users:
        thema= u.thema_set.all()
        usersDic[u] = [c.thema for c in thema]



    data = {"userlist":users, "usersDic":usersDic}

    return render(request,"blog/userlist.html", data)

def check_owner(user, owner):

    if user != owner:
        raise Http404


