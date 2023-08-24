from django.http import HttpResponse
from django.shortcuts import render


# Please add below.
def car_list(request):
    """The page for car list"""
    return render(request, "che_project_app/car_list.html")


def chat(request, id):
    """The page for car list"""
    context = {
        "id": id,
    }
    return render(request, "che_project_app/chat.html", context)


def detail_view(request, id):
    # Retrieve data based on the id parameter and pass it to the template
    context = {
        "id": id,
    }
    return render(request, "che_project_app/detail.html", context)


def index(request):
    return render(request, "che_project_app/index.html")
