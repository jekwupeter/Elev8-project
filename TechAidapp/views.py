from django.shortcuts import render

# Create your views here.
def home(request):
    '''Renders the homepage'''
    return render (request,"index.html")

def signin(request):
    '''Renders the signinpage'''
    return render (request,"signin.html")

def login(request):
    '''Renders the loginpage'''
    return render (request,"login.html")

def hospital(request):
    '''Renders the hospitalpage'''
    return render (request,"hospitals.html")