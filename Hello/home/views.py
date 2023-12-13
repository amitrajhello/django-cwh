from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is our homepage.")

def about(request):
    return HttpResponse("this is our about page.")

def services(request):
    return HttpResponse("this is our services page.")

def contact(request):
    return HttpResponse("this is our contact page.")
