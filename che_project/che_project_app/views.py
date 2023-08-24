from django.shortcuts import render

from django.http import HttpResponse

# Please add below.
def index(request):
    return HttpResponse("Hello World")
def navbar(request):
    return render(request, 'navbar.html')
def carlist(request):
    return render(request, 'carlist.html')