from django.shortcuts import render

from django.http import HttpResponse

# Please add below.
def index(request):
    return HttpResponse("Hello World")
def navbar(request):
    return render(request, 'navbar.html')
def carlist(request):
    return render(request, 'carlist.html')
def detail(request):
    context = {
        'car_name':"うんち",
        'owner_name':"うんちマン",
        'price':900,
        'rental_avail':True,
        'address':"埼玉県所沢市",
    }
    return render(request, 'car_detail.html', context)
