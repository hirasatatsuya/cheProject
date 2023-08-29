from django.http import HttpResponse
from django.shortcuts import render


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


def checkout(request, id):
    """The page for checkout"""
    context = {
        "id": id,
    }
    return render(request, "checkout.html")


def index(request):
    return HttpResponse("Hello World")


def navbar(request):
    return render(request, 'navbar.html')


def carlist(request):
    return render(request, 'carlist.html')


def detail(request):
    context = {
        'car_name': "うんち",
        'owner_name': "うんちマン",
        'price': 900,
        'rental_avail': True,
        'address': "埼玉県所沢市",
    }
    return render(request, 'car_detail.html', context)
