from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from . import models
from .forms import *
# Create your views here.
def home(request):
    service = models.Service.objects.all()
    context ={"service":service}
    return render(request, "index.html", context)

def gallery(request):
    gallery= models.Gallery.objects.all().order_by('-id')
    context= {"gallery":gallery}
    return render(request, 'gallery.html', context)

def gallery_detail(request, id):
    gallery= models.Gallery.objects.get(id=id)
    galdetail = models.GalleryImage.objects.filter(gallery=gallery).order_by('-id')
    return render(request, 'galleryimg.html',  {'galdetail' : galdetail,'gallery':gallery} )

def pricing(request):
    price= models.Subplan.objects.all()
    context={"price":price}
    return render(request, 'pricing.html', context )




def register(response):
    if response.method == "POST":
        form = SignUp(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = SignUp()
    return render(response, "registration/signup.html", {"form": form})


def services(request):
    services= models.Service.objects.all().order_by('-id')
    context= {"services":services}
    return render(request, 'services.html', context)
    

def sessions(request):
    session= models.Session.objects.all().order_by('id')
    context= {"session":session}
    return render(request, 'session.html', context)
    
def attendance(request):
    attendance= models.Attendance.objects.all().order_by('id')
    context= {"attendance":attendance}
    return render(request, 'attendance.html', context)