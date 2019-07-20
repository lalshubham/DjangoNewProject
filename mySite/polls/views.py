from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")


def contact(request):
    return HttpResponse("Contact Me")


def template(request):
    return render(request, 'polls/layouts/homepage.html')

def templateabout(request):
    return render(request, 'polls/about.html')
