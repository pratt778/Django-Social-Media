from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='signin')
def home(request):
    return render(request,'base.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    data={}
    myform = RegisterForm()
    data['form']=myform
    if request.method=="GET":
        myform = RegisterForm(request.GET)
        if myform.is_valid():
            myform.save()
            return redirect("signin")
    return render(request,'signup.html',data)

def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    data={}
    myform = LoginForm()
    data['form']=myform
    if request.method == "GET":
        myform = LoginForm(request.GET)
        if myform.is_valid():
            username = myform.cleaned_data['username']
            password = myform.cleaned_data['password']
            auth = authenticate(request,username=username,password=password)
            if auth is not None:
                login(request,auth)
                return redirect('home')
    return render(request,'signin.html',data)

@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('signin')