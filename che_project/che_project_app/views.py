from django.http import HttpResponse
from django.shortcuts import render
from .models import Car, User, Purpose

# Please add below.
def car_list(request):
    """The page for car list"""
    cars = Car.objects.all()
    context = {
        "lists": []
    }

    for car in cars:
        purposes = []
        pur_value = []
        pur_value = []
        for purpose in Purpose.objects.raw("SELECT * FROM che_project_app_purpose WHERE car_id_id = %s", [car.id]):
            pur_value.append(purpose)
        purposes.append(pur_value)
        user = User.objects.get(id = car.user_id_id)

        list_entity = {
            "car_name": car.name,
            "car_price": car.price,
            "lend_start_date": car.lend_start_date,
            "lend_end_date": car.lend_end_date,
            "user_name": user.name,
            "purposes": purposes
        }
        context["lists"].append(list_entity)
           
    return render(request, "car_list.html", context)

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
