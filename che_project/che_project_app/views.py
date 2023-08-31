from datetime import date, datetime, time, timedelta, timezone
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from pytz import timezone
import json
from .models import Car, User, Car_status, Purpose, Brand, Car_model, Car_images

# Please add below.
@csrf_protect
def car_list(request):
    refinement_element = {
        "rent_date": request.POST.get("return_car_rent_date"),
    }

    cars = Car.objects.all()    
    context = {
        "lists": []
    }

    # 車の情報取得処理
    for car in cars:
        purposes = []
        pur_value = []
        purpose_count = 0
        for purpose in Purpose.objects.raw(
            "SELECT * FROM che_project_app_purpose WHERE car_id_id = %s", [car.id]
        ):
            pur_value.append(purpose)
        purposes.append(pur_value)
        user = User.objects.get(id=car.user_id_id)

        car_image = Car_images.objects.get(car_id_id=car.id, display_order=1)
        list_entity = {
            "car_id": car.id,
            "car_name": car.name,
            "car_price": car.price,
            "lend_start_date": car.lend_start_date,
            "lend_end_date": car.lend_end_date,
            "user_name": user.name,
            "purposes": purposes,
            "car_image": car_image.path,
            "purpose_count": purpose_count,
        }

        # マッチングアルゴリズム
        if request.POST.get("return_car_list"):
            filter_purpose = request.POST.get("return_car_list")
        else:
            filter_purpose = []
        if len(filter_purpose) != 0:
            for elm in list_entity["purposes"]:
                for a in elm:
                    if a.name in filter_purpose:
                        purpose_count += 1
                        print("{} purpose count {}".format(car.name, purpose_count))
        
        # ToDo
        #何もチェックされていないとき全て出るように実装
        if request.POST.get("return_car_rent_date"): # 日付絞り込みあり
            ref_start_date = datetime.strptime(refinement_element["rent_date"], '%Y-%m-%d')
            ref_str_date = timezone("UTC").localize(ref_start_date)
            
            if list_entity["lend_start_date"] < ref_str_date and list_entity["lend_end_date"] > ref_str_date:
                if purpose_count > 0: # タグマッチングあり
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

@csrf_protect
def info_update(request):
    """The page for editing user intent"""
    if request.POST.get("rent_date"):
        rent_date = request.POST.get("rent_date")
    else:
        rent_date = "2023-08-31"
    user_id = 7
    user = User.objects.get(id = user_id)
    context = {
        "user_id": user_id,
        "name": user.name,
        "tel_phone": user.phone_number,
        "location": user.address,
        "email": user.email,
    }

    purpose = request.POST.getlist("what_car") + request.POST.getlist("what_purpose")

    return render(request, "info_update.html", {"context": context, "purpose": purpose, "rent_date": rent_date})


def checkout(request, id):
    """The page for checkout"""
    context = {
        "id": id,
    }
    return render(request, "checkout.html")


def car_detail(request, id):
    car = get_object_or_404(Car, id = id)
    user = get_object_or_404(User, id = car.user_id_id)
    car_images = Car_images.objects.filter(car_id_id = car.id)
    model = get_object_or_404(Car_model, id = car.model_name_id)
    car_status = get_object_or_404(Car_status, id = car.car_status_id)
    car_brand = get_object_or_404(Brand, id = car.brand_id_id)
    pur_value = []
    for purpose in Purpose.objects.raw(
        "SELECT * FROM che_project_app_purpose WHERE car_id_id = %s", [car.id]
    ):
        pur_value.append(purpose)
    context = {
        'car': car,
        'car_images': car_images,
        'user': user,
        'car_status': car_status,
        'purposes': pur_value,
        'car_brand': car_brand,
        'model': model,
    }
    return render(request, "detail.html", context)


def checkout(request, id):
    car = get_object_or_404(Car, id = id)
    user = get_object_or_404(User, id = car.user_id_id)
    model = get_object_or_404(Car_model, id = car.model_name_id)
    car_image_first = Car_images.objects.get(car_id_id = car.id, display_order = 1)
    car_status = get_object_or_404(Car_status, id = car.car_status_id)
    car_brand = get_object_or_404(Brand, id = car.brand_id_id)
    pur_value = []
    for purpose in Purpose.objects.raw(
        "SELECT * FROM che_project_app_purpose WHERE car_id_id = %s", [car.id]
    ):
        pur_value.append(purpose)
    context = {
        'car': car,
        'car_image_first': car_image_first,
        'user': user,
        'car_status': car_status,
        'purposes': pur_value,
        'car_brand': car_brand,
        'model': model,
    }
    return render(request, 'checkout.html', context)

def car_avail_update(request, id):
    car = get_object_or_404(Car, id = id)
    if car.rental_available == True:
        car.rental_available = False
        car.updated_at = datetime.now()
    car.save()
    return render(request, 'success_page.html')
