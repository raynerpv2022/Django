from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
 
def register(request):
    if request.method !="POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
           user_form = form.save() 
           login(request,user_form)
           return redirect("blog_app:index")

    data = {"form":form}
    return render(request,"registration/register.html",data)

 


    