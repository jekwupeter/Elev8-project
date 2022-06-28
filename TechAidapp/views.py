from django.shortcuts import render

from TechAidapp.models import Hospital

# Create your views here.
def home(request):
    '''Renders the homepage'''
    return render (request,"index.html")

def base(request):
    if request.method == "POST":
        searched = request.POST['searched']
        hospitals = Hospital.objects.filter(
        city__contains=searched)

        '''Renders the basepage'''
        return render (request,"base.html", 
        {'searched': searched, 'hospitals': hospitals})
    else:
        return render (request,"base.html",{"searched": searched})
    # if request.method == "POST":
    #     searched = request.POST['searched']
    # return render (request,"hospitals.html",{"searched": searched})

def signin(request):
    '''Renders the signinpage'''
    return render (request,"signin.html")

def login(request):
    '''Renders the loginpage'''
    return render (request,"login.html")

def hospital(request):
    '''Renders the hospitalpage'''
    return render (request,"hospitals.html")

def healthEnquiry(request):
    '''Renders the how-do-you-feel page'''
    return render (request,"how-do-you-feel.html")