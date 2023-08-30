from datetime import date, datetime, time, timedelta, timezone
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from pytz import timezone
from .models import Car, User, Car_status, Purpose, Brand, Car_model, Car_images

# Please add below.
@csrf_protect
def car_list(request):
    refinement_element = {
        "rent_date": request.POST.get("rent_date"),
    }

    cars = Car.objects.all()    
    context = {
        "lists": []
    }

    # 車の情報取得処理
    for car in cars:
        purposes = []
        pur_value = []
        for purpose in Purpose.objects.raw(
            "SELECT * FROM che_project_app_purpose WHERE car_id_id = %s", [car.id]
        ):
            pur_value.append(purpose)
        purposes.append(pur_value)
        user = User.objects.get(id=car.user_id_id)

        car_image = Car_images.objects.get(car_id_id=car.id, display_order=1)
        list_entity = {
            "car_name": car.name,
            "car_price": car.price,
            "lend_start_date": car.lend_start_date,
            "lend_end_date": car.lend_end_date,
            "user_name": user.name,
            "purposes": purposes,
            "car_image": car_image.path,
        }

        if request.POST.get("rent_date"): # 日付絞り込み
            ref_start_date = datetime.strptime(refinement_element["rent_date"], '%Y-%m-%d')
            ref_str_date = timezone("UTC").localize(ref_start_date)
            
            if list_entity["lend_start_date"] < ref_str_date and list_entity["lend_end_date"] > ref_str_date:
                context["lists"].append(list_entity)
        else:
            context["lists"].append(list_entity)
    
    return render(request, "car_list.html", {"lists": context["lists"], "refinement_element": refinement_element})


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


def checkout(request, id):
    """The page for checkout"""
    context = {
        "id": id,
    }
    return render(request, "checkout.html")


def index(request):
    return HttpResponse("Hello World")


def navbar(request):
    return render(request, "navbar.html")


def carlist(request):
    return render(request, "carlist.html")


def detail(request):
    context = {
        "car_name": "うんち",
        "owner_name": "うんちマン",
        "price": 900,
        "rental_avail": True,
        "address": "埼玉県所沢市",
    }
    return render(request, "car_detail.html", context)


def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    user = get_object_or_404(User, id=car.user_id_id)
    model = get_object_or_404(Car_model, id=car.model_name_id)
    car_status = get_object_or_404(Car_status, id=car.car_status_id)
    car_brand = get_object_or_404(Brand, id=car.brand_id_id)
    pur_value = []
    for purpose in Purpose.objects.raw(
        "SELECT * FROM che_project_app_purpose WHERE car_id_id = %s", [car.id]
    ):
        pur_value.append(purpose)
    context = {
        "car": car,
        "user": user,
        "car_status": car_status,
        "purposes": pur_value,
        "car_brand": car_brand,
        "model": model,
    }
    return render(request, "detail.html", context)


def checkout(request, id):
    car = get_object_or_404(Car, id=id)
    user = get_object_or_404(User, id=car.user_id_id)
    model = get_object_or_404(Car_model, id=car.model_name_id)
    car_status = get_object_or_404(Car_status, id=car.car_status_id)
    car_brand = get_object_or_404(Brand, id=car.brand_id_id)
    pur_value = []
    for purpose in Purpose.objects.raw(
        "SELECT * FROM che_project_app_purpose WHERE car_id_id = %s", [car.id]
    ):
        pur_value.append(purpose)
    context = {
        "car": car,
        "user": user,
        "car_status": car_status,
        "purposes": pur_value,
        "car_brand": car_brand,
        "model": model,
    }
    return render(request, "checkout.html", context)


def success_page(request, id):
    """This page show that customers ordered successfully"""
    context = {
        "id": id,
    }
    return render(request, "success_page.html")
