from django.shortcuts import render

from django.http import HttpResponse

# Please add below.
def index(request):
    return HttpResponse("Hello World")