from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import json
from .models import Car, User, Car_status, Purpose, Brand, Car_model

# Please add below.
def car_list(request):
    """The page for car list"""
    return render(request, "car_list.html")

def chat(request, id):
    """The page for car list"""
    context = {
        "id": id,
    }
    return render(request, "chat.html", context)

def detail_view(request, id):
    # Retrieve data based on the id parameter and pass it to the template
    context = {
        "id": id,
    }
    return render(request, "detail.html", context)

def info_update(request):
    """The page for editing user intent"""
    return render(request, "info_update.html")

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

def car_detail(request, id):
    car = get_object_or_404(Car, id = id)
    user = get_object_or_404(User, id = car.user_id_id)
    model = get_object_or_404(Car_model, id = car.model_name_id)
    car_status = get_object_or_404(Car_status, id = car.car_status_id)
    car_brand = get_object_or_404(Brand, id = car.brand_id_id)
    # purposes = Purpose.objects.filter(car_id_id = id).values()
    pur_value = []
    for purpose in Purpose.objects.raw('SELECT * FROM che_project_app_purpose WHERE car_id_id = %s', [car.id]):
        pur_value.append(purpose)
    context = {
        'car': car,
        'user': user,
        'car_status': car_status,
        'purposes': pur_value,
        'car_brand': car_brand,
        'model': model,
    }
    return render(request, 'detail.html', context)