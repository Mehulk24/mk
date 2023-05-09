from django.shortcuts import render, HttpResponse
from datetime import datetime
from MK.models import contact
from django.contrib import messages

# Create your views here.
def index(request):
    messages.success(request, "Your Massage is Send .")
    if request.method == "POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        contacts = contact(fname=fname,lname=lname,email=email,msg=msg)
        contacts.save()
        messages.success(request, "Massage submited !")
        
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def callout(request):
    return render(request,'callout.html.html')

def portfolio(request):
    return render(request,'portfolio.html')
    # return HttpResponse("This is a home page")