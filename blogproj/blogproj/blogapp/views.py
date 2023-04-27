from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm, PostForm
from django.contrib.auth import login ,logout,authenticate
from django.contrib import messages
from .models import Post
from .models import Contact
# Create your views here.
def home(request):
    post=Post.objects.all().order_by('-id')
    return render(request,'blogapp/home.html',{'post':post})
def about(request):
    return render(request,'blogapp/about.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        return render(request, 'blogapp/contact.html')
    else:
        return render(request, 'blogapp/contact.html')
    
def dashboard(request):
    if request.user.is_authenticated:
        post=Post.objects.all()
        return render(request,'blogapp/dashboard.html',{'post':post})
    else:
        return HttpResponseRedirect('/login/')
def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congrats You are a Author ')
            form.save()
    else:
        form=SignupForm()
    return render(request,'blogapp/signup.html',{'form':form})
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
           form =AuthenticationForm(request=request,data=request.POST)
           if form.is_valid():
            uname=form.cleaned_data['username']
            upassword=form.cleaned_data['password']
            user=authenticate(username=uname,password=upassword)
            if user is not None:
                login(request,user)
                messages.success(request,'Login Success')
                return HttpResponseRedirect('/dashboard/')
        
        else:
           form=AuthenticationForm()
           return render(request,'blogapp/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')
     
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def add(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=PostForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            form=PostForm()
            return render(request,'blogapp/add.html',{'form':form})
    else :
        return HttpResponseRedirect('/login/')
def update(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST,instance=pi)
            if form.is_valid:
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            p=Post.objects.get(pk=id)
            form=PostForm(instance=p)
            return render(request,'blogapp/update1.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
def delete(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')